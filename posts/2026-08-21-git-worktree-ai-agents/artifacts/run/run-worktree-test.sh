#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DEMO_ROOT="$(mktemp -d /tmp/devlog-worktree-test.XXXXXX)"
DEMO_ROOT="$(cd "$DEMO_ROOT" && pwd -P)"
REPO="$DEMO_ROOT/shop-app"

cleanup() {
  if [ -d "$REPO/.git" ]; then
    git -C "$REPO" merge --abort >/dev/null 2>&1 || true
    git -C "$REPO" worktree remove "$DEMO_ROOT/agent-claude" >/dev/null 2>&1 || true
    git -C "$REPO" worktree remove "$DEMO_ROOT/agent-codex" >/dev/null 2>&1 || true
    git -C "$REPO" worktree remove "$DEMO_ROOT/agent-a" >/dev/null 2>&1 || true
    git -C "$REPO" worktree remove "$DEMO_ROOT/agent-b" >/dev/null 2>&1 || true
  fi
  rm -rf "$DEMO_ROOT"
}
trap cleanup EXIT

mkdir -p "$REPO"
cp -R "$SCRIPT_DIR/fixture/." "$REPO/"
git -C "$REPO" init -b main >/dev/null
git -C "$REPO" config user.name "dev.log test"
git -C "$REPO" config user.email "test@example.invalid"
git -C "$REPO" add .
git -C "$REPO" commit -m "chore: initial demo" >/dev/null

echo '$ git --version'
git --version
echo '$ git status --short --branch'
git -C "$REPO" status --short --branch

echo
echo '$ git worktree add -b feat/home-copy ../agent-claude main'
git -C "$REPO" worktree add -b feat/home-copy "$DEMO_ROOT/agent-claude" main
echo '$ git worktree add -b docs/agent-rule ../agent-codex main'
git -C "$REPO" worktree add -b docs/agent-rule "$DEMO_ROOT/agent-codex" main
echo '$ git worktree list'
git -C "$REPO" worktree list | sed "s#$DEMO_ROOT#~/worktree-demo#g"

git -C "$DEMO_ROOT/agent-claude" apply "$SCRIPT_DIR/patches/claude-copy.patch"
git -C "$DEMO_ROOT/agent-codex" apply "$SCRIPT_DIR/patches/codex-readme.patch"

echo
echo '$ (cd ../agent-claude && git status --short --branch)'
git -C "$DEMO_ROOT/agent-claude" status --short --branch
echo '$ (cd ../agent-codex && git status --short --branch)'
git -C "$DEMO_ROOT/agent-codex" status --short --branch
echo '$ git status --short --branch  # main worktree'
git -C "$REPO" status --short --branch

git -C "$DEMO_ROOT/agent-claude" add index.html
git -C "$DEMO_ROOT/agent-claude" commit -m "feat: clarify intro copy" >/dev/null
git -C "$DEMO_ROOT/agent-codex" add README.md
git -C "$DEMO_ROOT/agent-codex" commit -m "docs: add agent rule" >/dev/null

echo
echo '$ git merge --no-ff feat/home-copy'
git -C "$REPO" merge --no-ff feat/home-copy -m "merge: home copy" | sed "s#$DEMO_ROOT#~/worktree-demo#g"
echo '$ git merge --no-ff docs/agent-rule'
git -C "$REPO" merge --no-ff docs/agent-rule -m "merge: agent rule" | sed "s#$DEMO_ROOT#~/worktree-demo#g"
echo '$ git log --graph --oneline --decorate --all --max-count=8'
git -C "$REPO" log --graph --oneline --decorate --all --max-count=8

git -C "$REPO" worktree remove "$DEMO_ROOT/agent-claude"
git -C "$REPO" worktree remove "$DEMO_ROOT/agent-codex"
git -C "$REPO" worktree add -b test/button-a "$DEMO_ROOT/agent-a" main >/dev/null
git -C "$REPO" worktree add -b test/button-b "$DEMO_ROOT/agent-b" main >/dev/null
git -C "$DEMO_ROOT/agent-a" apply "$SCRIPT_DIR/patches/conflict-a.patch"
git -C "$DEMO_ROOT/agent-b" apply "$SCRIPT_DIR/patches/conflict-b.patch"
git -C "$DEMO_ROOT/agent-a" add index.html
git -C "$DEMO_ROOT/agent-a" commit -m "test: button label A" >/dev/null
git -C "$DEMO_ROOT/agent-b" add index.html
git -C "$DEMO_ROOT/agent-b" commit -m "test: button label B" >/dev/null

echo
echo '$ git merge --no-ff test/button-a'
git -C "$REPO" merge --no-ff test/button-a -m "merge: button A" | sed "s#$DEMO_ROOT#~/worktree-demo#g"
echo '$ git merge --no-ff test/button-b'
set +e
git -C "$REPO" merge --no-ff test/button-b -m "merge: button B"
MERGE_STATUS=$?
set -e
echo "merge_exit_code=$MERGE_STATUS"
echo '$ git status --short'
git -C "$REPO" status --short
echo '$ git diff --name-only --diff-filter=U'
git -C "$REPO" diff --name-only --diff-filter=U
git -C "$REPO" merge --abort

echo
echo '$ git worktree remove ../agent-a'
git -C "$REPO" worktree remove "$DEMO_ROOT/agent-a"
echo '$ git worktree remove ../agent-b'
git -C "$REPO" worktree remove "$DEMO_ROOT/agent-b"
echo '$ git worktree list'
git -C "$REPO" worktree list | sed "s#$DEMO_ROOT#~/worktree-demo#g"
echo '$ git worktree prune --dry-run'
git -C "$REPO" worktree prune --dry-run

if [ "$MERGE_STATUS" -eq 0 ]; then
  echo 'expected merge conflict did not occur' >&2
  exit 1
fi

echo
echo 'RESULT: PASS - isolated edits merged cleanly; same-line edits conflicted as expected.'

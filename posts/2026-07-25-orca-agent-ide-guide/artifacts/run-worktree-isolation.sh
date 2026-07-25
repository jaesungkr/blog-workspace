#!/usr/bin/env bash
set -euo pipefail

experiment_root="$(mktemp -d "${TMPDIR:-/tmp}/orca-worktree-test.XXXXXX")"
trap 'rm -rf "$experiment_root"' EXIT

repo_dir="$experiment_root/repo"
worktree_a="$experiment_root/agent-a"
worktree_b="$experiment_root/agent-b"

git init -q "$repo_dir"
git -C "$repo_dir" config user.name "Codex experiment"
git -C "$repo_dir" config user.email "codex-experiment@example.invalid"
printf 'mode=base\n' > "$repo_dir/config.txt"
git -C "$repo_dir" add config.txt
git -C "$repo_dir" commit -qm "base"

git -C "$repo_dir" worktree add -qb agent-a "$worktree_a"
git -C "$repo_dir" worktree add -qb agent-b "$worktree_b"

printf 'mode=agent-a\n' > "$worktree_a/config.txt"
printf 'mode=agent-b\n' > "$worktree_b/config.txt"

echo "[environment]"
uname -srm
git --version
echo
echo "[registered worktrees]"
git -C "$repo_dir" worktree list --porcelain
echo "[main checkout]"
printf 'content='
tr -d '\n' < "$repo_dir/config.txt"
printf ' status='
git -C "$repo_dir" status --short | tr -d '\n'
echo
echo "[agent-a worktree]"
printf 'content='
tr -d '\n' < "$worktree_a/config.txt"
printf ' status='
git -C "$worktree_a" status --short | tr -d '\n'
echo
echo "[agent-b worktree]"
printf 'content='
tr -d '\n' < "$worktree_b/config.txt"
printf ' status='
git -C "$worktree_b" status --short | tr -d '\n'
echo
echo "[disk usage]"
du -sk "$repo_dir" "$worktree_a" "$worktree_b"

git -C "$worktree_a" add config.txt
git -C "$worktree_a" commit -qm "agent-a change"
git -C "$worktree_b" add config.txt
git -C "$worktree_b" commit -qm "agent-b change"
git -C "$repo_dir" merge -q agent-a

echo
echo "[merge collision]"
set +e
merge_output="$(git -C "$repo_dir" merge agent-b 2>&1)"
merge_exit=$?
set -e
printf 'exit=%s\n' "$merge_exit"
printf '%s\n' "$merge_output"
echo "conflict_markers=$(grep -Ec '^(<<<<<<<|=======|>>>>>>>)' "$repo_dir/config.txt")"
git -C "$repo_dir" merge --abort

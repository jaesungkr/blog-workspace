#!/bin/sh
set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repository_root=$(CDPATH= cd -- "$script_dir/.." && pwd)
skill_sources="$repository_root/.agents/skills"
codex_root="${CODEX_HOME:-$HOME/.codex}"
skills_directory="$codex_root/skills"

if [ ! -d "$skill_sources" ]; then
  echo "Skill directory not found: $skill_sources" >&2
  exit 1
fi

mkdir -p "$skills_directory"

for skill_source in "$skill_sources"/dev-log-*; do
  if [ ! -f "$skill_source/SKILL.md" ]; then
    continue
  fi

  skill_name=$(basename "$skill_source")
  skill_target="$skills_directory/$skill_name"

  if [ -L "$skill_target" ]; then
    current_target=$(readlink "$skill_target")
    if [ "$current_target" = "$skill_source" ]; then
      echo "Already linked: $skill_target -> $skill_source"
      continue
    fi

    echo "Refusing to replace existing link: $skill_target -> $current_target" >&2
    exit 1
  fi

  if [ -e "$skill_target" ]; then
    echo "Refusing to replace existing path: $skill_target" >&2
    exit 1
  fi

  ln -s "$skill_source" "$skill_target"
  echo "Linked Git-managed skill: $skill_target -> $skill_source"
done

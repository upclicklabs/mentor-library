#!/bin/bash
set -euo pipefail

# Only run in remote (web) sessions
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

REPO="upclicklabs/mentor-library"
SKILLS_DIR="$HOME/.claude/skills"
CLAUDE_MD="$HOME/.claude/CLAUDE.md"

mkdir -p "$SKILLS_DIR"

###############################################################################
# 1. Fetch the list of all files under skills/ from the repo
###############################################################################
TREE=$(gh api "repos/$REPO/git/trees/main?recursive=1" --jq '.tree[] | select(.path | startswith("skills/")) | .path' 2>/dev/null || true)

if [ -z "$TREE" ]; then
  echo "Warning: Could not fetch skill list from $REPO" >&2
  exit 0
fi

###############################################################################
# 2. Download each skill file into ~/.claude/skills/
###############################################################################
echo "$TREE" | while IFS= read -r filepath; do
  # Skip the global-CLAUDE.md — handled separately below
  if [ "$filepath" = "skills/global-CLAUDE.md" ]; then
    continue
  fi

  # e.g. skills/mentor-borris/SKILL.md → mentor-borris/SKILL.md
  relative="${filepath#skills/}"
  dest="$SKILLS_DIR/$relative"

  mkdir -p "$(dirname "$dest")"

  # Download the file content (base64-encoded from GitHub API, decode it)
  gh api "repos/$REPO/contents/$filepath" --jq '.content' 2>/dev/null \
    | base64 -d > "$dest" 2>/dev/null || true
done

###############################################################################
# 3. Install global CLAUDE.md (session memory instructions)
###############################################################################
GLOBAL_CLAUDE=$(gh api "repos/$REPO/contents/skills/global-CLAUDE.md" --jq '.content' 2>/dev/null || true)

if [ -n "$GLOBAL_CLAUDE" ]; then
  echo "$GLOBAL_CLAUDE" | base64 -d > "$CLAUDE_MD" 2>/dev/null || true
fi

echo "Mentor skills and session memory installed from $REPO"

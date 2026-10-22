#!/usr/bin/env bash
# Install Tayyib into an agent's skills directory (for agents that do not use Claude Code plugins).
# Claude Code users: /plugin install tayyib --marketplace me2resh/tayyib
# Usage: ./install.sh [claude|codex|all|<directory>]
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
TARGET="${1:-all}"
copy() { mkdir -p "$1"; rm -rf "$1/tayyib"; mkdir -p "$1/tayyib"; cp -R "$HERE/skills/tayyib/." "$1/tayyib/"; echo "installed: $1/tayyib"; }
case "$TARGET" in
  claude) copy "$HOME/.claude/skills" ;;
  codex)  copy "$HOME/.codex/skills" ;;
  all)    copy "$HOME/.claude/skills"; copy "$HOME/.codex/skills" ;;
  *)      copy "$TARGET" ;;
esac
echo "Cursor: copy .cursor/rules/tayyib.mdc into your project. Copilot: copy .github/copilot-instructions.md. Other agents: add AGENTS.md to their instructions and keep skills/tayyib/ readable."

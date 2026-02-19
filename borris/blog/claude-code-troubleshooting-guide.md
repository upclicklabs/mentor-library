---
title: "Reference the Claude Code troubleshooting guide"
source_url: "https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/troubleshooting"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Reference the Claude Code troubleshooting guide

Solutions to common issues with Claude Code installation and usage.

## Common Installation Issues

### Windows Installation Issues: Errors in WSL

**OS/platform detection issues**: If you receive an error during installation, WSL may be using Windows npm. Try:
- Run `npm config set os linux` before installation
- Install with `npm install -g @anthropic-ai/claude-code --force --no-os-check` (do NOT use sudo)

**Node not found errors**: If you see `exec: node: not found` when running `claude`, your WSL environment may be using a Windows installation of Node.js. Confirm with `which npm` and `which node` (should point to Linux paths starting with `/usr/`). Fix by installing Node via your Linux distribution's package manager or via nvm.

**nvm version conflicts**: If nvm is installed in both WSL and Windows, version conflicts may occur. Ensure nvm is properly loaded in your shell config:

```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```

### WSL2 Sandbox Setup

Sandboxing is supported on WSL2 but requires installing additional packages:

```bash
# Ubuntu/Debian
sudo apt-get install bubblewrap socat

# Fedora
sudo dnf install bubblewrap socat
```

WSL1 does not support sandboxing.

### Linux and Mac Installation: Permission or Command Not Found Errors

#### Recommended: Native Claude Code Installation

```bash
# macOS, Linux, WSL - Install stable version
curl -fsSL https://claude.ai/install.sh | bash

# Install latest version
curl -fsSL https://claude.ai/install.sh | bash -s latest

# Install specific version
curl -fsSL https://claude.ai/install.sh | bash -s 1.0.58
```

```powershell
# Windows PowerShell - Install stable version
irm https://claude.ai/install.ps1 | iex
```

This installs the appropriate build for your OS and adds a symlink at `~/.local/bin/claude`.

### Windows: Git-Bash Required

Claude Code on native Windows requires Git for Windows (includes Git Bash). If Git is installed but not detected, set the path explicitly:

```powershell
$env:CLAUDE_CODE_GIT_BASH_PATH="C:\Program Files\Git\bin\bash.exe"
```

### Windows: installMethod is native, but claude command not found

Add `%USERPROFILE%\.local\bin` to your user PATH via System Properties > Environment Variables. Verify with `claude doctor`.

## Permissions and Authentication

### Repeated Permission Prompts

Use the `/permissions` command to allow specific tools to run without approval.

### Authentication Issues

1. Run `/logout` to sign out completely
2. Close Claude Code
3. Restart with `claude` and complete authentication again
4. If browser doesn't open, press `c` to copy the OAuth URL

If problems persist:
```bash
rm -rf ~/.config/claude-code/auth.json
claude
```

## Configuration File Locations

| File | Purpose |
|------|---------|
| `~/.claude/settings.json` | User settings (permissions, hooks, model overrides) |
| `.claude/settings.json` | Project settings (checked into source control) |
| `.claude/settings.local.json` | Local project settings (not committed) |
| `~/.claude.json` | Global state (theme, OAuth, MCP servers) |
| `.mcp.json` | Project MCP servers (checked into source control) |

### Resetting Configuration

```bash
# Reset all user settings and state
rm ~/.claude.json
rm -rf ~/.claude/

# Reset project-specific settings
rm -rf .claude/
rm .mcp.json
```

## Performance and Stability

### High CPU or Memory Usage

1. Use `/compact` regularly to reduce context size
2. Close and restart Claude Code between major tasks
3. Add large build directories to `.gitignore`

### Command Hangs or Freezes

1. Press Ctrl+C to cancel the current operation
2. If unresponsive, close the terminal and restart

### Search and Discovery Issues

If Search tool, `@file` mentions, custom agents, and custom skills are not working, install system `ripgrep`:

```bash
# macOS
brew install ripgrep

# Windows
winget install BurntSushi.ripgrep.MSVC

# Ubuntu/Debian
sudo apt install ripgrep
```

Then set `USE_BUILTIN_RIPGREP=0` in your environment.

### Slow or Incomplete Search Results on WSL

Disk read performance penalties when working across file systems on WSL may result in fewer-than-expected matches. Solutions:
1. Submit more specific searches with directory or file type constraints
2. Move project to Linux filesystem (`/home/`) rather than Windows filesystem (`/mnt/c/`)
3. Run Claude Code natively on Windows instead of through WSL

## IDE Integration Issues

### JetBrains IDE Not Detected on WSL2

**Option 1: Configure Windows Firewall** (recommended)
- Find WSL2 IP with `wsl hostname -I`
- Create a firewall rule in PowerShell (Administrator):
```powershell
New-NetFirewallRule -DisplayName "Allow WSL2 Internal Traffic" -Direction Inbound -Protocol TCP -Action Allow -RemoteAddress 172.21.0.0/16 -LocalAddress 172.21.0.0/16
```

**Option 2: Switch to mirrored networking**
Add to `.wslconfig`:
```ini
[wsl2]
networkingMode=mirrored
```
Then restart WSL with `wsl --shutdown`.

### Escape Key Not Working in JetBrains Terminals

Go to Settings > Tools > Terminal, then either uncheck "Move focus to the editor with Escape" or delete the "Switch focus to Editor" shortcut.

## Markdown Formatting Issues

### Missing Language Tags in Code Blocks

Solutions:
1. Ask Claude to add language tags to all code blocks
2. Set up post-processing hooks for automatic formatting
3. Manually review generated markdown files

### Best Practices for Markdown Generation

- Be explicit: ask for "properly formatted markdown with language-tagged code blocks"
- Document preferred markdown style in CLAUDE.md
- Set up validation hooks for automatic verification

## Getting More Help

1. Use `/bug` command within Claude Code to report problems to Anthropic
2. Check the [GitHub repository](https://github.com/anthropics/claude-code) for known issues
3. Run `/doctor` to diagnose issues (checks installation, auto-update, settings files, MCP config, keybindings, context usage, plugin errors)
4. Ask Claude directly about its capabilities and features

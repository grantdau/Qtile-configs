# Qtile Configuration

This repository contains my personal Qtile window manager configuration.

## Features

- Custom keybindings for efficient window and workspace management
- Multi-monitor support
- Autostart script for monitor setup
- Shortcuts for launching common applications

## Dependencies

- Qtile
- Tilix (terminal emulator)
- Firefox
- Steam
- Spotify (Flatpak)
- Tutanota (Flatpak)

## Installation

1. Clone this repository to your `~/.config/qtile/` directory.
2. Ensure you have all the dependencies installed.
3. Log out and log back in, selecting Qtile as your window manager.

## Keybindings Cheat Sheet

### Window Management

| Keybinding | Action |
|------------|--------|
| `Mod + h` | Move focus left |
| `Mod + l` | Move focus right |
| `Mod + j` | Move focus down |
| `Mod + k` | Move focus up |
| `Mod + Space` | Move window focus to other window |
| `Mod + Shift + h` | Move window left |
| `Mod + Shift + l` | Move window right |
| `Mod + Shift + j` | Move window down |
| `Mod + Shift + k` | Move window up |
| `Mod + Control + h` | Grow window to the left |
| `Mod + Control + l` | Grow window to the right |
| `Mod + Control + j` | Grow window down |
| `Mod + Control + k` | Grow window up |
| `Mod + n` | Reset all window sizes |
| `Mod + w` | Kill focused window |
| `Mod + f` | Toggle fullscreen on focused window |
| `Mod + t` | Toggle floating on focused window |

### Workspace Management

| Keybinding | Action |
|------------|--------|
| `Mod + [1-9]` | Switch to group [1-9] |
| `Mod + Shift + [1-9]` | Move focused window to group [1-9] |

### Multi-monitor

| Keybinding | Action |
|------------|--------|
| `Mod + Right` | Focus next monitor |
| `Mod + Left` | Focus previous monitor |
| `Mod + Shift + Right` | Move window to next monitor |
| `Mod + Shift + Left` | Move window to previous monitor |
| `Mod + period` | Move focus to next monitor |
| `Mod + comma` | Move focus to previous monitor |

### Layout Management

| Keybinding | Action |
|------------|--------|
| `Mod + Tab` | Toggle between layouts |
| `Mod + Shift + Return` | Toggle between split and unsplit stack |

### Application Shortcuts

| Keybinding | Action |
|------------|--------|
| `Mod + Return` | Launch Tilix |
| `Mod + Shift + s` | Launch Steam |
| `Mod + s` | Launch Spotify |
| `Mod + e` | Launch Tutanota |
| `Mod + i` | Launch Firefox |

### Qtile Management

| Keybinding | Action |
|------------|--------|
| `Mod + Control + r` | Reload Qtile config |
| `Mod + Control + q` | Shutdown Qtile |
| `Mod + r` | Spawn command prompt |

Note: `Mod` key is set to the Super key (Windows key on most keyboards).

## Customization

To customize this configuration, edit the `config.py` file in your `~/.config/qtile/` directory. Refer to the [Qtile documentation](http://docs.qtile.org/) for more information on available options and features.

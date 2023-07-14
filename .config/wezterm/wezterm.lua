local wezterm = require 'wezterm'
local keybinds = require 'keybinds'
local launcher = require 'launcher'
-- local on = require 'on'

-- Create config table
local config = {}

-- Start config_builder
if wezterm.config_builder then
	config = wezterm.config_builder()
end

-- Set color scheme
-- config.color_scheme = 'AdventureTime'
config.color_scheme = 'BirdsOfParadise'

-- Tab_bar settings
config.enable_tab_bar = false
config.use_fancy_tab_bar = true

-- Window settings
config.enable_scroll_bar = false
config.window_decorations = NONE
config.window_padding = {
	left = 5,
	right = 0,
	top = 5,
	bottom = 0,
}

-- Font settings
config.font_size = 12
config.font = wezterm.font_with_fallback {
		'Jetbrains mono',
		'Font Awesome 6 Free',
	}

-- Keybinds
keybinds.apply_to_config(config)

-- Launcher settings
launcher.apply_to_config(config)

return config

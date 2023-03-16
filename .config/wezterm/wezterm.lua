local wezterm = require 'wezterm'

local act = wezterm.action
return {
	color_scheme = 'BirdsOfParadise',
	enable_tab_bar = false,
	window_decorations = "NONE",
	font_size = 15,
	font = wezterm.font_with_fallback {
		'JetBrains Mono',
		'Font Awesome 6 Free',
	},
	keys = {
		-- Pane Management
		
		-- Create
		{mods = "CTRL|SHIFT|ALT", key = "h", action = act.SplitPane{direction="Left"}},
		{mods = "CTRL|SHIFT|ALT", key = "j", action = act.SplitPane{direction="Down"}},
		{mods = "CTRL|SHIFT|ALT", key = "k", action = act.SplitPane{direction="Up"}},
		{mods = "CTRL|SHIFT|ALT", key = "l", action = act.SplitPane{direction="Right"}},
		
		-- Destroy
		{mods = "CTRL|SHIFT", key = "d", action = act.CloseCurrentPane{confirm=true}},
		
		-- Navigation
		{mods = "CTRL|SHIFT", key = "h", action = act.ActivatePaneDirection("Left")},
		{mods = "CTRL|SHIFT", key = "j", action = act.ActivatePaneDirection("Down")},
		{mods = "CTRL|SHIFT", key = "k", action = act.ActivatePaneDirection("Up")},
		{mods = "CTRL|SHIFT", key = "l", action = act.ActivatePaneDirection("Right")},
		{mods = "CTRL|SHIFT", key = "Space", action = act.PaneSelect{mode="Activate"}},

		-- Manipulation
		{mods = "CTRL|SHIFT", key = "s", action = act.PaneSelect{mode="SwapWithActive"}},
	}
}
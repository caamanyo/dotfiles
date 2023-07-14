local wezterm = require 'wezterm'
local act = wezterm.action
local mux = wezterm.mux

local function open_python_project()
  local project_dir = wezterm.home_dir .. '/Projects/ls-export-files'
  local tab, build_pane, window = mux.spawn_window {
    workspace = 'coding',
    cwd = project_dir,
    args = args,
  }
  local editor_pane = build_pane:split {
    direction = 'Top',
    size = 0.6,
    cwd = project_dir,
  }
  -- may as well kick off a build in that pane
  build_pane:send_text 'pipenv shell\n'
end

local module = {}
local launcher = {
	{args = {'bashtop'},},
	{
		label = 'Open python project',
		args = { 'wezterm start --always-new-process' },
	}

}



function module.apply_to_config(config)
	config.launch_menu = launcher
end


return module
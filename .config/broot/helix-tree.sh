filename=$1
zellij action focus-previous-pane
zellij action write-chars ":open $filename"
zellij action write 13

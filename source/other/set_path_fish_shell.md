# set PATH fish shell

first, edit this
- `nvim /home/$(whoami)/.config/fish/config.fish`

add this line before `if status is-interactive`
`set -gx PATH /new/path $PATH`
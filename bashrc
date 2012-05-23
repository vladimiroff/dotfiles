# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Load every single file in ./bash
for f in $HOME/dotfiles/bash/*; do [ -f "$f" ] && source $f; done

PS1='[\u@\h \W]$(parse_git_branch)\$ '
# xhost +local: &> /dev/null

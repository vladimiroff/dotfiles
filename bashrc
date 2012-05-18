# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Load every single file in ./bash
source $HOME/dotfiles/bash/*

PS1='[\u@\h \W]$(parse_git_branch)\$ '
# xhost +local: &> /dev/null

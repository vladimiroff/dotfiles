# If not running interactively, don't do anything
export LANG='en_US.UTF-8'
[[ $- != *i* ]] && return

# I don't always run tmux
# But when I do, I want it in 256 colors and with UTF-8 support
[ -n "$TMUX" ] && export TERM=screen-256color
alias tmux='tmux -u -2'

# sudo bash-comletion
complete -cf please

# Load every single file in ./bash
source ~/dotfiles/bash/*

function parse_git_dirty {
  [[ $(git status 2> /dev/null | tail -n1) != "nothing to commit (working directory clean)" ]] && echo "*"
}
function parse_git_branch {
    git branch --no-color 2> /dev/null | sed -e '/^[^*]/d' -e "s/* \(.*\)/(\1$(parse_git_dirty))/"
}
PS1='[\u@\h \W]$(parse_git_branch)\$ '
export _JAVA_OPTIONS='-Dawt.useSystemAAFontSettings=on -Dswing.defaultlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel'

# xhost +local: &> /dev/null
KWIN_DIRECT_GL=1

# Add ~/dotfiles/bin/ to PATH
export PATH=~/dotfiles/bin:$PATH

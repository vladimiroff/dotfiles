#!/bin/sh

xset r rate 150 50

setxkbmap -layout "us,bg(phonetic)"
setxkbmap -option grp:alt_shift_toggle,grp_led:scroll
xmodmap .Xmodmap

exec awesome
#exec startkde

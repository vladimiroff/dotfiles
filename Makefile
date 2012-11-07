SHELL := /bin/bash

install: install-bash install-tmux install-git install-vim install-pip install-ipython install-pentadactyl install-fonts

install-bash:
	ln -fs `pwd`/bashrc ~/.bashrc

install-tmux:
	ln -fs `pwd`/tmux.conf ~/.tmux.conf

install-git:
	ln -fs `pwd`/gitconfig ~/.gitconfig

install-vim:
	[[ -d ~/.vim ]] || ( git clone git@github.com:Vladimiroff/Vimfiles.git ~/.vim && cd ~/.vim && make install )

install-ipython:
	[[ -d ~/.config/ipython ]] || mkdir -p ~/.config/ipython/profile_default
	ln -fs `pwd`/ipython/profile_default/ipython_config.py ~/.config/ipython/profile_default/ipython_config.py

install-pip:
	mkdir -p ~/.pip
	ln -fs `pwd`/pip.conf ~/.pip/pip.conf

install-pentadactyl:
	ln -fs `pwd`/pentadactylrc ~/.pentadactylrc

install-fonts:
	[[ -d ~/.fonts ]] || mkdir -p ~/.fonts
	ln -fs `pwd`/fonts/* ~/.fonts

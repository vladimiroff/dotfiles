SHELL := /bin/bash

install: install-bash install-tmux install-git install-vim install-pip

install-bash:
	ln -fs `pwd`/bashrc ~/.bashrc

install-tmux:
	ln -fs `pwd`/tmux.conf ~/.tmux.conf

install-git:
	ln -fs `pwd`/gitconfig ~/.gitconfig

install-vim:
	[[ -d ~/.vim ]] || ( git clone git@github.com:Vladimiroff/Vimfiles.git ~/.vim && cd ~/.vim && make install )

install-pip:
	mkdir -p ~/.pip
	ln -fs `pwd`/pip.conf ~/.pip/pip.conf

ALL   := bash tmux X git mercurial vim ipython ranger zsh systemd mutt

dotfiles = `pwd`

update:
	git pull
	git submodule sync
	git submodule foreach "git checkout master; git pull origin master; echo"
	$(MAKE) install

install: $(ALL:%=install-%)

install-X:
	mkdir -p ~/.config/touchegg
	ln -fs $(dotfiles)/x11/Xmodmap ~/.Xmodmap
	ln -fs $(dotfiles)/x11/xinitrc ~/.xinitrc
	ln -fs $(dotfiles)/x11/Xdefaults ~/.Xdefaults
	ln -fs $(dotfiles)/x11/Xresources ~/.Xresources
	ln -fs $(dotfiles)/x11/touchegg.conf ~/.config/touchegg/touchegg.conf
	ln -fs $(dotfiles)/x11/libinput-gestures.conf ~/.config/libinput-gestures.conf

install-bash:
	ln -fs $(dotfiles)/sh/rc ~/.bashrc
	ln -fs $(dotfiles)/bash/profile ~/.bash_profile

install-tmux:
	ln -fs $(dotfiles)/tmux/tmux.conf ~/.tmux.conf

install-git:
	ln -fs $(dotfiles)/gitconfig ~/.gitconfig

install-vim:
	[[ -d ~/.vim ]] || ( git clone git@github.com:Vladimiroff/Vimfiles.git ~/.vim && cd ~/.vim && make install )
	ln -fs $(dotfiles)/ctags ~/.ctags

install-ipython:
	[[ -d ~/.ipython ]] || mkdir -p ~/.ipython/profile_default
	ln -fs $(dotfiles)/ipython/profile_default/ipython_config.py ~/.ipython/profile_default/ipython_config.py

install-ranger:
	mkdir -p ~/.config/ranger/
	ln -fs $(dotfiles)/ranger/* ~/.config/ranger/

install-zsh:
	ln -fs $(dotfiles)/sh/rc ~/.zshrc

install-mercurial:
	ln -fs $(dotfiles)/hgrc ~/.hgrc

install-systemd:
	mkdir -p ~/.config/systemd/user/
	cp $(dotfiles)/systemd/user/* ~/.config/systemd/user/
	sed -i "/Environment\=/c\Environment\=\"DOTFILES\=$(dotfiles)\"" ~/.config/systemd/user/offlineimap.service

install-mutt:
	ln -fs $(dotfiles)/mail/mutt/ ~/.mutt
	ln -fs $(dotfiles)/mail/offlineimaprc ~/.offlineimaprc
	ln -fs $(dotfiles)/mail/msmtprc ~/.msmtprc
	mkdir -p ~/.cache/mutt/{headers,bodies,tmp}
	mkdir -p ~/.cache/mutt/{headers,bodies}

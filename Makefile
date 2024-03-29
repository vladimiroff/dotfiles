ALL := bash tmux git mercurial vim ipython zsh systemd konsole starship bat sqlite

dotfiles = `pwd`

update:
	git pull
	$(MAKE) install

env:
	mkdir -p ~/.config/environment.d
	cat $(dotfiles)/sh/environment  | awk '/^export/ { gsub(/^export /, ""); print }' > ~/.config/environment.d/dotfiles.conf

install: $(ALL:%=install-%) env

install-bash:
	ln -fs $(dotfiles)/sh/dir_colors ~/.dir_colors
	ln -fs $(dotfiles)/bash/rc ~/.bashrc
	ln -fs $(dotfiles)/bash/profile ~/.bash_profile

install-tmux:
	ln -fs $(dotfiles)/tmux/tmux.conf ~/.tmux.conf

install-git:
	ln -fs $(dotfiles)/gitconfig ~/.gitconfig

install-vim:
	[[ -d ~/.vim ]] || ( git clone git@github.com:Vladimiroff/Vimfiles.git ~/.vim && cd ~/.vim && make install )

install-ipython:
	[[ -d ~/.ipython ]] || mkdir -p ~/.ipython/profile_default
	ln -fs $(dotfiles)/ipython/profile_default/ipython_config.py ~/.ipython/profile_default/ipython_config.py

install-zsh:
	ln -fs $(dotfiles)/zsh/rc ~/.zshrc
	ln -fs $(dotfiles)/sh/environment ~/.zshenv

install-mercurial:
	ln -fs $(dotfiles)/hg/rc ~/.hgrc

install-systemd:
	mkdir -p ~/.config/systemd/user/
	cp $(dotfiles)/systemd/user/* ~/.config/systemd/user/

install-konsole:
	mkdir -p ~/.local/share/konsole/
	ln -fs $(dotfiles)/konsole/nord.colorscheme ~/.local/share/konsole/nord.colorscheme
	ln -fs $(dotfiles)/konsole/kiril.profile ~/.local/share/konsole/kiril.profile

install-starship:
	ln -fs $(dotfiles)/starship.toml ~/.config/starship.toml

install-bat:
	ln -sf $(dotfiles)/bat ~/.config/bat

install-sqlite:
	ln -sf $(dotfiles)/sqliterc ~/.sqliterc

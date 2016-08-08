c = get_config()

c.TerminalIPythonApp.display_banner = False
c.InteractiveShellApp.extensions = ['autoreload']
c.InteractiveShellApp.exec_lines = ['%autoreload 2']
c.TerminalInteractiveShell.confirm_exit = False

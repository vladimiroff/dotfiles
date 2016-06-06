# Configuration file for ipython.

c = get_config()

#------------------------------------------------------------------------------
# TerminalIPythonApp configuration
#------------------------------------------------------------------------------

c.TerminalIPythonApp.display_banner = False

#------------------------------------------------------------------------------
# InteractiveShellApp configuration
#------------------------------------------------------------------------------
c.InteractiveShellApp.extensions = ['autoreload']
c.InteractiveShellApp.exec_lines = ['%autoreload 2']

#------------------------------------------------------------------------------
# TerminalInteractiveShell configuration
#------------------------------------------------------------------------------

# TerminalInteractiveShell will inherit config from: InteractiveShell
c.TerminalInteractiveShell.autoedit_syntax = False
c.TerminalInteractiveShell.color_info = True
c.TerminalInteractiveShell.history_length = 10000
c.TerminalInteractiveShell.autoindent = True
c.TerminalInteractiveShell.colors = 'Linux'
c.TerminalInteractiveShell.separate_in = '\n'
c.TerminalInteractiveShell.show_rewritten_input = True
c.TerminalInteractiveShell.automagic = True
c.TerminalInteractiveShell.separate_out = ''
c.TerminalInteractiveShell.deep_reload = False
c.TerminalInteractiveShell.screen_length = 0
c.TerminalInteractiveShell.editor = 'vim'
c.TerminalInteractiveShell.confirm_exit = False
c.TerminalInteractiveShell.readline_remove_delims = '-/~'
c.TerminalInteractiveShell.logstart = False
c.TerminalInteractiveShell.logfile = ''
c.TerminalInteractiveShell.logappend = ''
c.TerminalInteractiveShell.pager = 'less'
c.TerminalInteractiveShell.autocall = 1
c.TerminalInteractiveShell.multiline_history = True
c.TerminalInteractiveShell.readline_use = True
c.TerminalInteractiveShell.quiet = False
c.TerminalInteractiveShell.term_title = True
c.TerminalInteractiveShell.object_info_string_level = 0
c.TerminalInteractiveShell.cache_size = 1000
c.TerminalInteractiveShell.ast_node_interactivity = 'last_expr'
c.TerminalInteractiveShell.pdb = False

#------------------------------------------------------------------------------
# PromptManager configuration
#------------------------------------------------------------------------------

c.PromptManager.in_template = '[\\#] >>> '
c.PromptManager.in2_template = '   .\\D.: '
c.PromptManager.out_template = '[\\#] <<< '
c.PromptManager.justify = True
c.PromptManager.color_scheme = 'Linux'

#------------------------------------------------------------------------------
# HistoryManager configuration
#------------------------------------------------------------------------------

c.HistoryManager.db_log_output = False
c.HistoryManager.db_cache_size = 0

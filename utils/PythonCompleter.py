import os
import sys 
import readline
import glob

class tabCompleter(object):
	''' A simple tab completer for linux '''
	def pathCompleter(self,text,state):
		line   = readline.get_line_buffer().split()
		if '~' in text:
			text = os.path.expanduser('~')
		if os.path.isdir(text):
			text += '/'
		return [x for x in glob.glob(text+'*')][state]

import sys

def good(message:str):
	''' Prints a message with [+] at the front to signify success '''
	print("[+] " + str(message))

def bad(message:str):
	''' Prints a message with [-] at the front to signify failure '''
	print("[-] " + str(message))
def info(message:str):
	''' Prints a message to signify information '''
	print("[ ] " + str(message))

def fatal(failure:str):
	print("[/] " + str(failure) + " failed, exiting now")
	sys.exit(1)

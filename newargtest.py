import sys

arguments = sys.argv
arguments[0] = ''
	
for argument in arguments:
	if len(argument) > 3:
		print(argument)


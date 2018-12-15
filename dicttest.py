import sys

list_arguments = sys.argv
del list_arguments[0]
list1 = []
for argument in list_arguments:
	if ":" in argument:
		list1.append(tuple(argument.split(":")))

dict1 = dict(list1)
for key, value in dict1.items():
	print("ID:{} Name:{}".format(key, value))	 

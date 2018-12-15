import sys

list_arguments = sys.argv
list_arguments[0] = ''
list_arguments_length_more_three = []
list_arguments_length_less_three = []
for argument in list_arguments:
	if len(argument) > 3:
		list_arguments_length_more_three.append(argument)
	else:
		list_arguments_length_less_three.append(argument)

print(list_arguments_length_more_three)
del list_arguments_length_less_three[0]
print(list_arguments_length_less_three)  

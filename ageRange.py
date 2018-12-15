import sys

age = int( sys.argv[1])
if 0 <= age and age< 10:
	print("you belong to kids")
elif 10 <= age and age <18:
	print("you belong to teenageer")
elif 18 <= age and age < 30:
	print("you belong to adult")
elif 30 <= age and age < 60:
	print("you belong to older")
elif 60 <= age and age < 120:
	print("you belong to oldest")

with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())


print()

filename = 'pi_digits.txt'

with open(filename) as file_object1:
	for line in file_object1:
		print(line.rstrip())


print()

with open(filename) as file_object2:
	lines = file_object2.readlines()

for line in lines:
	print(line.rstrip())
	

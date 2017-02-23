names = ['song', 'gao', 'yan', 'lang']

print("I want " + names[0] + ' ' + names[1] + ' ' + names[2] + ' ' + names[3] + ' ' + "have a dinner")

print(names[2] + " have something to do.")

names[2] = 'he'

print("I want " + names[0] + ' ' + names[1] + ' ' + names[2] + ' ' + names[3] + ' ' + "have a dinner")

print("I have a lot money")
names.insert(0, "gong")
names.insert(3 , "zou")
names.append("zhou")

for elem in names:
	print("I want " + elem.title() + " have dinner.")


print("two person")
num = len(names)
while num > 2:
	tmp = names.pop()
	print("sorry, "+tmp)
	num = len(names)

for elem in names:
	print(elem + ", I want have dinner with you.")
	
del names[0]
del names[0]

print(names)

	

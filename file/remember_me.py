import json

def greet_user():
#	filename = 'username.json'
	username = get_stored_username()
	if username:
		print("Wecome back, "+username+"!")
	else :
		username = get_new_username()
		print("We'll remember you when you come back, " + username + '!')

def get_new_username():
	username = input("What is your name?")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username
	
def get_stored_username():
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username


greet_user()

'''
#username = input("What is your name?")

filename = 'username.json'
try:
	with open(filename) as f_obj:
		username = json.load(f_obj)
except FileNotFoundError:
		username = input("What is your name?")
		with open(filename, 'w') as f_obj:
			json.dump(username, f_obj)
			print("We'll remember you when you come back, " + username + '!')
else:
	print("Welcome back, " + username + "!")
	
'''

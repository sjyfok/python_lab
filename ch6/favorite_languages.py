favorite_language = {
	'jen': 'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}

for name, language in favorite_language.items():
	print(name.title() + "'s favorite language is " + 
		language.title() + '.')
		
for name in favorite_language.keys():
	print(name.title())
	
friends = ['phil', 'sarah']
for name in favorite_language.keys():
	print(name.title())
	if name in friends:
		print(" Hi " + name.title() + 
			", I see your favorite language is " +
			favorite_language[name].title() + "!")
			

for name in sorted(favorite_language.keys()):
	print(name.title() + ", thank you for taking the poll.")
	
print()
for language in favorite_language.values():
	print(language)
	
print()
for language in set(favorite_language.values()):
	print(language)

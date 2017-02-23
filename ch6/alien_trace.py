alien_0 = {'x_pos' : 0, 'y_pos':25, 'speed' : 'medium'}

print("Original x-pos: " + str(alien_0['x_pos']))

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3
	
alien_0['x_pos'] = alien_0['x_pos']+x_increment
print("New x-pos:" + str(alien_0['x_pos']))
print(alien_0)
del alien_0['x_pos']
print(alien_0)


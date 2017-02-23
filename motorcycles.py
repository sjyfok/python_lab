motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append("ducati")
print(motorcycles)

motorcycles2 = []
motorcycles2.append("honda")
motorcycles2.append("yamaha")
motorcycles2.append("suzuki")
print(motorcycles2)

motorcycles2.insert(0, "ducati")
print(motorcycles2)

del motorcycles2[3]
print(motorcycles2)

motorcycles3 = ['honda', 'yamaha', 'suzuki']
print(motorcycles3)
popped_motorcyle = motorcycles3.pop()
print(motorcycles3)
print(popped_motorcyle)

motorcycles4 = ['honda', 'yamaha', 'suzuki']
last_owned= motorcycles4.pop()
print("The last motorcycle I owned was a " + last_owned.title()+".")


motorcycles5 = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles5.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title()+'.')

motorcycles6 = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles6)
motorcycles6.remove('ducati')
print(motorcycles6)


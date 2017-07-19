class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive(self):
		long_name = str(self.year)+' ' + self.make + ' ' + self.model
		return long_name.title()
	
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading)+" miles on it.")
		
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	
	def increment_odometer(self, miles):
		self.odometer_reading += miles

class Battery():
	def __init__(self, battery_size = 70):
		self.battery_size = battery_size
		
	def describe_battery(self):
		print("This Car has a "+str(self.battery_size)+" kwh battery.")
			
	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self_battery_size == 80:
			range = 270
		
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)			
		
class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(	make, model, year)
		self.battery = Battery(70)

	def describe_battery(self):
		print("This car has a " + str(self.battery_size) + "= kwh battery.")
	
if __name__ == '__main__':
	my_new_car = Car("audi", "a4", 2016)
	print(my_new_car.get_descriptive())
	my_new_car.read_odometer()
	my_new_car.update_odometer(23500)
	my_new_car.read_odometer()
	my_new_car.increment_odometer(100)
	my_new_car.read_odometer()
	print("")
	my_tesla = ElectricCar('tesla', 'model s', 2016)
	print(my_tesla.get_descriptive())
	my_tesla.battery.describe_battery()
	my_tesla.battery.get_range()

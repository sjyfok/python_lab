for num in range(1, 21):
	print(num)

numbers = list(range(1, 1000001))
#for num in numbers:
#	print(num)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = [value for value in range(1, 21, 2)]
for elem in odd_numbers:
	print(elem)

numby3 = [value for value in range(3, 31, 3)]
for elem in numby3:
	print(elem)
	
thrs = [value**3 for value in range(1, 11)]
for elem in thrs:
	print(elem)

thrs1 = list(thrs)
print(thrs1)




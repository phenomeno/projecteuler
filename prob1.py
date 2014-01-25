list = []



"""
for x in range(1,1000):
	if x % 3 == 0 or x % 5 == 0:
		list.append(x)
"""
		
for x in range(1, 1000):
	if x % 3 == 0:
		list.append(x)
	if x % 5 == 0:
		list.append(x)
	if x % 3 == 0 and x % 5 == 0:
		list.remove(x)
print list
summed_list = sum(list)

print summed_list

"""
for x in range(1, 1000):
	if x % 3 == 0:
		list.append(x)
	if x % 5 == 0:
		list.append(x)
	


for x in range(1, 1000):
	if x % 3 == 0:
		list.append(x)
	if x % 5 == 0:
		list.append(x)
	if x % 3 and x % 5 == 0:
		list.remove(x)
		
		"""
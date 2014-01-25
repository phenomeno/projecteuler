list = []



for x in range(0,1000):

	
	if x == 0 or x == 1 or x == 2:
		list.append(x)
		
		
	else:
	
	
		a = list[x-2]
		
		b = list[x-1]
	
		
		c = a + b
	
		
		if c < 4000000:
			list.append(c)
			
		else:
			break
		




print sum(list[2::3])
list = []

s = 2
a = 1
b = 2
for x in range(0,1000):	
		c = a + b
		if c >= 4000000: 
			break
		if c % 2 == 0:
			s += c
		a = b
		b = c
print s
#print sum(list[2::3])
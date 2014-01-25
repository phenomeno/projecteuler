import math

a = []
b = []



def prime(x): 
	b = []
	if x == 1: return True
	if x == 2: return True
	if x%2 == 0: return False
	for y in range(3,int(math.sqrt(x)),2):
		z = x % y
		b.append(z) 
	if 0 in b:
		return False
	else:
		return True
		
for x in range(1, 100):
	if prime(x):
		print x	
		
		
"""	
	
	
for x in range(1, int(math.sqrt(13195))):
	if True and prime(x) == True:
		a.append(x)
		
print a	
print a[-1]


#13195 % x == 0

"""
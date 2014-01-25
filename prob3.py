import math

a = []
b = []



def prime(x):
	for y in range(3,int(math.sqrt(600851475143))):
		if x != y:
			z = x % y
			b.append(z)
	if 0 in b:
		return False
	else:
		return True
			
	
	
	
for x in range(1, int(math.sqrt(600851475143))):
	if 13195 % x == 0 and prime(x) == True:
		a.append(x)
			
print a	
print a[-1]



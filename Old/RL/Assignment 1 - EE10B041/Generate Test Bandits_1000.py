import random
for i in range(2000):
	for j in range(1000):
		random.seed()
		print random.gauss(0,1),
	print '\n',

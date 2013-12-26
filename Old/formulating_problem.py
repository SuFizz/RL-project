import numpy
import math
import sys

def median_elimination(frame,delta,epsilon):
	reward = numpy.zeros(len(frame))
	number = (4/(epsilon**2))*math.log(3/delta);
	number = int(math.ceil(number))
#	number = 100
	for i in range(number):
		print i
		reward += numpy.random.standard_normal(len(frame)) + frame
		
	reward /= number
	med = numpy.median(reward)
#	print numpy.where(reward<med)
#	raw_input()
#	print numpy.where(reward>med)
	return numpy.delete(reward,numpy.where(reward<med)),numpy.where(reward>med)


if __name__ == "__main__":
	users = 20
	subframes = 10
	x = subframes/4
	mean_f = 8
	dev_f = 2
	
	frame_collect = numpy.array([[ 8,  9,  7,  8,  9,  5, 12,  7,  9,  8],
       [13, 10, 13,  7,  5,  9,  8,  8,  1, 11],
       [ 7,  7, 10,  9, 10,  8,  3,  7,  8, 11],
       [11,  8,  6, 11,  8,  7,  8,  6,  3,  9],
       [ 8,  7,  8,  3, 11,  7,  7,  9,  5, 13],
       [10, 11,  7,  8,  6,  8,  5,  8,  9,  7],
       [ 3, 11,  4,  9,  7,  8,  9,  5,  9, 11],
       [ 7,  7,  8,  8,  5, 10,  5,  4, 10, 10],
       [ 4,  9,  9, 10,  7,  8,  6, 10, 14,  8],
       [ 6, 11,  6,  6,  8, 13,  5,  3,  6, 12],
       [10,  9,  7,  9,  8,  5, 11, 13, 13,  4],
       [11,  8,  6, 11, 12,  9, 13,  4,  4,  3],
       [ 7,  7,  7, 14,  8,  6,  7,  9,  5, 14],
       [ 8,  6,  7,  7,  7, 15,  6,  9,  8, 14],
       [ 6, 10,  7,  6,  6, 11,  9,  4,  6, 10],
       [ 4,  6, 11,  7,  8, 10, 13,  5,  9, 11],
       [ 8,  4,  6,  3, 12,  5, 10,  4,  5,  8],
       [ 9,  6,  5,  7,  6,  6,  9,  6,  5,  8],
       [10,  9,  6,  9, 10,  6,  9,  9,  6,  3],
       [ 8,  6,  1,  9,  8,  9,  7,  6,  8,  9]]);
	
	#now we run median elimination on this system.
	#solving for each of the users as a MAB
	uu = []
	flags = numpy.zeros(users)
	epsilon = 1e-3/2
	delta = 1e-3/2
	eeww = []
	ree = []
	while 1:	
#		print here
		for i in range(users):
			print i
			print len(frame_collect[i]),x,'111'
			if (len(frame_collect[i]))/2 >= x:
				xxx = median_elimination(frame_collect[i],delta,epsilon);
				eeww.append(xxx)
				ree.append(eeww[i][0])
				uu.append(eeww[i][1])
			else:
				flags[i] = 1;
				print "here"
				continue;

#		raw_input()
#		print len(numpy.where(frame_collect,flags == 1)),users,"werree";
		if len(numpy.where(flags == 1)[0]) == users:
#			sys.exit(1)
			print uu[-users:]
			break
		frame_collect = numpy.array(ree)
		print uu[-users:]
		ree = []
		eeww = []
		delta /= 2
		epsilon *= 0.75

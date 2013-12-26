import numpy

N = 20			#no of users
M = 10			#no of subchannels

#assume that we have a thresholding function for the rewards so that everything greater than 3*mean we will say is ACK and anything below is NACK
mean = 5
stddev = 13
RpC = numpy.random.normal(mean,stddev,M)
alpha = 0.8
gamma = 0.9
epsilon = 0.9

#def greedy_action(Q,state):
#	return Q[state].argmax()
#	print output
#	llistt = []
#	i = 0
#	while output or i!=M:
#		llistt.append(output%10)
#		output/=10
#		i+=1
#	print llistt
#	llistt.reverse()
#	print llistt
#	llistt = numpy.array(llistt)

#	actions = numpy.where(llistt == 1)
#	print llistt
#	return actions

#def random_action():
#	_nos = numpy.random.randint(0,M)
#	rree = [numpy.random.randint(0,2) for b in range(0,M)]
#	rree = numpy.array(rree)
#	print rree
#	actions = numpy.where(rree == 1)
#	return actions

def convert(action):
	ee = int(bin(action)[2:])
	llist = []
	i=0
	while ee or i!=M:
		llist.append(ee%10)
		ee /=10
		i+=1
#	llist.reverse()
	llist = numpy.array(llist)
	actions = numpy.where(llist==1)
	return actions


def RS(action):
	while not action:
		action = numpy.random.randint(0,pow(2,M));
	_action = convert(action)
#	print _action
	rew = bool((sum(RpC[_action]) + sum(numpy.random.normal(0,1,len(_action[0]))))/len(_action[0]) > 3*mean)
#	print _action
	return (int(rew)-2*len(_action[0])),rew

if __name__ == "__main__":
	#master gets only a bunch of ACKS and NACKS
	#actions evolve as 
#	bandsTOuser = numpy.randint(1,M,N)	#randomly allocate 1 --> M bands as the case maybe throughout
	_states = 2
	Q = numpy.random.uniform(0,1,(_states,pow(2,M)))
	#I am starting in the NACK state because in the start I don't really know if there is anything happening
	state = 0

	_action = 123;		#arbit action

	x_es = []

	while 1:
		eep = numpy.random.uniform(0,1)

		Reward,state_new = RS(_action)
		if(eep < epsilon):					#then do the greedy action
			_action_ = Q[state].argmax();
#			print "greedy"

		else:
			_action_ = numpy.random.randint(0,pow(2,M));
			print "random"

#		print _action_
#		print _action
#		_action_ = converting(_action_)
#		_action = converting(_action)
		Q[state][_action] += alpha*(Reward + gamma*Q[state_new][_action_] - Q[state][_action])
		state = state_new
		_action = _action_
		print _action,Reward
		x_es.append(_action_)

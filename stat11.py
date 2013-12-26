import numpy

N = 20			#no of users
M = 10			#no of subchannels

#assume that we have a thresholding function for the rewards so that everything greater than 3*mean we will say is ACK and anything below is NACK
mean = 5
stddev = 13
threshold = 5

RpC = numpy.random.normal(mean,stddev,M)

alpha = 0.8
gamma = 0.9

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


def RS(action,maxe):
	while not action:
		action = numpy.random.randint(0,pow(2,M));
	_action = convert(action)
#	print _action
#	print maxe
	fee = (sum(RpC[_action]) + sum(numpy.random.standard_normal(len(_action[0]))))/len(_action[0])
	if (fee >= maxe):
		maxe = 0.5*fee;
		rew = max(1,2*fee)
	else:
		rew = min(-fee,fee)

	if fee>threshold:
		state = 1
	else:
		state = 0
#	print _action
	return rew+state*1.5,state,maxe


if __name__ == "__main__":
	#master gets only a bunch of ACKS and NACKS
	#actions evolve as 
#	bandsTOuser = numpy.randint(1,M,N)	#randomly allocate 1 --> M bands as the case maybe throughout
	maxe = -10
	_states = 2
	Q = numpy.random.uniform(0,1,(_states,pow(2,M)))
	#I am starting in the NACK state because in the start I don't really know if there is anything happening
	state = 0

	_action = 123;		#arbit action

	x_es = []

	t = 0


	while 1:
		epsilon = 0.999/9999000*(t)
		t+=1;
		if epsilon >= 0.9999:
			epsilon = 0.9999;
			
		eep = numpy.random.uniform(0,1)

		Reward,state_new,maxe = RS(_action,maxe)
		if(eep < epsilon):					#then do the greedy action
			_action_ = Q[state].argmax();

		else:
			_action_ = numpy.random.randint(0,pow(2,M));
#			print "random"

		Q[state][_action] += alpha*(Reward + gamma*Q[state_new][_action_] - Q[state][_action])
		state = state_new
		_action = _action_
		print state,_action,Reward
		x_es.append(_action)

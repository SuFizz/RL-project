import numpy

N = 200			#no of users
M = 100			#no of subchannels

#assume that we have a thresholding function for the rewards so that everything greater than 3*mean we will say is ACK and anything below is NACK
mean = 5
stddev = 13
threshold = 3

meanvalue = 1
modevalue = numpy.sqrt(2 / numpy.pi) * meanvalue

RpC = numpy.random.normal(mean,stddev,(N,M))

alpha = 0.8
gamma = 0.9

#def dispute(action):
#	rr = numpy.sort(action)
##	print rr
#	wee = numpy.array(rr[:-1] & rr[1:])
##	print wee
##	raw_input()
#	return bool(len((numpy.where(wee > 0))[0]))

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


def RS(action,maxe):		#Give him reward ; action ; maxe --> maximum rate
#	if dispute(action):
#		return -100,state
#	print _action
#	print maxe

#	else:
#		ee = []
#		weed = [];
#		for i in range(N):
#			ee.append(convert(action[i]))
#			weed.append(sum(RpC[i][ee[i]])+numpy.random.rayleigh(modevalue))
#		weed = numpy.array(weed)
#		ACKS = len(numpy.where(weed>threshold+numpy.random.rayleigh(modevalue))[0])
		
#		reward = (numpy.average(weed) + ACKS) * max(weed);

	tt = numpy.random.rayleigh(modevalue,M);
	rew = numpy.zeros(M);
	acks = numpy.zeros(N);

	for i in range(M):
#		print action[i]
		rew[i] = RpC[action[i]][i] + tt[i];
		acks[action[i]] += rew[i]
#	acks[action] += 1
	eeww = numpy.where(acks>threshold)
	state = len(eeww[0])		#no of ACKS corresponds to the state


	# = ( performance of channel + Rate per Channel ) * 2  + ( ACKS which is appended at the User to choose him more often) if this is greater than or equal to earlier observed rates on that channel
	#else
	#reward = ( performance of channel + Rate per Channel ) * 1/2 +if lesser
	#performance per channel is got by thresholding ==> ie I am rewarding that channel a little more if it is better than others relatively cause I know that I could choose that channel rather than any other channel

	rew[numpy.where(rew>threshold)] += 1

	up_max = numpy.where(rew>=maxe)
	maxe[up_max] = rew[up_max]
	rew[up_max] *= 2
	ee = numpy.where(rew[up_max] < 0)
	rew[ee] = 1;
	
	up_max_bar = numpy.where(rew < maxe)

	wwf = numpy.where(rew[up_max_bar]*1/2 < rew[up_max_bar])
	rew[up_max_bar][wwf] *= 0.5

	return rew,state,maxe#,eeww	#No of ACKS corresponds to the state


if __name__ == "__main__":
#	master gets only a bunch of ACKS and NACKS
#	actions evolve as 
#	bandsTOuser = numpy.randint(1,M,N)	#randomly allocate 1 --> M bands as the case maybe throughout
#	rewards are given through the environment and so I am the one who gives him the rewards
#DONT READ. THIS COMMENT WILL CONFUSE <==> I realize that irrespective of whatever number of ACKs I get, I am happy if I have maximum rate. This just goes onto say that I need some kind of transmission happening. So, I define 2 states - [[No ACK's and NACK's]] and [[At least 1 ACK]] ===> WRONG CONCLUSION

#	maxe = -10
	_states = M+1
	Q = numpy.random.uniform(0,1,(_states,N,M))
	#I am starting in the ALL NACK state because in the start I don't really know if there is anything happening
	state = 0
	
	#Each state corresponds to the number of ACKS I receive from the USERS

	_action = numpy.random.randint(0,N,M)		#arbit actions

	maxe = numpy.random.uniform(-1,-2,M)		#ie the maximum corresponding to each of the states
	#it makes more sense to give a reward such that each channel is treated differently otherwise we are unnecessarily punishing the good channels
	t = 0

	while 1:
		epsilon = 0.999/1000*(t)
		#alpha *= 0.999
		t+=1;
		if epsilon >= 0.9999:
			epsilon = 0.9999;
			print epsilon
			
		eep = numpy.random.uniform(0,1)

#		dp = dispute(_action)
#		if()
		Reward,state_new,maxe = RS(_action,maxe)
		interm = Q[state];
		if(eep < epsilon):					#then do the greedy action
			_action_ = numpy.array([numpy.argmax(interm[:,i]) for i in range(M)])

		else:
			_action_ = numpy.random.randint(0,N,M);
#			print "random",'\n',t

		for i in range(len(_action)):
				Q[state][_action[i]][i] += alpha*(Reward[i] + gamma*Q[state_new][_action_[i]][i] - Q[state][_action[i]][i])
		state = state_new
		_action = _action_
		print _action#,Reward
#		x_es.append(_action)

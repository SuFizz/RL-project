from __future__ import division
import random
import numpy
import math
from matplotlib.pyplot import *

t = open("testbed1.out",'r');
r = t.readlines()
t.close()

arms = 10

for i in range(len(r)):
	r[i] = r[i].split()
	for g in range(arms):
		r[i][g] = float(r[i][g])

step_rewards = []

rewards = []
rew = []

def train(line,action_selected,No_of_trials,reward_collected,estimated_reward):
	No_of_trials[action_selected] += 1;
	reward_trial = line[action_selected] + random.gauss(0,1);					#with the noise
	reward_collected[action_selected] += reward_trial;							#sum of all the previous rewards;

	estimated_reward[action_selected] = reward_collected[action_selected]/float(No_of_trials[action_selected]);
	return estimated_reward[action_selected],reward_trial,line[action_selected]==max(line);

if __name__ == "__main__":
#		print "TEMPERATURE USED ",temperature,"++++++++++++++++++++++++++++++++++++++++++++++"
	for line in range(2000):
		print line+1,
		step_rewards.append([])
		you = r[line]
		you = numpy.array(you)
		estimated_reward = numpy.zeros(arms)
		No_of_trials = numpy.zeros(arms)
		reward_collected = numpy.zeros(arms)
#		usable = numpy.ones(arms)
#		for armer in range(arms):
#			gen = train(you,armer,No_of_trials,reward_collected,estimated_reward)
		T_horizon = 1000
		delta0 = 1
		timess = int(math.floor(0.5*math.log(T_horizon/math.e)))
		for iters in range(timess):
		###################################THE LOGIC FOR THE ACTION TO BE SELECTED
##################ARM SELECTION
			ennemm = int(math.ceil(2*math.log(T_horizon*delta0**2)/delta0**2))
#			print ennemm,"ee"
			if len(you) > 1:
				for timers in range(ennemm):
					for acction in range(len(you)):
						step_rewards[line].append(train(you,acction,No_of_trials,reward_collected,estimated_reward))
						#print "here"
			else:
#				print "here"
				for timers in range(T_horizon):
					step_rewards[line].append(train(you,0,No_of_trials,reward_collected,estimated_reward))
				break;
#			print No_of_trials
##################ARM SELECTION

##################ARM ELIMINATION
			the_thingy = math.sqrt(math.log(T_horizon*delta0**2)/(2*ennemm))
			maxee = max(estimated_reward - the_thingy)
			indes = numpy.where((estimated_reward+the_thingy) < maxee)
			indices = []
			for free in range(len(indes[0])):
				indices.append(indes[0][free])

#			print indices
#					usable[ireward:] = usable[ireward+1:]						#removing the non usable arms from the game

			you = numpy.delete(you,indices)
			No_of_trials = numpy.delete(No_of_trials,indices)
			reward_collected = numpy.delete(reward_collected,indices)
			estimated_reward = numpy.delete(estimated_reward,indices)
#			print you
##################ARM ELIMINATION

##################delta0 RESET
			delta0 /= 2;
#			print you;
##################delta0 RESET
#		raw_input()

###################################################################################################################
	empr0 = []
	for rr in range(len(step_rewards[0])):
		x = 0;
		noo = 0;
		for gh in range(500):
			try:
				x += step_rewards[gh][rr][0]
				noo += 1
			except:
				continue
		empr0.append(x/noo)
	figure(1)
	plot(empr0,'c')#,color = colo_r)
	title("Estimated Reward Over Time")
	xlabel("Time")
	ylabel("Reward")
	savefig("__Estimated Reward_1000.png")
#	l0.append(str(epsilon))

	empr1 = []
	for rr in range(1000):
		x = 0;
		noo = 0;
		for gh in range(500):
			try:
				x += step_rewards[gh][rr][1]
				noo += 1;
			except:
				continue
		empr1.append(x/noo)
	figure(2)
	plot(empr1,'c')#,color = colo_r)
	title("Reward per trial Over Time")
	xlabel("Time")
	ylabel("Reward")
	savefig("__Reward per trial_1000.png")
#	l1.append(str(epsilon))
	
	
	empr2 = []
	for rr in range(1000):
		x = 0;
		noo = 0;
		for gh in range(500):
			try:
				x += step_rewards[gh][rr][2];
				noo += 1;
			except:
				continue
		empr2.append(x/noo*100);
	figure(3)
	plot(empr2,'c')#,color = colo_r)
	title("Optimality Over Time")
	xlabel("Time")
	ylabel("Percentage Optimal Action")
	savefig("__Percent Optimal_1000.png")
#	l2.append(str(epsilon))

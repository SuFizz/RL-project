from __future__ import division
import random
import numpy
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
		estimated_reward = numpy.zeros(arms)
		No_of_trials = numpy.zeros(arms)
		reward_collected = numpy.zeros(arms)
#		for armer in range(arms):
#			gen = train(you,armer,No_of_trials,reward_collected,estimated_reward)
		for iters in range(1000):
		###################################THE LOGIC FOR THE ACTION TO BE SELECTED
			action_selected = (estimated_reward + numpy.sqrt(2*numpy.log(sum(No_of_trials))/No_of_trials)).argmax()
#			print action_selected;
#			raw_input()
		###################################THE LOGIC FOR THE ACTION TO BE SELECTED
			step_rewards[line].append(train(you,action_selected,No_of_trials,reward_collected,estimated_reward))


	###################################################################################################################
	empr0 = []
	for rr in range(1000):
		x = 0;
		for gh in range(2000):
			x += step_rewards[gh][rr][0]
		empr0.append(x/2000)
	figure(1)
	plot(empr0,'r')#,color = colo_r)
	title("Estimated Reward Over Time")
	xlabel("Time")
	ylabel("Reward")
#	l0.append(str(epsilon))

	empr1 = []
	for rr in range(1000):
		x = 0;
		for gh in range(2000):
			x += step_rewards[gh][rr][1]
		empr1.append(x/2000)
	figure(2)
	plot(empr1,'r')#,color = colo_r)
	title("Reward per trial Over Time")
	xlabel("Time")
	ylabel("Reward")
#	l1.append(str(epsilon))
	
	
	empr2 = []
	for rr in range(1000):
		x = 0;
		for gh in range(2000):
			x += step_rewards[gh][rr][2]
		empr2.append(x/20)
	figure(3)
	plot(empr2,'r')#,color = colo_r)
	title("Optimality Over Time")
	xlabel("Time")
	ylabel("Percentage Optimal Action")
#	l2.append(str(epsilon))

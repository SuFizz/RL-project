from __future__ import division
import random
from matplotlib.pyplot import *

t = open("testbed.out",'r');
r = t.readlines()
t.close()

arms = 1000

for i in range(len(r)):
	r[i] = r[i].split()
	for g in range(arms):
		r[i][g] = float(r[i][g])

step_rewards = []

rewards = []
rew = []

def train(line,action_selected,No_of_trials,reward_collected,estimated_reward):
	No_of_trials[action_selected] += 1;
	random.seed()
	reward_trial = line[action_selected] + random.gauss(0,1);					#with the noise
	reward_collected[action_selected] += reward_trial;							#sum of all the previous rewards;

	estimated_reward[action_selected] = reward_collected[action_selected]/float(No_of_trials[action_selected]);
#	print action_selected,line.index(max(line))
#	print max(line)
#	raw_input()
	return estimated_reward[action_selected],reward_trial,line[action_selected]/max(line);
#for comparing the reward obtained versus the max reward possible.

if __name__ == "__main__":
	for epsilon in ([0.1]):					#vary the epsilon values and plot
		print "EPSILON USED ",epsilon,"++++++++++++++++++++++++++++++++++++++++++++++"
		for line in range(2000):
			print line+1,
			step_rewards.append([])
			you = r[line]
			estimated_reward = [0]*arms
			No_of_trials = [0]*arms
			reward_collected = [0]*arms
			for iters in range(1000):
				if(random.uniform(0,1) <= epsilon):
					action_selected = int(random.uniform(0,arms));
				else:
					action_selected = estimated_reward.index(max(estimated_reward));

				step_rewards[line].append(train(you,action_selected,No_of_trials,reward_collected,estimated_reward))


	###################################################################################################################
		empr0 = []
		for rr in range(1000):
			x = 0;
			for gh in range(2000):
				x += step_rewards[gh][rr][0]
			empr0.append(x/2000)
		figure(1)
		plot(empr0,'k')#,color = colo_r)
	#	title("Estimated Reward Over Time")
	#	xlabel("Time")
	#	ylabel("Reward")
	#	l0.append(str(epsilon))


		empr1 = []
		for rr in range(1000):
			x = 0;
			for gh in range(2000):
				x += step_rewards[gh][rr][1]
			empr1.append(x/2000)
		figure(2)
		plot(empr1,'k')#,color = colo_r)
	#	title("Reward per trial Over Time")
	#	xlabel("Time")
	#	ylabel("Reward")
	#	l1.append(str(epsilon))
	
	
		empr2 = []
		for rr in range(1000):
			x = 0;
			for gh in range(2000):
				x += step_rewards[gh][rr][2]
			empr2.append(x/20)
		figure(3)
		plot(empr2,'k')#,color = colo_r)
	#	title("Optimality Over Time")
	#	xlabel("Time")
	#	ylabel("Reward")
	#	l2.append(str(epsilon))
		
	figure(1)
	title("Estimated Reward Over Time")
	xlabel("Time")
	ylabel("Reward")
	
	figure(2)
	title("Reward per trial Over Time")
	xlabel("Time")
	ylabel("Reward")
	
	figure(3)
	title("Optimality Over Time")
	xlabel("Time")
	ylabel("Reward")
###################################################################################################################

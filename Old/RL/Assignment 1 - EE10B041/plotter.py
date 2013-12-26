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

import gym

env = gym.make('CartPole-v0')

for i_episode in range(20):		# one episode is everytime cartpole falls 
	observation = env.reset()	
	for timestep in range(1000):
		env.render()		# render for every timestep
		print(observation)	# prints array of velocities on where cartpole is
		action = env.action_space.sample()	# ML - random action
		observation, reward, done, info = env.step(action)
		
		# step function completes an action and return four variables
		# observation - what it sees
		# reward - set of velocities
		# done - boolean ; info - diagnostics

		if done:
			print("episode finished")
			break


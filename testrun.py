import gym

env = gym.make('CartPole-v0')	#create the environment
env.reset()
	
for _ in range(100):		#thousand time steps		
	env.render()		#render at each time-step
	env.step(env.action_space.sample())	#taking a random step


 


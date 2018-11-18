import gym
import numpy as np


# HILL CLIMBING - initialize weights randomly, utilize memory to save those weights

def run_episode(env, weights):
	observation = env.reset()
	totalreward = 0
	for _ in range(200):
		env.render()
		action = 0 if np.matmul(weights, observation)<0 else 1	#initializing weights
		observation, reward, done, info = env.step(action)
		totalreward += reward
		if done:
			break
	return totalreward


def train(submit):
	env = gym.make('CartPole-v0')
	
	episodes_per_update = 5
	noise_scaling = 0.1
	weights = np.random.rand(4) * 2 - 1
	bestreward = 0
	for _ in range(100):
		newweight = weights + (np.random.rand(4) * 2 - 1) * noise_scaling
		reward = run_episode(env, newweight)
		print "reward %d best %d" % (reward, bestreward)

		if reward > bestreward:
			bestreward = reward
			weights = newweight
			if reward == 200:
				break

run = train(submit=False)
print run

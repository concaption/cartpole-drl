In this notebook, you will learn the basics of Reinforcemnt Learning using stable baselines library: how to create a RL model, train it and evaluate it. Because all algorithms share the same interface, we will see how simple it is to switch from one algorithm to another.

Stable-Baselines works on environments that follow the gym interface. You can find a list of available environment here.

Stable-Baselines works on environments that follow the [gym interface](https://stable-baselines.readthedocs.io/en/master/guide/custom_env.html).
You can find a list of available environment [here](https://gym.openai.com/envs/#classic_control).

It is also recommended to check the [source code](https://github.com/openai/gym) to learn more about the observation and action space of each env, as gym does not have a proper documentation.
Not all algorithms can work with all action spaces, you can find more in this [recap table](https://stable-baselines.readthedocs.io/en/master/guide/algos.html)

# Environment
For this example, we will use CartPole environment, a classic control problem.

"A pole is attached by an un-actuated joint to a cart, which moves along a frictionless track. The system is controlled by applying a force of +1 or -1 to the cart. The pendulum starts upright, and the goal is to prevent it from falling over. A reward of +1 is provided for every timestep that the pole remains upright. "

## Create the Gym env and instantiate the agent

For this example, we will use CartPole environment, a classic control problem.

"A pole is attached by an un-actuated joint to a cart, which moves along a frictionless track. The system is controlled by applying a force of +1 or -1 to the cart. The pendulum starts upright, and the goal is to prevent it from falling over. A reward of +1 is provided for every timestep that the pole remains upright. "

Cartpole environment: [https://gym.openai.com/envs/CartPole-v1/](https://gym.openai.com/envs/CartPole-v1/)

![Cartpole](https://cdn-images-1.medium.com/max/1143/1*h4WTQNVIsvMXJTCpXm_TAw.gif)

Note: vectorized environments allow to easily multiprocess training. In this example, we are using only one process, hence the DummyVecEnv.

We chose the MlpPolicy because input of CartPole is a feature vector, not images.

The type of action to use (discrete/continuous) will be automatically deduced from the environment action space


we are going train a [Deep Q-Network agent (DQN)](https://stable-baselines.readthedocs.io/en/master/modules/dqn.html).

The essential point of this section is to show you how simple it is to tweak hyperparameters.

The main advantage of stable-baselines is that it provides a common interface to use the algorithms, so the code will be quite similar.


DQN paper: https://arxiv.org/abs/1312.5602

Dueling DQN: https://arxiv.org/abs/1511.06581

Double-Q Learning: https://arxiv.org/abs/1509.06461

Prioritized Experience Replay: https://arxiv.org/abs/1511.05952
# Conclusion

In this notebook we have seen:
- how to define and train a RL model using stable baselines, it takes only one line of code ;)
- how to use different RL algorithms and change some hyperparameters
# write a deep reinforment learning function for the cartpole problem
# !pip install stable-baselines3[extra]
import os
import gym
# from stable_baselines3 import PPO
from stable_baselines3 import DQN
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy

# train a DQN model for the cartpole problem
def train_dqn(env_name, n_timesteps, seed):
    env_name = 'CartPole-v0'
    # Create the environment
    env = gym.make(env_name)
    # train the model
    model = DQN(MlpPolicy, env, verbose=1)
    n_timesteps = 100000
    model.learn(total_timesteps=n_timesteps)
    model.save("cartpole_model")
    

# Create a CartPole environment
def main():
    env = gym.make('CartPole-v0')
    # Create the environment
    env = DummyVecEnv([lambda: env])
    # Load the model
    model = DQN.load("cartpole_model")
    # Evaluate the agent
    mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=10)
    print("Mean reward:", mean_reward, "Std reward:", std_reward)
    # Close the environment
    env.close()
if __name__ == '__main__':
    train_dqn()
    main()
    

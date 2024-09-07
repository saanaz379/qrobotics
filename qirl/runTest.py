# adapted from https://github.com/LauraGentini/QRL/tree/main/1-GroverEnhancement
# modified for qiskit 1.0 and openai gymnasium

import gymnasium as gym

from mazeLearner import MazeLearner

if __name__ == "__main__":
    env_for_test = gym.make("FrozenLake-v1", is_slippery = False, render_mode = "human")
    # env_for_test = gym.make("FrozenLake-v1", is_slippery = False)
    learner = MazeLearner(env_for_test)
    hyperp = {'k': 0.1,
              'alpha': 0.1,
              'gamma': 0.99,
              'eps': 0.01,
              'max_epochs': 3000,
              'max_steps': 15,
              'graphics': True}
    learner.set_hyperparams(hyperp)
    trajectories = learner.train()
    for key in trajectories.keys():
        print(key, trajectories[key])
    print(learner.state_vals.reshape((4, 4)))
    for state, flag in enumerate(learner.grover_steps_flag):
        print(state, '\t', flag)
    for s, circ in enumerate(learner.acts_circs):
        print('action circuit for state ', s)
        print(circ.draw())

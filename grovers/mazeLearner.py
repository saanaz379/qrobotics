# adapted from https://github.com/LauraGentini/QRL/tree/main/1-GroverEnhancement
# modified for qiskit 1.0 and openai gymnasium

import numpy as np

from math import ceil
from qiskit import *
from qiskit.transpiler import generate_preset_pass_manager
from qiskit.circuit.library import GroverOperator
from qiskit.quantum_info import Statevector
from qiskit.providers.basic_provider import BasicSimulator

class MazeLearner:
  def __init__(self, env):
    self.env = env

    # state value space and action value space dimensions
    self.obs_dim = self.env.observation_space.n
    self.acts_dim = self.env.action_space.n

    # dim of qubits for encoding all actions
    self.acts_reg_dim = ceil(np.log2(self.acts_dim))

    # optimal number of steps for grover's
    self.max_grover_steps = int(round(np.pi / (4 * np.arcsin(1. / np.sqrt(2 ** self.acts_reg_dim))) - 0.5))

    # quality vals???
    self.state_vals = np.zeros(self.obs_dim)

    # grovers steps taken???
    self.grover_steps = np.zeros((self.obs_dim, self.acts_dim), dtype = int)

    # boolean flags to signal maximum amplification reached
    self.grover_steps_flag = np.zeros((self.obs_dim, self.acts_dim), dtype = bool)

    # learner parameters
    self.hyperparams = {'k': -1,
                        'alpha': 0.05,
                        'gamma': 0.99,
                        'eps': 0.01,
                        'max_epochs': 1000,
                        'max_steps': 100,
                        'graphics': False}

    # current state (should initialize to 0) irrelevant if initialized at the beginning of each epoch
    self.state = self.env.reset()[0]

    # current action
    self.action = 0

    # list of grover oracles
    self.grover_ops = self._init_grover_ops()

    # list of state-action circuits
    self.acts_circs = self._init_acts_circs()

    # qiskit simulator
    self.SIM = BasicSimulator()

  def _init_grover_ops(self):
    states_binars = [format(i, '0{}b'.format(self.acts_reg_dim)) for i in range(self.acts_dim)]
    targ_states = [Statevector.from_label(s) for s in states_binars]
    grops = [GroverOperator(oracle = ts) for ts in targ_states]
    return [g.to_instruction() for g in grops]

  def _init_acts_circs(self):
    circs = [QuantumCircuit(self.acts_reg_dim, self.acts_reg_dim, name = '|as_{}>'.format(i)) for i in range(self.obs_dim)]
    for c in circs:
      c.h(list(range(self.acts_reg_dim)))
    return circs

  def set_hyperparams(self, hyperdict):
    self.hyperparams = hyperdict

  def train(self):
    traj_dict = {}
    optimal_steps = self.hyperparams['max_steps']

    for epoch in range(self.hyperparams['max_epochs']):

      # print every 10th epoch
      if epoch % 100 == 0:
        print("Processing epoch {} ...".format(epoch))

      # start the epoch by going back to first square and clearing trajectory
      self.state = self.env.reset()[0]
      traj = [self.state]

    #   if self.hyperparams['graphics']: # only for running locally
    #     self.env.render()

      # each epoch consists of a series of steps that lead to the goal square
      for step in range(optimal_steps):
        print('Taking step {0}/{1}'.format(step, optimal_steps), end = '\r')

        # select action TODO 1
        self.action = self._take_action()

        # take action
        new_state, reward, terminated, truncated, info = self.env.step(self.action)

        # adjustments to gymnasium settings
        if new_state == self.state:
          reward -= 10
          terminated = True
        if new_state == self.obs_dim - 1:
          reward += 99
          optimal_steps = step + 1
        elif not terminated:
          reward -= 1

        # probabilities of state value fn + grover mods + run
        self._update_statevals(reward, new_state) # TODO 2
        self.grover_steps[self.state, self.action] = self._eval_grover_steps(reward, new_state) # TODO 3
        self._run_grover_bool() # TODO 4

        # if self.hyperparams['graphics']: # only for running locally
        #   self.env.render()

        traj.append(new_state)
        if terminated:
          break
        self.state = new_state
      traj_dict['epoch_{}'.format(epoch)] = traj
    return traj_dict

  def _take_action(self):
    circ = self.acts_circs[self.state]
    circ_tomeasure = circ.copy()
    circ_tomeasure.measure(list(range(self.acts_reg_dim)), list(range(self.acts_reg_dim)))
    pm = generate_preset_pass_manager(backend=self.SIM, optimization_level=1)
    circ_tomeasure = pm.run(circ_tomeasure)
    result = self.SIM.run(circ_tomeasure, shots=1).result()
    counts = result.get_counts()
    action = int((list(counts.keys()))[0], 2)
    return action

  def _update_statevals(self, reward, new_state):
    self.state_vals[self.state] += self.hyperparams['alpha'] * (reward
                                                                + self.hyperparams['gamma'] * self.state_vals[new_state]
                                                                - self.state_vals[self.state])
    
  def _eval_grover_steps(self, reward, new_state):
    steps_num = int(self.hyperparams['k'] * (reward + self.state_vals[new_state]))
    return min(steps_num, self.max_grover_steps)

  def _run_grover_bool(self):
    flag = self.grover_steps_flag[self.state, :]
    gsteps = self.grover_steps[self.state, self.action]
    circ = self.acts_circs[self.state]
    op = self.grover_ops[self.action]
    if not flag.any():
      for _ in range(gsteps):
        circ.append(op, list(range(self.acts_reg_dim)))
    if gsteps >= self.max_grover_steps and not flag.any():
      self.grover_steps_flag[self.state, self.action] = True
    self.acts_circs[self.state] = circ

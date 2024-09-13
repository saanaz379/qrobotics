# Applying quantum algorithms to robotics tasks offers a more intuitive approach to learning and understanding their design.

**Abstract:**
Robotics is often learners' first introduction to computer science concepts due to its hands-on nature. Quantum robotics is a quickly evolving field which holds similar promise. This poster introduces a novel curriculum for teaching about the core concepts of quantum computing through quantum agent models implemented for managing robots’ decision processes. Specifically, it delves into the use of a variety of quantum algorithms, such as quantum random walks, to be used in tandem with classical reinforcement learning algorithms in order to enable robots to improve their performance on specified design goals. Such an approach allows learners to visually understand the impacts that quantum algorithms can have, a skill directly correlated to higher learner retention rates.

**1. Learning Grover's Algorithm using path planning tasks:** This approach utilizes amplitude amplification to find the best path through a predetermined environment.

The OpenAI Gymnasium library provides benchmarking tools to simulate robot path planning tasks. The FrozenLake environments has 16 states (entries in the grid) and 4 actions (directions the robot can move in). This algorithm achieves consistent accuracy after 3000 epochs of training. The training process for the Grover-inspired path planning algorithm results in 16 trained action circuits, each of which amplify the most likely action to take when on the specified square. The number of repetitions of the amplification operations is determined by the rewards received for each state. Finally, the output of the action circuit directly translates to the provided actions.

**2. Learning Quantum Key Distribution using secure communications tasks:** The BB-84 protocol can be visualized in terms of multiple robots attempting secure communications.

The optical experiments for this study are conducted using VQOL (a JavaScript library for photonics experiments). The lasers in both experiments encode a bit with a value of 0 in the diagonal basis, representing a robot sending an outgoing signal with the value of 0. The first experiment demonstrates how a set of two robots can detect if communications have been intercepted. The laser to the far left represents the robot sending the outgoing signal. The intercepting robot is represented by the polarizing beam splitter in the rectilinear basis and photon detector #3. Because the act of eavesdropping changes the polarization of the bit, the listening robot measures the wrong value of the bit, which can be detected during classical communications between the two intended robots after the signals have been transmitted. The experiment results in successfully transmitting and receiving a bit with a value of 0 only when the following two conditions are met: (1) There are no eavesdroppers present AND (2) The robot sending the signal and the robot receiving the signal have chosen the same basis (in this case, the diagonal basis).

**3. Learning Quantum Random Walks using path planning tasks:** Quantum walks are the key to traversing a network of states and actions in the larger quantum projective simulation algorithm.

The FrozenLake benchmark is used to test the quantum projective simulation algorithm. The agent (robot, in this context) interacts with the environment (frozen lake, in this context) through states and actions. The current state is the input, while the next action is the output of the algorithm. The key to projective simulation lies in the ECM, a network of nodes representing each experience the robot remembers. These nodes can be either states (s1, s2, etc.) or actions (a1, a2, a3, or a4). In order for the agent to choose the correct action according to past experiences from the network, the network is modeled as a transition matrix for a Markov chain and random walks are computed, amplifying the actions of the highest likelihood that are rewarded the most. The matrix contains the probabilities of transitioning from one node to the other in the directed, weighted network called the ECM.

**4. Learning Quantum Positional Verification (QPV) using navigation tasks:** An entanglement-based approach to QPV (proposed by Paul Kwiat, Eric Chitambar, Andrew Conrad, and Samantha Isaac in https://www.ideals.illinois.edu/items/125134) can be used for autonomous robots navigation tasks.

QPV requires two external vehicles (the verifiers) to locate the robot in question. Each verifier chooses a value that satisfies a condition, xy = pi/2. This condition ensures the entanglement phase of QPV can be carried out to its full capacity. Both x and y are sent to the prover via a classical channel. The prover uses an entanglement source to prepare this state using the two values received from both Verifiers. The entanglement source communicates with the two verifiers by sending a pair of photons entangled in this state, both in the same polarization. Each of the verifiers has a polarizing beam splitter and set of photon detectors to perform a Bell test on this information sent from the prover. This procedure must be repeated at least twice in order for the verifiers to measure the signals in two bases (required by the Bell test).

**5. Learning Quantum Neural Networks (QNNs) using trajectory planning tasks:** QNNs are the fully Quantum Reinforcement Learning strategy that are implementable on NISQ devices.

The OpenAI Gymnasium benchmark used to test the QNN is CartPole. The inputs (states) provided are the cart position, cart velocity, pole position, and pole velocity. In order for the algorithm to successfully keep the pole on the cart upright, it can decide to move the cart left or right (as actions). The classical pre-processing step takes the dot product of the 4 inputs in a vector with a vector of 4 trainable parameters. The RX gates encode the modified weights created by the classical pre-processing step, after which the variational ansatz with trainable parameters transforms those values and circularly entangles them to create a level of interaction between the variables. This sequence of gates can be repeated to add layers to the QNN. The probability distribution created by the output of the circuit is then used to calculate the expected reward for each action. The expected rewards can then be used to make the final decision on what action to take. In the context of CartPole, this is simply whether to move left or right.

**Citations and Future Reading:**

Taghvaei, A., Hutchinson, S. A., & Mehta, P. G. (2014). A coupled oscillators-based control architecture for locomotory gaits. 53rd IEEE Conference on Decision and Control, 3487–3492. https://doi.org/10.1109/CDC.2014.7039930

Fazilat, M., Zioui, N., & St-Arnaud, J. (2022). A novel quantum model of forward kinematics based on quaternion/Pauli gate equivalence: Application to a six-jointed industrial robotic arm. Results in Engineering, 14, 100402. https://doi.org/10.1016/j.rineng.2022.100402

Fazilat, M., Zioui, N., & St-Arnaud, J. (2022). A novel quantum model of forward kinematics based on quaternion/Pauli gate equivalence: Application to a six-jointed industrial robotic arm. Results in Engineering, 14, 100402. https://doi.org/10.1016/j.rineng.2022.100402

Leib, D., Seidel, T., Jäger, S., Heese, R., Jones, C., Awasthi, A., Niederle, A., & Bortz, M. (2023). An optimization case study for solving a transport robot scheduling problem on quantum-hybrid and quantum-inspired hardware. Scientific Reports, 13(1), 18743. https://doi.org/10.1038/s41598-023-45668-1

Kwiat, P., Chitambar, E., Conrad, A., & Isaac, S. (2022). Autonomous Vehicle-Based Quantum Communication Network. I-ACT-21-02. https://hdl.handle.net/2142/115964

Abbas, A. H., Abdel-Ghani, H., & Maksymov, I. S. (2024). Classical and Quantum Physical Reservoir Computing for Onboard Artificial Intelligence Systems: A Perspective (arXiv:2407.04717). arXiv. https://doi.org/10.48550/arXiv.2407.04717

Rao, P. U., & Sodhi, B. (2022). Collision-free Path Planning in Multi-vehicle Deployments – A Quantum Approach. 2022 IEEE International Conference on Quantum Computing and Engineering (QCE), 13–21. https://doi.org/10.1109/QCE53715.2022.00019

Kumar, S., Adeniyi, T., Alomari, A., & Ganguly, S. (2023). Design of Quantum Machine Learning Course for a Computer Science Program. 2023 IEEE International Conference on Quantum Computing and Engineering (QCE), 03, 68–77. https://doi.org/10.1109/QCE57702.2023.20326

Wang, J., Ye, Z., Lai, Y., Li, W., & He, J. (2015). Efficiency at maximum power of a quantum heat engine based on two coupled oscillators. Physical Review. E, Statistical, Nonlinear, and Soft Matter Physics, 91(6), 062134. https://doi.org/10.1103/PhysRevE.91.062134

Moioli, R. C., Vargas, P. A., & Husbands, P. (2010). Exploring the Kuramoto model of coupled oscillators in minimally cognitive evolutionary robotics tasks. IEEE Congress on Evolutionary Computation, 1–8. https://doi.org/10.1109/CEC.2010.5586486

Babbush, R., Berry, D. W., Kothari, R., Somma, R. D., & Wiebe, N. (2023). Exponential quantum speedup in simulating coupled classical oscillators*. 2023 IEEE 64th Annual Symposium on Foundations of Computer Science (FOCS), 405–414. https://doi.org/10.1109/FOCS57990.2023.00030

Kwak, Y., Yun, W. J., Jung, S., Kim, J.-K., & Kim, J. (2021). Introduction to Quantum Reinforcement Learning: Theory and PennyLane-based Implementation. 2021 International Conference on Information and Communication Technology Convergence (ICTC), 416–420. https://doi.org/10.1109/ICTC52510.2021.9620885

LauraGentini. (2024). LauraGentini/QRL [Jupyter Notebook]. https://github.com/LauraGentini/QRL (Original work published 2021)

Yao, J., Huang, Y., Wan, Z., Zhang, L., Sun, C., & Zhang, X. (2017). Minimum-time trajectory planning for an inchworm-like climbing robot based on quantum-behaved particle swarm optimization. Proceedings of the Institution of Mechanical Engineers, Part C: Journal of Mechanical Engineering Science, 231(18), 3443–3454. https://doi.org/10.1177/0954406216646138

Mannone, M., Seidita, V., & Chella, A. (2023). Modeling and designing a robotic swarm: A quantum computing approach. Swarm and Evolutionary Computation, 79, 101297. https://doi.org/10.1016/j.swevo.2023.101297

von Stryk, O. (1993). Numerical Solution of Optimal Control Problems by Direct Collocation. In R. Bulirsch, A. Miele, J. Stoer, & K. Well (Eds.), Optimal Control: Calculus of Variations, Optimal Control Theory and Numerical Methods (pp. 129–143). Birkhäuser. https://doi.org/10.1007/978-3-0348-7539-4_10

Dutta, S., Parihar, A., Khanna, A., Gomez, J., Chakraborty, W., Jerry, M., Grisafe, B., Raychowdhury, A., & Datta, S. (2019). Programmable coupled oscillators for synchronized locomotion. Nature Communications, 10(1), 3299. https://doi.org/10.1038/s41467-019-11198-6

Hohenfeld, H., Heimann, D., Wiebe, F., & Kirchner, F. (2024). Quantum Deep Reinforcement Learning for Robot Navigation Tasks. IEEE Access, 12, 87217–87236. IEEE Access. https://doi.org/10.1109/ACCESS.2024.3417808

Komarova, K., Gattuso, H., Levine, R. D., & Remacle, F. (2020). Quantum Device Emulates the Dynamics of Two Coupled Oscillators. The Journal of Physical Chemistry Letters, 11(17), 6990–6995. https://doi.org/10.1021/acs.jpclett.0c01880

Chella, A., Gaglio, S., Mannone, M., Pilato, G., Seidita, V., Vella, F., & Zammuto, S. (2023). Quantum planning for swarm robotics. Robotics and Autonomous Systems, 161, 104362. https://doi.org/10.1016/j.robot.2023.104362

Dong, D., Chen, C., Zhang, C., & Chen, Z. (2006). Quantum robot: Structure, algorithms and applications. Robotica, 24(4), 513–521. https://doi.org/10.1017/S0263574705002596

Gonçalves, C. P. dos S. (2018). Quantum Robotics, Neural Networks and the Quantum Force Interpretation (SSRN Scholarly Paper 3244327). https://doi.org/10.2139/ssrn.3244327

Benioff, P. (1998). Quantum robots and environments. Physical Review A, 58(2), 893–904. https://doi.org/10.1103/PhysRevA.58.893

Mahanti, S., Das, S., Behera, B. K., & Panigrahi, P. K. (2019). Quantum robots can fly; play games: An IBM quantum experience. Quantum Information Processing, 18(7), 219. https://doi.org/10.1007/s11128-019-2332-4

Raghuvanshi, A., Fan, Y., Woyke, M., & Perkowski, M. (2007). Quantum Robots for Teenagers. 37th International Symposium on Multiple-Valued Logic (ISMVL’07), 18–18. https://doi.org/10.1109/ISMVL.2007.46

Dunjko, V., Friis, N., & Briegel, H. J. (2015). Quantum-enhanced deliberation of learning agents using trapped ions. New Journal of Physics, 17(2), 023006. https://doi.org/10.1088/1367-2630/17/2/023006

Benioff, P. (1998). Some foundational aspects of quantum computers and quantum robots. Superlattices and Microstructures, 23(3), 407–417. https://doi.org/10.1006/spmi.1997.0519

Sriarunothai, T., Wölk, S., Giri, G. S., Friis, N., Dunjko, V., Briegel, H. J., & Wunderlich, C. (2018). Speeding-up the decision making of a learning agent using an ion trap quantum processor. Quantum Science and Technology, 4(1), 015014. https://doi.org/10.1088/2058-9565/aaef5e

La Cour, B. R., Maynard, M., Shroff, P., Ko, G., & Ellis, E. (2022). The Virtual Quantum Optics Laboratory. 2022 IEEE International Conference on Quantum Computing and Engineering (QCE), 677–687. https://doi.org/10.1109/QCE53715.2022.00091

Flamini, F., Krumm, M., Fiderer, L. J., Müller, T., & Briegel, H. J. (2024). Towards interpretable quantum machine learning via single-photon quantum walks. Quantum Science and Technology, 9(4), 045011. https://doi.org/10.1088/2058-9565/ad5907
Miller, B., Sawhney, R., Crane, K., & Gkioulekas, I. (2024). Walkin’ Robin: Walk on Stars with Robin Boundary Conditions. ACM Trans. Graph., 43(4), 41:1-41:18. https://doi.org/10.1145/3658153

Useful links:
https://gist.github.com/kyunghoj/f5cbb382a664645ab0bb

Prepare summary of:
    Motivation
    Problem Statement
    Literature Review
    Approach
    Progress so far


Prepare schedule for:
    Proposal
    Qualification Exam
    Defense

## Motivation
- UAS in Military and migration to higher levels of autonomy
- Three horizons -> leveling up autonomy
- Field experts believe that various missions will become operationized with various levels of autuonomy for UAS platforms: EW being one of them
- From acquisition and academics strong confidence will be Human out of the Loop Operation or Fully autonomous
- Aircraft Combat Surviveabiltiy (ACS)
- Challenges in Planning for UAS
  - Computation time not shared and is done offline more than not
  - Demand for UAS to be able to intelligently plan routes from SOTA comprehensive review for beyond Visual Line of Sight Operations
  - Need to consider obstacles,terrain,threats, and thereat detections
- Optimal  of autonomous UAS
  - Nonlinear models typically linearized, accurate only to a certain degree
- Prediction of threats
  - For military applications typically modelled as Gaussian
  - Radar systems
  - Sentry dynamic UAS  
  - Intelligent swarm systems?  


# Problem Statements
- Dynamic Approach Vector Global Planning: Design a system enabling unmanned aerial systems (UAS) to generate optimal approach vectors in real-time, emphasizing adaptability in uncertain environments​
  - Utilize GPU to improve parallelization speed 
  - Utilize MDP to generate optimal route based on effector based on probabilities of various threats 
    - Utilize kill chain? 
  - Paralleize based approach vector for target to speed up search iteration with GPU as well 
  - **Why would I do this?**
    - General route planners utilize deterministic environments 
    - Result times are slow if optimal or using stochastic environments 

- Autonomous Decision Making in Adversarial Contexts with LLMS : Utilize LLMs to develop a decision-making framework for UAS to intelligently select optimal routes, considering diverse circumstances and adversarial threats to enhance mission safety and success. ​
  - Need to check this out with SLMs and how this pipeline works 
  - Idea is for SLM to have input of what is going on with environment
  - Based on that send commands to the MPC on what to do or utilize motion primitives derived from MPC with dictionary
  - 

- Model Predictive Control with Threat Mitigation and Asset Maximization: Create a real-time system for UAS to continuously optimize trajectories, effectively avoiding both deterministic and nondeterministic threats, ensuring mission success in dynamic environments with the given asset.
  - Check out stochastic MPC or MPC based on markov decision process from global planner? 
  - 
# Outline
**Find the gaps in the research**


# Tips
- Look at previous disserations that are similiar to my research **Guidance and Navigation of Fixed Wing UAS in Adversial Environments**


# Gaps
## Trajectory Planning
- A lot of this trajectory planning stuff doesn't consider dynamic manuevering obstacles/threats 
- What do you do then?? Kinetic weapons avoidance but not coupled with radar 
- Playing the role of the evader, how can I avoid mobile threats/aircraft 
- Using GPU's for faster compute of trajectories 
  - Can I do something like this for target tracking?
- If I needed to switch roles how would I build an algorithm that can let me hunt down a grounded vehicle 
- What disturbances do I need to deal with on my system? 
  - I fail something on my wing?
  - I get tracked by my system
- Weapons tracking or targeting:
  - Optimize time on target 
  - Optimize damage done 
- Using GPU to increase performance 

## Weapons trajectory considerations
- 

## Things I can use
- Kill chain costing? 
- Probability of detection
- Probability of kill 

## Redundant future works 
- Fu

# Literature Review Topics

- Path Planning/Trajectory Planning Adversial Environments
  - Obstacle avoidance  
  - Radar Avoidance 
  - Dynamic adversary considerations 
- 
- Optimal Trajectory Control 
- Model Predictive Control - Fixed Wing applications
- Fixed Wing Dynamics and Modeling  
- Data Driven Model Predictive Control  

# Gaussian Process MPC
https://www.youtube.com/watch?app=desktop&v=FHlsbFqWS5g&ab_channel=LearningSystemsandRoboticsLab
- Consider the system dynamics:
  - $x_{t+1} = f(x_t, u_t) + g(x_t,u_t) + \epsilon_t$
  - Designs a controller for systems with prior uncertainty that learns online and continously improves performance while satisfying safety constraints.
- Pros:
  - Nonparametric model 
  - Improved performance with more data 
- Compare Robust and Adaptive Control mechanisms 
- Approach
  - Use nonparametric model for unknown model error (Gaussian Process confidence intervals)
  - Algorithm to safely acquire data and optimize task - robust control 
  - Defining and analyzing closed-loop safety - Lyapunov analysis/ Learned Models

- ## Nonparametric Model with MPC
- 
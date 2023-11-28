# Outline
**Find the gaps in the research**


# Tips
- Look at previous disserations that are similiar to my research **Guidance and Navigation of Fixed Wing UAS in Adversial Environments**


# Gaps
- A lot of this trajectory planning stuff doesn't consider dynamic manuevering obstacles/threats 
- What do you do then?? Kinetic weapons avoidance but not coupled with radar 
- Playing the role of the evader, how can I avoid mobile threats/aircraft 
- If I needed to switch roles how would I build an algorithm that can let me hunt down a grounded vehicle 
- What disturbances do I need to deal with on my system? 
  - Wind 
  - I fail something on my  wing?
  - I get tracked by my system 

# Literature Review Topics
- Model Predictive Control 
- Path Planning Adversial Environments
  - Obstacle avoidance  
  - Radar Avoidance 
- Fixed Wing Dynamics and Modeling 
- Model Predictive Control 
- Gaussian Process Model Predictive Control  

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
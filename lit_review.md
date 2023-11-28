# Outline
**Find the gaps in the research**


# Tips
- Look at previous disserations that are similiar to my research **Guidance and Navigation of Fixed Wing UAS in Adversial Environments**
- 

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
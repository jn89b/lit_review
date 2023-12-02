# An Optimal Engagement Zone Avoidance Scenario in 2-D
Isaac E. Weintraub∗, Alexander Von Moll†, Christian Carrizales‡, Nicholas Hanlon§, and Zachariah Fuchs¶

## What 
- Trajectory optimization in engagement zone areas 
- Vehicle must reach some destination and minimize time to get there while traversing through EZ area

## Literature Review
- Meh 


## How
- Problem formulation for getting to location through:
  - Simple cost function
  - Constraint handling
  - If else penalty function
  - Be at exact time location

## Results
- Trajectories were influenced differently by how formulation was conducted and also the tuning parameter for the radar system 

## Interesting things 
- Derived cost function from your classical lagrangian and hamiltonian multipliers 
- Did proof of it? Not sure I need to but we'll see using the hamiltonian
- Modeled threats as cardiod-shaped threats, becomes polar equations 

## Drawbacks
- The effectiveness of the proposed strategies heavily relies on assumptions made about the system, such as constant strictly-positive speed, specific constraints, and the dynamic nature of the engagement zone. These assumptions may not hold in all real-world scenarios.
- The practical application of the proposed optimal control strategies in real-world situations, especially in dynamic and unpredictable environments, is not thoroughly discussed. The text could benefit from addressing the challenges of implementing these strategies in practical scenarios.
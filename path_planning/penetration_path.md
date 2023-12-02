# A Novel Real-Time Penetration Path Planning Algorithm for Stealth UAV in 3D Complex Dynamic Environment - Planning and Trajectory with Threats

ZHE ZHANG 1, JIAN WU 1,2, JIYANG DAI 1, AND CHENG HE 1

## Literature Review
- Active route planning methods to reduce RCS 
  - Reduce pitch angle [10]
  - Optimal trajectory problem
  - Used simple ellipsoid models

## What 
- Used 3DOF kinematic model for aircraft to move through netted radar system 
- Used ellipsoid model and simple probability of detection model for radar system
- Coupled SA* coupled MPC for search space
- Handled pop up threats or unknown radar configurations

## How
- Given configuration space with n radars
- Plan route from start to end
- Minimize RCS detection for aircraft given kinematic constraints

## Results
- Under 50 percent detection 
- Simulated three different scenarios

## Drawbacks/Limitations
- Radar models are **too simplified** 
- Terrain not considered in simulation
- Used a 3DOF model for x,y, yaw
- Pop up threats and replanning are questionable, its replanning at the start not during traversal
- No active/adversial threats when modeling
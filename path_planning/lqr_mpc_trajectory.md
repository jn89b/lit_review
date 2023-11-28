# Comparative Study of Optimal Multivariable LQR and MPC Controllers for Unmanned Combat Air Systems in Trajectory Tracking - Trajectory 

Alvaro Ortiz 1 , Sergio Garcia-Nieto 2,* and Raul Simarro 2

## Literature Review It Did 
- Path planning 
  - Djikstra's 
  - A*
  - Adaptive cell decomposition 
- Guidance Navigation Controls 
  - Control 
    - PID systems -> how to deal with SISO systems 
    - MPC 
  - Guidance
    - Proportional Navigation -> 
    - Predictive Controls using MPC 

## What 
- Did a comparative analysis between LQR and linear MPC for mission trajectory-planning for military applications (payload dropoff ) with fixed wing aircraft

## How
- The F-86 Sabre was tasked with a mission to reach a final destination q f from an initial point qi at a certain velocity and precision so as to accomplish a successful blitz on the objective. The weapons chosen for this purpose were two M117 demolition bombs. Furthermore, several obstacles had to be avoided during the mission.
- Global planner -> ACD (Adaptive Cell Decomposition)
  - OctTree
  - Obstacles were static, no dynamic obstacles 
  - Used DTED information 
  - Radar:
    - Similarly to the danger area, the radar area approximated the scope of an enemy radar. It was defined as a cylinder, with its bottom altitude determined by the minimum altitude at which the UAV could be detected
- **Trajectory Smoothing**
  - Used load factor consideration to smooth the path between waypoints
  - Check this out
- Guidance Law, used L1 controller/ProNav similiar to track the waypoints 
- MPC and LQR for low level controls 
  - This is using linearized model with aircraft at some trim reference point 
- Aircraft payload dropped off was modeled with wind 
- Results were conducted with payload dropoff to the simulation frame work 

## Results
- Good in linear land obviously 

## Drawbacks/Limitations
- Run time wasn't discussed/ probably bad 
- No Dynamic adversaries or pop up considerations  
- Lack of RCS consideration and fidelity of radars 

# Real-time trajectory planning for UCAV air-to-surface attack using inverse dynamics optimization method and receding horizon control

- This is releasing a payload

# Overview

## Literature Review

The literature review explores existing research and methodologies related to trajectory planning for Unmanned Combat Aerial Vehicles (UCAVs), identifying gaps in knowledge and motivating the proposed approach.

## What Did They Do?

### Parameterization and Inverse Dynamics Optimization

1. **Trajectory Parameterization:**
   - Functions dependent on time and virtual speed define the UCAV trajectory.

2. **Inverse Dynamics Equations:**
   - Controls and remaining states (γ and ψ) are determined using inverse dynamics equations.

3. **Numerical Evaluation:**
   - Path constraints and objectives are numerically evaluated over nodes along a virtual arc.
   - Virtual speed at each node is calculated based on coordinates and airspeed.

4. **Conversion to NLP Problem:**
   - The continuous optimization problem is discretized at nodes, transforming it into an NLP problem.

### Real-Time Trajectory Planning Framework

1. **Integration with Low-Level Control System:**
   - Real-time trajectory planning is integrated with the UCAV's low-level control system.

2. **2-DOF RHC Architecture:**
   - A 2-DOF Receding Horizon Control (RHC) architecture with two feedback control loops.

3. **Receding Horizon Planning Strategy:**
   - Real-time feedback compensates for environmental uncertainty.

4. **Algorithm Execution:**
   - The real-time trajectory planning algorithm iteratively executes until the UCAV enters the guided bomb’s Launch Acceptability Region (LAR).

## How Did They Do It?

### Solving the NLP Problem

1. **Two-Stage Iterative Optimization:**
   - Derivative-free algorithms for initial guess.
   - Sparse nonlinear optimizer (SNOPT) for NLP problem.

2. **Transformation of Constraints:**
   - Constraints transformed into a penalty function for derivative-free optimization.
   - Weight coefficients chosen to balance importance.

## Results

### Simulations

1. **Scenario 1: Single Stationary Target and Stationary Obstacles:**
   - UCAV navigates static obstacles, reaches the target, and delivers the guided bomb.
   - Trajectory planning iterations mostly converge within 2 seconds.

2. **Scenario 2: Single Moving Target and Moving Obstacles:**
   - UCAV navigates a dynamic environment.
   - Comparison between trajectories with and without obstacle/target position prediction.

3. **Scenario 3: Multiple Attacks Against Same/Different Targets:**
   - UCAV plans trajectories for attacking different targets in sequence.
   - Scenario where the UCAV attacks the same target twice with a trajectory adjustment.

4. **Scenario 4: Wind Disturbance:**
   - UCAV adapts to wind disturbance, maintains feasibility, and meets weapon delivery conditions.

### Comparison with GPM

1. **Gauss Pseudospectral Method (GPM):**
   - The proposed method is compared with GPM, a state-of-the-art optimal trajectory generation method.
   - Comparison includes total flight time, planning time, convergence rate, and number of optimization variables.

2. **Comparison Results:**
   - The proposed Inverse Dynamics Optimization method provides comparable results to GPM.
   - It exhibits superior convergence and robustness properties and significantly faster computation times.

## Conclusion

The proposed trajectory planning algorithm demonstrates effectiveness in navigating UCAVs through complex scenarios. It provides real-time adaptability, robustness, and feasibility even in dynamic environments and in the presence of external disturbances. The comparison with GPM highlights its computational efficiency while maintaining competitive performance.


## Interesting notes 


## Drawbacks
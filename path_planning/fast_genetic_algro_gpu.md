# Fast Genetic Algorithm Path Planner for Fixed-Wing Military UAV Using GPU
- VINCENT ROBERGE MOHAMMED TARBOUCHI GILLES LABONT

### What did they do?

The authors developed a Genetic Algorithm (GA) for path planning in the context of Unmanned Aerial Vehicles (UAVs). The algorithm aims to find optimal trajectories for UAVs, considering various constraints and objectives. The GA follows a standard structure with initialization, evaluation, selection, crossover, mutation, and replacement steps.

### How did they do it?

1. **Algorithm Overview:**
   - Candidate solutions (trajectories) are randomly initialized within the search space.
   - The termination criterion is based on a fixed number of iterations.

2. **Fitness Function:**
   - A crucial component for evaluating solution quality.
   - Infeasible solutions have fitness in the range (0, 1), while feasible solutions have fitness in the range (1, 2).

3. **Genetic Algorithm Details:**
   - Selection, crossover, and mutation operators are employed.
   - Different crossover operations are implemented for diversification.
   - Elitism is used for solution replacement.

4. **Mitigating Initial Condition Sensitivity:**
   - Large populations and separate populations evolving in isolation are used.
   - Parallel implementation on a GPU enhances efficiency without increasing computation time.

5. **Parallel Implementation:**
   - Three common parallel primitives for GPUs (parallel map, parallel reduction, parallel scan) are utilized.
   - The GA is implemented using gpuMF, a software framework parallelizing the entire metaheuristic on the GPU.

6. **Parallelization of Fitness Function:**
   - Different parallelization approaches are discussed for path smoothing, terrain collision checking, ascent/descent rate verification, fuel consumption, and average altitude calculation.
   - The second parallelization approach often yields better performance due to higher parallelism.

7. **Numerical Simulation and Results:**
   - Tested on various terrains and scenarios.
   - Trajectories are generated for 18 scenarios on six different terrains.
   - GP


## Interesting Notes
- This algorithm is very very fast, can we encode SAS to do GPU calculations? Don't see that out there but I see research on using it with regular A*


## Drawbacks
- They choose the number of waypoints to reach the goal, which is kind of stupid, so that the UAV can fly smoothly. They say it would make sense to use a higher level planner then use this to get the trajectory. 
- The algorithm assumes a detection distance for obstacles, impacting the UAV's ability to respond promptly to newly detected threats.Depending on the use case, this assumption might limit the algorithm's responsiveness to dynamic environments. In other words its very low resolution of the data, RCS isn't really factored into here 
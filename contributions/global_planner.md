# Baseline Knowledge
- 


## Pipeline
- From target location ray trace around around increments to generate grid mapping
- Cache and vectorize obstacles:
  - Dynamic obstacles store as a respulsive function that is represented on how these obstacles move
  - Static obstacles just inflate based on type of consideration 
- Utilize GPU to run parallel priority queues https://yichaozhou.com/publication/1501massive/slides.pdf
- Utilize APFs to tune the heuristics for Astar based on direction of dybnamic threats 
- https://iopscience.iop.org/article/10.1088/1742-6596/2649/1/012026/pdf
- https://medium.com/@geminae.stellae/introduction-to-gpu-programming-with-python-cuda-577bfdaa47f3

<!-- ## Markov Decision Processes 
- I have a state 
- I have an action
- When I take an action there is a certain probability distrubtion that will happen based on the action I take 
- **MDP the probability only matters based on the current state I take**
  - So you can set it up as a chain of Markovs to have it based on a previous action that you make
- This becomes a stochastic shortest path problem
- How do we solve this?
  -  Can generate a policy/look up table:
     -  When you are at this state, take this action
     -  Typical cost function is to minimize expected cost to goal (expected cost is average cost typically)
     -  Solve this with the **Bellman equation**, pick the best action based on the policy
     -  Can't really use Astar or Djikstra's to solve these problems since its deterministic based, there is no probability
     -  But there are MDP algorithms, that utilize heuristics like Astar
        -  The cost computation is typically recursive
 -->

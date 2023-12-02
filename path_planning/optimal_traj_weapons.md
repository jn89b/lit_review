# Optimal path planning with modified A-Star algorithm for stealth unmanned aerial vehicles in 3D network radar environment 

Zhe Zhang1, Jian Wu1,2, Jiyang Dai1 and Cheng He1

## What Did They Do:

- **Objective:**
  - Develop a penetration path planning algorithm for stealth UAVs considering complex network radar environments.

- **Challenges Addressed:**
  - Combat environment complexity.
  - Maneuverability and attitude constraints.
  - Path planning algorithm efficiency.
  - Optimization and path safety.

- **Contributions of the Modified A-Star Algorithm:**
  - Introduced a 3D sector search approach for expanded track points.
  - Modified heuristic function for accurate path cost estimation.
  - Integrated dynamic RCS characteristics and attitude angle considerations.
  - Considered network radar detection systems for threat evaluation.

- **Simulation Scenarios:**
  - Evaluated in different threat scenarios with varying numbers of threat sources.

## Literature Review:

- **Background:**
  - Stealth technology application in modern high-tech warfare equipment.
  - Challenges in penetration path planning for stealth UAVs.
  - Previous studies on aircraft penetration path planning, optimization, and threat considerations.

- **Prior Approaches:**
  - Studies by Moore, Inanc, Liu, and Ruz on UAV path planning under RCS variations.
  - Discussion of heuristic adaptive pseudospectral approach and trajectory optimization.
  - Limitations of existing algorithms and their focus on offline planning, online planning, or optimal approaches.

## How Did They Do It:

- **Algorithm Components:**
  - Kinematic model and dynamic RCS characteristics of stealth UAVs.
  - Network radar detection system with emphasis on threat probability.
  - Improvements made to the A-Star algorithm for enhanced search efficiency.
  - Attitude angle constraints during flight considered.
  - Radar detection probability calculations using a rank-K fusion criterion.

- **Simulation Methodology:**
  - Tested in MATLAB 2020Ra with a Windows 10 system.
  - Utilized the rank-K fusion criterion for radar detection probability.
  - RCS of stealth UAV presented in a numerical simulation.

## What Are the Results:

- **Simulation Results:**
  - Modified A-Star algorithm outperforms bidirectional multilayer A-Star and conventional A-Star algorithms.
  - Successfully plans optimal penetration paths with higher security and efficiency.
  - Demonstrates effectiveness in complex network radar environments.
  - Specific flight sensor data and efficiency metrics provided for each scenario.

- **Conclusion:**
  - The modified A-Star algorithm proves effective in addressing the challenges of penetration path planning for stealth UAVs in realistic threat scenarios.


## Drawbacks
- Dynamic environments: Consider the adaptability of the algorithm to dynamic environments. If the simulation assumes a relatively static threat scenario, it may be essential to discuss how the algorithm handles changes in the environment during the UAV's flight.
- Sensor and Measurement Uncertainty:
    Address uncertainties associated with sensor measurements and radar detection probabilities. Real-world conditions often involve uncertainty, and accounting for these uncertainties is crucial for the practical application of the algorithm.
- Consideration of Electronic Warfare Tactics:
    If applicable, discuss whether the simulation includes electronic warfare tactics related to manipulating or exploiting the noise floor. Electronic countermeasures can play a significant role in stealth and evasion, and their absence might limit the simulation's realism.
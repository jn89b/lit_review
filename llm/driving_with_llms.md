# Driving with LLMs: Fusing Object-Level Vector Modality for Explainable Autonomous Driving


## Data Collection 
Check out https://medium.com/@ksakmann/behavioral-cloning-make-a-car-drive-like-yourself-dc6021152713
- Vector Behavior Cloning
- Refer to paper: 
- Obtaining data
  - Used a custom 2D to train RL agent to solve driving scenarios 
  - Ground object vector into LLMS, used a language generator that translates numerical data into textual descriptions for representation pretraining(tokens)
  - Used GPT to generate question-answering dataset conditioned of 10k different driving scenarios 
- 
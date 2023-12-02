# Massively Parallel A* Search on a GPU
Yichao Zhou and Jianyang Zeng∗

## What did they do?

The authors proposed a GPU-based parallel A* search algorithm for solving problems in diverse domains, including sliding puzzles, pathfinding, and protein design. They addressed challenges in adapting A* search to GPU architecture, particularly focusing on efficient node duplication detection.

## How did they do it?

1. **Node Duplication Detection:**
   - Proposed two mechanisms for node duplication detection on GPU: parallel cuckoo hashing and parallel hashing with replacement.
   - Parallel cuckoo hashing used multiple hash tables and functions to handle collisions, allowing parallel insertion.
   - Parallel hashing with replacement dropped old nodes instead of pushing them to different positions, making it simpler and faster.

2. **Parallel A* Implementation:**
   - Utilized GPU architecture by assigning one cuckoo hashing instance to each GPU block, ensuring efficient synchronization.
   - Developed theoretical analyses of failure rates for parallel cuckoo hashing and demonstrated that the probability of hash table rebuilding is low.

3. **Experimental Evaluation:**
   - Conducted experiments comparing GPU-based A* (GA*) with traditional CPU-based sequential A* on sliding puzzles, pathfinding, and protein design problems.
   - Varied the number of parallel priority queues in GA* to leverage GPU parallelism fully.
   - Provided theoretical results, including guarantees on finding optimal solutions and bounds on the number of expanded nodes.

## Results?

1. **Sliding Puzzles:**
   - Achieved a near 30x speedup with GA* compared to sequential A* for 15-puzzles and 24-puzzles, demonstrating efficiency in handling exponential search space.

2. **Pathfinding:**
   - GA* performance varied based on graph characteristics, outperforming sequential A* by about 7 times in some cases.
   - GPU-based A* demonstrated efficiency when heuristic functions deviated from actual distances.

3. **Protein Design:**
   - Attained a near 45x speedup with GA* compared to sequential A* in protein design problems.
   - The GPU effectively accelerated the computation of complex heuristic functions, a bottleneck in this domain.

## Conclusion and Future Work:

The GPU-based parallel A* algorithm showcased significant speedup in solving problems with exponential search space. Future work may explore bidirectional A* search algorithms on GPUs and the potential of employing A* search in a multi-GPU environment.

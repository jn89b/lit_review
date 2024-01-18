from numba import cuda, int32
import numpy as np

# Define the state structure
class State:
    def __init__(self, s, param1, param2, param3):
        self.s = s
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3

# Define the binary heap data structure
class Heap:
    def __init__(self):
        self.data = []

    def insert(self, element):
        self.data.append(element)
        self._heapify_up(len(self.data) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.data[index].param1 < self.data[parent_index].param1:
                self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
                index = parent_index
            else:
                break

@cuda.jit
def init_heap(s, Q, states_pool, nodes_pool, state_len, total_Q_size):
    heap_instance = Q[0]
    new_state = State(s, 0, 0, 0)
    heap_instance.insert(new_state)
    cuda.atomic.add(total_Q_size, 0, 1)

print("starting")
# Example usage
s = "example_string"
Q = [Heap()]  # Q is a list containing a Heap object
states_pool = cuda.device_array(10, dtype=State)  # Example: Allocate space for 10 states on the GPU
nodes_pool = cuda.device_array(100, dtype=np.int8)  # Example: Allocate space for 100 nodes on the GPU
state_len = len(s)
total_Q_size = cuda.device_array(1, dtype=int32)

# # Launch the CUDA kernel
# init_heap[1, 1](s, Q, states_pool, nodes_pool, state_len, total_Q_size)
# print("launching heap")
# # Copy data back from GPU to CPU for verification
# total_Q_size_cpu = total_Q_size.copy_to_host()[0]
# print("Total Q Size:", total_Q_size_cpu)

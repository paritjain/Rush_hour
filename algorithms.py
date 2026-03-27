"""
    1. BFS  – Breadth-First Search        (optimal, complete)
    2. DFS  – Depth-First Search          (not optimal, depth-limited)
    3. UCS  – Uniform-Cost Search         (optimal, complete)
    4. A*   – A-Star Search               (optimal with admissible h)
"""
import heapq
from collections import deque

# Shared helper
def _stats(nodes: int, path_len: int) -> dict:
    return {'nodes_explored': nodes, 'solution_length': path_len}

# 1.  BFS  –  Breadth-First Search
def bfs(initial_state):
  
    if initial_state.is_goal():
        return [], _stats(0, 0)

    queue   = deque([(initial_state, [])])
    visited = {initial_state.encode()}
    nodes   = 0

    while queue:
        state, path = queue.popleft()
        nodes += 1

        for action, next_state in state.get_successors():
            enc = next_state.encode()
            if enc in visited:
                continue
            visited.add(enc)

            new_path = path + [(action, next_state)]

            if next_state.is_goal():
                return new_path, _stats(nodes, len(new_path))

            queue.append((next_state, new_path))

    return None, _stats(nodes, 0)

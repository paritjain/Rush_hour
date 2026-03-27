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

# 2.  DFS  –  Depth-First Search (depth-limited)
def dfs(initial_state, max_depth: int = 50):
    if initial_state.is_goal():
        return [], _stats(0, 0)
    stack   = [(initial_state, [])]
    visited = {initial_state.encode()}
    nodes   = 0

    while stack:
        state, path = stack.pop()
        nodes += 1

        # Depth limit 
        if len(path) >= max_depth:
            continue

        for action, next_state in state.get_successors():
            enc = next_state.encode()
            if enc in visited:
                continue
            visited.add(enc)

            new_path = path + [(action, next_state)]

            if next_state.is_goal():
                return new_path, _stats(nodes, len(new_path))

            stack.append((next_state, new_path))

    return None, _stats(nodes, 0)

# 3.  UCS  –  Uniform-Cost Search
def ucs(initial_state):
    if initial_state.is_goal():
        return [], _stats(0, 0)

    counter = 0   # tie-breaker for equal-cost nodes
    # Heap entry: (cost, tie_breaker, state, path)
    heap    = [(0, counter, initial_state, [])]
    visited = {}   # encode → best cost seen so far
    nodes   = 0

    while heap:
        cost, _, state, path = heapq.heappop(heap)
        enc = state.encode()

        if enc in visited:
            continue
        visited[enc] = cost
        nodes += 1

        if state.is_goal():
            return path, _stats(nodes, len(path))

        for action, next_state in state.get_successors():
            next_enc = next_state.encode()
            new_cost = cost + 1   # uniform cost = 1 per move
            if next_enc not in visited:
                counter += 1
                new_path = path + [(action, next_state)]
                heapq.heappush(heap,
                               (new_cost, counter, next_state, new_path))

    return None, _stats(nodes, 0)






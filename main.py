import time

from algorithms import bfs, dfs, ucs, astar
from heuristics import h_blocking_cars, h_advanced
from puzzles    import get_puzzle
from visualize  import show_solution

# Algorithm registry
ALGORITHMS = {
    '1': ('BFS',               lambda s: bfs(s)),
    '2': ('DFS  (depth≤50)',   lambda s: dfs(s, max_depth=50)),
    '3': ('UCS',               lambda s: ucs(s)),
    '4': ('A*  h1=BlockingCars',  lambda s: astar(s, h_blocking_cars)),
    '5': ('A*  h2=Advanced',      lambda s: astar(s, h_advanced)),
}
# Comparison mode 
def run_all_algorithms(state):
    """Solve the same puzzle with every algorithm and compare."""
    print('\n' + '=' * 65)
    print(f'  {"Algorithm":<26} {"Nodes":>10} {"Moves":>7} {"Time (s)":>10}')
    print('=' * 65)

    for key in sorted(ALGORITHMS):
        name, algo = ALGORITHMS[key]
        t0          = time.time()
        solution, stats = algo(state)
        elapsed     = time.time() - t0

        moves = stats['solution_length'] if solution else 'None'
        print(f'  {name:<26} {stats["nodes_explored"]:>10} '
              f'{str(moves):>7} {elapsed:>10.4f}')

    print('=' * 65)
    print('\n  Legend')
    print('  Nodes = total states expanded during search')
    print('  Moves = number of car moves in the solution')


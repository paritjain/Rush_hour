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

# Single algorithm mode 
def run_single_algorithm(state):
    """Let the user pick one algorithm, solve, then open the visualizer."""
    print('\nSelect algorithm:')
    for key in sorted(ALGORITHMS):
        name, _ = ALGORITHMS[key]
        print(f'  {key}. {name}')

    choice = input('\nEnter choice (1–5) [default 4]: ').strip() or '4'
    if choice not in ALGORITHMS:
        print('Invalid choice – using A* h1.')
        choice = '4'

    name, algo = ALGORITHMS[choice]
    print(f'\nRunning {name}…')

    t0              = time.time()
    solution, stats = algo(state)
    elapsed         = time.time() - t0

 # Print results
    print(f'\n  Result   : {"SOLVED" if solution else "No solution found"}')
    print(f'  Nodes    : {stats["nodes_explored"]}')
    print(f'  Moves    : {stats["solution_length"]}')
    print(f'  Time     : {elapsed:.4f}s')

    if solution:
        print('\n  Solution path:')
        for i, ((car_id, direction), _) in enumerate(solution, 1):
            print(f'    Step {i:2d}: move car {car_id} {direction}')

    # Open visualizer 
    print('\n  Opening visualizer…')
    print('  (Use arrow keys to step through, SPACE to auto-play, Q to quit)\n')
    show_solution(state, solution, name, stats)

# Main
def main():
    print("="*40)
    print("Rush Hour - AI Solver")
    print("="*40)
# Choose puzzle 
    print('\nSelect puzzle difficulty:')
    print('  1. Easy   (~5 moves)')
    print('  2. Medium (~6 moves)')
    print('  3. Hard   (~8 moves)')
    level = input('\nEnter level (1/2/3) [default 1]: ').strip() or '1'

    try:
        level = int(level)
        if level not in (1, 2, 3):
            raise ValueError
    except ValueError:
        print('Invalid input – defaulting to Easy.')
        level = 1

    state = get_puzzle(level)

    print(f'\nPuzzle (level {level}):')
    state.print_board()
    print('  (X = red car,  > = exit)\n')

# Choose action 
    print('What would you like to do?')
    print('  1. Compare ALL algorithms (table)')
    print('  2. Run one algorithm + open visual')
    action = input('\nEnter choice (1/2) [default 2]: ').strip() or '2'

    if action == '1':
        run_all_algorithms(state)
    else:
        run_single_algorithm(state)


if __name__ == '__main__':
    main()

   





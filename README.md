# Rush_hour
A complete implementation of the **Rush Hour** sliding-block puzzle with four
AI search algorithms and interactive visualisation.


You will be prompted to:
1. Choose a puzzle difficulty (1 = Easy, 2 = Medium, 3 = Hard)
2. Choose an action:
   - **Option 1** – Run *all* algorithms and print a comparison table
   - **Option 2** – Run *one* algorithm and open the visual step-through


## Heuristics

Both heuristics are **admissible** (never over-estimate) → A* stays optimal.

### h1 – Blocking Cars
Count the number of distinct cars standing between the red car and the exit.
Each blocker needs at least one move, so this is a valid lower-bound.

### h2 – Blocking Cars + Stuck Blockers
Start with h1, then add 1 for every blocking car that **cannot immediately
move** (because it too is blocked by another car).  
This is a tighter lower-bound than h1, so A* explores fewer nodes with h2.

## Puzzle Descriptions

### Easy
```
. . . . . .
. . . A . .
X X . A . .  →   Move A up, slide X to exit.
. . . . . .
. . . . . .
. . . . . .
```

### Medium
```
A A . . . .
. . . B . .
X X . B . C  →   B must move, C must move, then X slides through.
. . . . . C
. . D D . .
. . . . . .
```

### Hard
```
. . A . B B
. . A . . .
X X A . . .  →   D must move first to let A slide down, unblocking X.
. . . C C .
. D D . . .
. . . E E .
```

---

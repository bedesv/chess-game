# chess-game

**I've had to put this aside for now as I'm too busy with uni to put any time into it**  

This is a side project where I'm developing a chess playing algorithm.  

In order to focus on just the algorithm development, a Python chess library is used.

# Requirements
    pip install chess



# Design Process
My initial thought was to cache all the best possible moves for each player from each state, as that's guaranteed to have an optimal solution. Unfortunately, this involves about 10^45 different boards, which would be far too big and take too long to compute and search through.

My next thought was some kind of min-max algorithm with pruning.


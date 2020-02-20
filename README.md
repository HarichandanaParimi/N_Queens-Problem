# N_Queens-Problem
 

N Queens is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other, for which solutions exist for all the natural numbers n except for n=2 and n=3.

This problem is solved by three methods of Hill climbing algorithm.
 
# Steepest-Ascent Hill Climbing

It first examines all the neighbouring nodes and then selects the node closest to the solution state as next node.

# Hill climbing with side way moves

To avoid staying stuck in a shoulder plateau, we allow hill-climbing to move to neighbour states that have the same value as the current one.

# Random-restart-hill-climbing

It conducts a series of hill-climbing searches from randomly generated initial states until a goal is found.
     


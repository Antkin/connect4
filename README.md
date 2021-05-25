# connect4
Human vs AI connect 4 games. Uses minimax (no a/b pruning atm) to choose decent moves. Current heuristic looks at 1) game winning moves,
and 2) moves where theres 3 chips in a row and a 4th chip can be added. Only looks at the _xxx_ case for now as opposed
to the x_xx type cases.

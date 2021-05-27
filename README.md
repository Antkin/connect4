# connect4
Human vs AI connect 4 games. Uses minimax (no a/b pruning atm) to choose decent moves. Current heuristic looks at 1) game winning moves,
and 2) moves where theres 3 chips in a row and a 4th chip can be added. The 3 chip in a row heuristic looks at the _xxx, x_xx, xx_x, and xxx_ case. 

This repository is written in python. To play against the AI compile and run the code. In the terminal follow the prompt to select which player (human or AI) plays first. Once the player is selected a pygame window will open and the user can play on by dropping chips on the screen.

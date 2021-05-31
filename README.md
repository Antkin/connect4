# connect4
Human vs AI connect 4 game written in python. 
Current implementation uses minimax with a/b pruning for improved effeciency. 
Current heuristic takes into account several types of game states:
    1) Game winning moves are assigned extremely high heuristic values, and we focus on game states that achieve game winning moves sooner
    2) We check for every type of 3 in a row where a 4th chip can be played. So _xxx, x_xx, xx_x, and xxx_ type moves. These types of moves have a pretty high heuristic value, and we go for
    game states where the number of these types of moves is maximized.
    3) We check for every type of 2 in a row where 2 chips can still be played. These types of moves have a lower heuristic value than the 3 in a rows, but once again we try and 
    go for game states where the number of these types of moves are maximized.
    4) Finally we check for opponent 3 in a row moves where a 4th chip can be played. These moves are assigned a negative heuristic value.

To play the game compile and run the connect4.py file. From there select 0 to randomly select the 1st player, 1 to let a human player go first, and 2 for the AI to go first.
Once you select the player a pygame window will open on which you can play by clicking on the row you want to play.
The game will use a text to speech library to announce the Ai moves, it will also play randomly selected audio clips when the AI blocks the human players connect4 as well as funny music when it wins.
The difficulty can be adjusted by going into the connect4.py file and changing the numerical value on the self.minimax call near the bottom.

Some future upgrades planned are a UI start screen, replay button, back button, and difficulty slider. 
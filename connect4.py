import numpy as np
import sys
import math
import board

class connect4:
    global rows
    global collumns
    global empty
    global humanPlayer
    global aiPlayer
    
    rows = 6
    collumns = 7
    empty = 0
    humanPlayer = 1
    aiPlayer = 2
    
    def create_new_board():
        newBoard = np.zeros((rows, collumns))
        return newBoard
    
    def create_board_copy(inputBoard):
        newBoard = np.copy(inputBoard)
        return newBoard
    
    def possibleMoves(inputBoard):
        
    
    print(create_new_board())
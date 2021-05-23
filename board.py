# -*- coding: utf-8 -*-
"""
Created on Sat May 22 17:08:48 2021

@author: Owner
"""
class board:
    state = []
    turn = 0
    
    def __init__(self, state, turn):
        self.state = state
        self.turn = turn
    
    def possibleMoves(self):
        moves = []
        
        for i in range(0, 7):
            if (self.state[i][0] == 0):
                moves.append(i)
        
        return moves
    
    def winningState(self):
        boardWidth = 7
        boardHeight = 6
        
        #Horizontal Check
        for i in range(boardHeight):
            for j in range(boardWidth - 3):
                if self.state[j][i] == self.turn and self.state[j + 1][i] == self.turn and self.state[j + 2][i] == self.turn and self.state[j + 3][i] == self.turn:
                    return True
                
        #Vertical Check
        for i in range(boardWidth):
            for j in range(boardHeight - 3):
                if self.state[j][i] == self.turn and self.state[j][i + 1] == self.turn and self.state[j][i + 2] == self.turn and self.state[j][i + 3] == self.turn:
                    return True
        
        return False
        # Check forward diagnol aka / type wins
        
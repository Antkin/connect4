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
    
    #Creates empty board
    def create_new_board():
        newBoard = np.zeros((rows, collumns))
        return newBoard
    
    #Creates copy of an existing board
    def create_board_copy(inputBoard):
        newBoard = np.copy(inputBoard)
        return newBoard
    
    #Returns a list of the collumns where you can still play
    def possibleMoves(inputBoard):
        openCollumns = []
        for i in range(collumns):
            if inputBoard[0][i] == 0:
                openCollumns.append(i)
        
        return openCollumns
    
    #Returns true or false if a move can be made in that collumn
    def isValidMove(inputBoard, collumn):
        if collumn < collumns and inputBoard[0][collumn] == 0:
            return True
        else:
            return False
    
    #Places a chip in the indicated collumn, check if the move is valid first
    def makeMove(inputBoard, collumn, playerNum):
        rowPointer = 0
        
        while(rowPointer < rows):
            if(inputBoard[rowPointer][collumn] == 0) and (rowPointer == rows - 1):
                inputBoard[rowPointer][collumn] = playerNum
                break
                
            elif(inputBoard[rowPointer][collumn] != 0):
                inputBoard[rowPointer - 1][collumn] = playerNum
                break
                
            else:
                rowPointer += 1
    
    #Checks if there is a winning combination
    def winningMove(inputBoard, playerNum):
        #Check for horizontal wins
        for collumn in range(collumns - 3):
            for row in range(rows):
                if inputBoard[row][collumn] == playerNum and inputBoard[row][collumn+1] == playerNum and inputBoard[row][collumn+2] == playerNum and inputBoard[row][collumn+3] == playerNum:
                    return True
                
        #Check for vertical wins
        for collumn in range(collumns):
            for row in range(rows - 3):
                if inputBoard[row][collumn] == playerNum and inputBoard[row+1][collumn] == playerNum and inputBoard[row+2][collumn] == playerNum and inputBoard[row+3][collumn] == playerNum:
                    return True
                
        #Check for backward slash type wins
        for collumn in range(collumns-3):
            for row in range(rows-3):
                if inputBoard[row][collumn] == playerNum and inputBoard[row+1][collumn+1] == playerNum and inputBoard[row+2][collumn+2] == playerNum and inputBoard[row+3][collumn+3] == playerNum:
                    return True
        
        #Check for forward slash type wins
        for collumn in range(collumns-3):
            for row in range(3, rows):
                if inputBoard[row][collumn] == playerNum and inputBoard[row-1][collumn+1] == playerNum and inputBoard[row-2][collumn+2] == playerNum and inputBoard[row-3][collumn+3] == playerNum:
                    return True
                
        return False
        
    testHorizontal = create_new_board()
    testVertical = create_new_board()
    testForwardDiagnol = create_new_board()
    testBackwardDiagnol = create_new_board()
    
    #Vertical 
    while(True):
        if(isValidMove(testVertical, 3)):
            makeMove(testVertical, 3, 1)
        else:
            break
     
    print("Vertical Test")
    print(testVertical)
    print(winningMove(testVertical, 1))
    
    #Horizontal
    pointer = 0
    while(True):
        if(isValidMove(testHorizontal, pointer)):
            makeMove(testHorizontal, pointer, 1)
            pointer += 1
        else:
            break
        
    print("Horizontal Test")
    print(testHorizontal)
    print(winningMove(testHorizontal, 1))
        
   
    
    
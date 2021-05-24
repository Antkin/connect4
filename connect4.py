import numpy as np
import random as rand
import math

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
    def create_new_board(self):
        newBoard = np.zeros((rows, collumns))
        return newBoard
    
    #Creates copy of an existing board
    def create_board_copy(self, inputBoard):
        newBoard = np.copy(inputBoard)
        return newBoard
    
    #Returns a list of the collumns where you can still play
    def possibleMoves(self, inputBoard):
        openCollumns = []
        for i in range(collumns):
            if inputBoard[0][i] == 0:
                openCollumns.append(i)
        
        return openCollumns
    
    #Returns true or false if a move can be made in that collumn
    def isValidMove(self, inputBoard, collumn):
        if collumn < collumns and inputBoard[0][collumn] == 0:
            return True
        else:
            return False
    
    #Places a chip in the indicated collumn, check if the move is valid first
    def makeMove(self, inputBoard, collumn, playerNum):
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
    def winningMove(self, inputBoard, playerNum):
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
        
    def minimax(self, state, depth, maximizingPlayer):
        currPlayer = 0
        prevPlayer = 0
        if (maximizingPlayer):
            currPlayer = 2
            prevPlayer = 1
        else:
            currPlayer = 1
            prevPlayer = 2
        
        gameOver = self.winningMove(state, prevPlayer)
        
        if (depth == 0) or gameOver:
            if gameOver:
                #print("EOG Scenario detected for player "+str(prevPlayer))
                #Human win
                if (prevPlayer == 1):
                    return (None, -1)
                #AI win
                elif (prevPlayer == 2):
                    return (None, 1)
                #No win
                else:
                    return (None, 0)
            
            #reached 0 depth
            else:
                return (None, 0)
        
        if (maximizingPlayer):
            value = -100000
            for moves in self.possibleMoves(state):
                newState = self.create_board_copy(state)
                self.makeMove(newState, moves, currPlayer)
                move, newValue = self.minimax(newState, depth - 1, False)
                #print("Move "+str(moves)+" results in value "+str(newValue))
                if newValue > value:
                    value = newValue
                    collumn = moves
            return collumn, value
        
        else:
            value = 100000
            for moves in self.possibleMoves(state):
                newState = self.create_board_copy(state)
                self.makeMove(newState, moves, currPlayer)
                move, newValue = self.minimax(newState, depth - 1, True)
                
                if newValue < value:
                    value = newValue
                    collumn = moves
            return collumn, value
            
        
        
    def play(self):
        playerSelection = True
        
        #currTurn = 1 means its the human player, currTurn = 2 means its the AI player
        currTurn = 0
        while(playerSelection):
            val = input("Press 0 to randomly select the first player, 1 to play human first, 2 to play AI first! \n")
            
            if (val == '0'):
                startingPlayer = rand.randint(1, 2)
                if (startingPlayer == 1):
                    print("Human plays first!")
                    currTurn = 1
                else:
                    print("AI plays first!")
                    currTurn = 2
                
                playerSelection = False
                    
                
         
            elif (val == '1'):
                print("Human plays first!")
                currTurn = 1
                playerSelection = False
            
            elif (val == '2'):
                print("AI plays first!")
                currTurn = 2
                playerSelection = False
        
            else:
                print("Unrecognized input, please enter 0, 1, or 2.")
            
        gameOver = False
        board = self.create_new_board()
        correctTurn = False
        
        print("Initial game state is:")
        print(board)
        print()
        
        while (True):
            #Human Turn
            if (currTurn == 1):
                while(not correctTurn):
                    val = input("Human 1 players turn! Please enter the collumn you would like to drop your chip into, starting from 1 and ending at 7.")
                    #User puts in a num from 1-7, but array indices are 0-6
                    val = int(val) - 1
                    
                    if self.isValidMove(board, val):
                        correctTurn = True
                        self.makeMove(board, val, currTurn)
                        
                        if self.winningMove(board, currTurn):
                            print(board)
                            print("Human winner!!!")
                            return 0
                        
                    else:
                        print("This is not a valid move, please try again!")
            
            #AI Turn
            else:
                collumn, value = self.minimax(board, 4, True)
                if self.isValidMove(board, collumn):
                    print("AI playing on collumn "+str(collumn))
                    self.makeMove(board, collumn, currTurn)
                    
                    if self.winningMove(board, currTurn):
                        print(board)
                        print("AI Winner!")
                        return 0
                    
                else:
                    print("AI ERROR")
                    return 0
                
            if(currTurn == 1):
                currTurn = 2
            else:
                currTurn = 1
                
            correctTurn = False
            
            print("Current game state is")
            print(board)
            print()
                
            

                
game = connect4()
game.play()
   
    
    
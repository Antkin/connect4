import numpy as np
import random as rand
import math
import pygame
import sys
import pyttsx3 as tts
from playsound import playsound
from os import listdir

class connect4:
    global rows
    global collumns, empty, humanPlayer, aiPlayer
    global background, red_chip, yellow_chip, empty_chip
    global squaresize, windowWidth, windowHeight, chipSlotRadius
    
    
    rows = 6
    collumns = 7
    empty = 0
    humanPlayer = 1
    aiPlayer = 2
    
    #Pygame variables
    background = (0, 0 ,0)
    red_chip = (255, 0 , 0)
    yellow_chip = (255, 255, 0)
    empty_chip = (255, 255, 255)
    
    squaresize = 100
    windowWidth = squaresize * collumns
    windowHeight = squaresize * (rows + 1)
    chipSlotRadius = (squaresize // 2) - 5
    
    #draws pygame board
    def draw_board(self, state):
        for collumn in range(collumns):
            for row in range(rows):
                pygame.draw.rect(screen, background, (collumn * squaresize, row * squaresize + squaresize, squaresize, squaresize))
                pygame.draw.circle(screen, empty_chip, (collumn * squaresize + squaresize // 2, row * squaresize + squaresize + squaresize // 2), chipSlotRadius)
        
        for collumn in range(collumns):
            for row in range(rows):
                if state[row][collumn] == 1:
                    pygame.draw.circle(screen, red_chip, (collumn * squaresize + squaresize // 2, windowHeight - (rows - row) * squaresize + squaresize // 2), chipSlotRadius)
                 
                elif state[row][collumn] == 2:
                    pygame.draw.circle(screen, yellow_chip, (collumn * squaresize + squaresize // 2, windowHeight - (rows - row) * squaresize + squaresize // 2), chipSlotRadius)
                  
        pygame.display.update()
    
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
                
    #Looks at the number of chips that need to be placed to reach a certain row in a collumn
    def emptySpace(self, inputBoard, row, collumn):
        count = 0
        pointer = row
        while(pointer < rows - 1):
            if inputBoard[pointer+1][collumn] == 0:
                count += 1
                pointer += 1
            else:
                return count
        
        return count
    
    #Another heuristic function which will check how many "three in a row" cases there are. 
    #Original heuristic only looked at _xxx and xxx_ case. This heuristic will also look at the 
    #x_xx and xx_x case.
    #For now we dont look at 2 in a rows
    def threeInARow(self, inputBoard, playerNum):
        heuristicValue = 0
               
        #In all cases we must ensure that that exactly 3 of the positions are the player number
        #and the fourth is a 0. If another players chips are in the way we cant play in any case
        
        #Check for horizontal 3's
        for collumn in range(collumns - 3):
            for row in range(rows):
                #These values get reset every iteration
                countPlayerNum = 0
                countZero = 0
                zeroPos = []
                
                if inputBoard[row][collumn] == playerNum:
                    countPlayerNum += 1
                elif inputBoard[row][collumn] == 0:
                    countZero += 1
                    zeroPos.extend([row, collumn])
                    
                if inputBoard[row][collumn+1] == playerNum:
                    countPlayerNum += 1
                elif inputBoard[row][collumn+1] == 0:
                    countZero += 1
                    zeroPos.extend([row, collumn+1])
                
                if inputBoard[row][collumn+2] == playerNum:
                    countPlayerNum += 1
                elif inputBoard[row][collumn+2] == 0:
                    countZero += 1
                    zeroPos.extend([row, collumn+2])
                    
                if inputBoard[row][collumn+3] == playerNum:
                    countPlayerNum += 1
                elif inputBoard[row][collumn+3] == 0:
                    countZero += 1
                    zeroPos.extend([row, collumn+3])
                
                #Checking ONLY for cases where we have 3 of our players chips and one empty space
                if countPlayerNum == 3 and countZero == 1:
                    heuristicValue += 6 - self.emptySpace(inputBoard, zeroPos[0], zeroPos[1])
                
                    
       
        #Check for vertical 3's, since these moves are easy to counter I weigh them lower
        #This is an easy check because there is only one scenario
        for collumn in range(collumns):
            for row in range(rows - 3):
                if inputBoard[row][collumn] == 0 and inputBoard[row+1][collumn] == playerNum and inputBoard[row+2][collumn] == playerNum and inputBoard[row+3][collumn] == playerNum:
                    heuristicValue += 4
                
        #Check for backward slash type 3's
        for collumn in range(collumns-3):
            for row in range(rows-3):
                countPlayerNum = 0
                countZero = 0
                zeroPos = []
                
                if inputBoard[row][collumn] == playerNum:
                    countPlayerNum += 1
                elif inputBoard[row][collumn] == 0:
                    countZero += 1
                    zeroPos.extend([row, collumn])
                    
                if inputBoard[row+1][collumn+1] == playerNum:
                    countPlayerNum += 1
                elif inputBoard[row+1][collumn+1] == 0:
                    countZero += 1
                    zeroPos.extend([row+1, collumn+1])
                    
                if inputBoard[row+2][collumn+2] == playerNum:
                    countPlayerNum += 1
                elif inputBoard[row+2][collumn+2] == 0:
                    countZero += 1
                    zeroPos.extend([row+2, collumn+2])
                    
                if inputBoard[row+3][collumn+3] == playerNum:
                    countPlayerNum += 1
                elif inputBoard[row+3][collumn+3] == 0:
                    countZero += 1
                    zeroPos.extend([row+3, collumn+3])
                    
                if countPlayerNum == 3 and countZero == 1:
                    heuristicValue += 6 - self.emptySpace(inputBoard, zeroPos[0], zeroPos[1])
        
        #Check for forward slash type 3's
        for collumn in range(collumns-3):
            for row in range(3, rows):
                countPlayerNum = 0
                countZero = 0
                zeroPos = []
                
                if inputBoard[row][collumn] == playerNum:
                    countPlayerNum += 1
                elif inputBoard[row][collumn] == 0:
                    countZero += 1
                    zeroPos.extend([row, collumn])
                    
                if inputBoard[row-1][collumn+1] == playerNum:
                    countPlayerNum += 1
                elif inputBoard[row-1][collumn+1] == 0:
                    countZero += 1
                    zeroPos.extend([row-1, collumn+1])
                    
                if inputBoard[row-2][collumn+2] == playerNum:
                    countPlayerNum += 1
                elif inputBoard[row-2][collumn+2] == 0:
                    countZero += 1
                    zeroPos.extend([row-2, collumn+2])
                    
                if inputBoard[row-3][collumn+3] == playerNum:
                    countPlayerNum += 1
                elif inputBoard[row-3][collumn+3] == 0:
                    countZero += 1
                    zeroPos.extend([row-3, collumn+3])
                    
                if countPlayerNum == 3 and countZero == 1:
                    heuristicValue += 6 - self.emptySpace(inputBoard, zeroPos[0], zeroPos[1])
                
        return heuristicValue
    
    #Check for a tie
    def tieDetector(self, inputBoard):
        for collumn in range(collumns):
            for row in range(rows):
                if inputBoard[row][collumn] == 0:
                    return False
                
        return True
    
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
        
    #Minimax algorithm -- the "brains" of the AI
    def minimax(self, state, depth, maximizingPlayer, a, b):
        currPlayer = 0
        prevPlayer = 0
        if (maximizingPlayer):
            currPlayer = 2
            prevPlayer = 1
        else:
            currPlayer = 1
            prevPlayer = 2
        
        gameOver = self.winningMove(state, prevPlayer)
        tie = self.tieDetector(state)
        
        if (depth == 0) or gameOver or tie:
            if gameOver:
                #print("EOG Scenario detected for player "+str(prevPlayer))
                #Human win
                if (prevPlayer == 1):
                    return (None, -100000 * (depth + 1))
                #AI win
                elif (prevPlayer == 2):
                    return (None, 100000 * (depth + 1))
                #No win -- kind of useless rn because we dont detect ties
            elif tie:
                return (None, 0)
            
            #reached 0 depth -- lets see how many 3's we have
            else:
                if prevPlayer == 1:
                    return (None, -self.threeInARow(state, prevPlayer))
                else:
                    return (None, self.threeInARow(state, prevPlayer))
        
        if (maximizingPlayer):
            value = -math.inf
            for moves in self.possibleMoves(state):
                newState = self.create_board_copy(state)
                self.makeMove(newState, moves, currPlayer)
                move, newValue = self.minimax(newState, depth - 1, False, a, b)
                #If we see a better heuristic value from a move update the best move
                if newValue > value:
                    value = newValue
                    collumn = moves
                    
                #Update our alpha-beta values
                a = max(a, value)
                if a >= b:
                    break
                
            return collumn, value
        
        else:
            value = math.inf
            for moves in self.possibleMoves(state):
                newState = self.create_board_copy(state)
                self.makeMove(newState, moves, currPlayer)
                move, newValue = self.minimax(newState, depth - 1, True, a, b)
                
                if newValue < value:
                    value = newValue
                    collumn = moves
                    
                #Update our alpha-beta values 
                b = min(b, value)
                if b <= a:
                    break
                
            return collumn, value
            
        
    #Handles the gameplay    
    def play(self):
        #Set up audio player
        engine = tts.init()
        #rate = engine.getProperty('rate')
        engine.setProperty('rate', 150)
        voices = engine.getProperty('voices')
        #voices[0] is male, voices[1] is female
        engine.setProperty('voice', voices[0].id)
        
        #Set up mp3 player sounds
        blockingSounds = listdir("./connect4sounds/blockingMoves/")
        winningSound = listdir("./connect4sounds/winningMove/")
        
        playerSelection = True
        firstTurnAI = True
        #currTurn = 1 means its the human player, currTurn = 2 means its the AI player
        currTurn = 0
        while(playerSelection):
            val = input("Press 0 to randomly select the first player, 1 to play human first, 2 to play AI first! \n")
            
            if (val == '0'):
                startingPlayer = rand.randint(1, 2)
                if (startingPlayer == 1):
                    print("Human plays first!")
                    currTurn = 1
                    firstTurnAI = False
                else:
                    print("AI plays first!")
                    currTurn = 2
                
                playerSelection = False
                    
                
         
            elif (val == '1'):
                print("Human plays first!")
                currTurn = 1
                playerSelection = False
                firstTurnAI = False
            
            elif (val == '2'):
                print("AI plays first!")
                currTurn = 2
                playerSelection = False
                
                
            else:
                print("Unrecognized input, please enter 0, 1, or 2.")
        
        
        global screen
        screen = pygame.display.set_mode((windowWidth, windowHeight))
        pygame.init()
        board = self.create_new_board()
        self.draw_board(board)
        pygame.display.update()
        gameOver = False
        
        while (not gameOver):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, empty_chip, (0,0, windowWidth, squaresize))
                    posX = event.pos[0]
                    if currTurn == 1:
                        pygame.draw.circle(screen, red_chip, (posX, squaresize // 2), chipSlotRadius)
                
                pygame.display.update()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(screen, empty_chip, (0, 0, windowWidth, squaresize))
                    
                
                    if (currTurn == 1):
                        #Human Turn
                        posX = event.pos[0]
                        val = math.floor(posX // squaresize)
                        
                        if self.isValidMove(board, val):
                            self.makeMove(board, val, currTurn)
                            
                            self.draw_board(board)
                            
                            if self.winningMove(board, currTurn):
                                gameOver = True
                                print("Human winner!!!")
                                engine.say("It seems I have lost this round.")
                                engine.runAndWait()
                                
                            if self.tieDetector(board):
                                gameOver = True
                                print("Tie detected!!!")
                                engine.say("It seems I have met my match. Lets call this one a tie.")
                                engine.runAndWait()
                                
                            if(currTurn == 1):
                                currTurn = 2
                            else:
                                currTurn = 1
                            
                        else:
                            print("This is not a valid move, please try again!")
            
            #AI Turn
            if (currTurn == 2 and not gameOver):
                boardCopy = self.create_board_copy(board)
                
                if firstTurnAI:
                    collumn = 3
                    firstTurnAI = False
                else:
                    collumn, value = self.minimax(board, 7, True, -math.inf, math.inf)
                    print(value)
                    
                if self.isValidMove(board, collumn):
                    print("AI playing on collumn "+str(collumn + 1))
                    self.makeMove(board, collumn, currTurn)
                    self.draw_board(board)
                    
                    engine.say("AI Playing on callem "+str(collumn+1))
                    engine.runAndWait()
                    
                    #Check if we blocked an opponents connect 4
                    #Play funny sound if so
                    self.makeMove(boardCopy, collumn, 1)
                    if self.winningMove(boardCopy, 1):
                        playsound('./connect4sounds/blockingMoves/'+rand.choice(blockingSounds))
                    
                    
                    if self.winningMove(board, currTurn):
                        gameOver = True
                        print("AI Winner!!!")
                        engine.say("Better luck next time hahahahaha.")
                        engine.runAndWait()
                        
                        playsound('./connect4sounds/winningMove/'+rand.choice(winningSound))
                        
                    elif self.tieDetector(board):
                        gameOver = True
                        print("Tie detected!!!")
                        engine.say("It seems I have met my match. Lets call this one a tie.")
                        engine.runAndWait()
                        
                    if(currTurn == 1):
                        currTurn = 2
                    else:
                        currTurn = 1
        
        if gameOver:
            while(True):
                for event in pygame.event.get():
                    self.draw_board(board)
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        return 0
                        
game = connect4()
game.play()
   
    
    
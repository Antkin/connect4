import connect4

class connect4TesterCode:
    testHorizontal = connect4.create_new_board()
    testVertical = connect4.create_new_board()
    testForwardDiagnol = connect4.create_new_board()
    testBackwardDiagnol = connect4.create_new_board()
    
    #Vertical 
    while(True):
        if(connect4.isValidMove(testVertical, 3)):
            connect4.makeMove(testVertical, 3, 1)
        else:
            break
     
    print("Vertical Test")
    print(testVertical)
    print(connect4.winningMove(testVertical, 1))
    
    #Horizontal
    pointer = 0
    while(True):
        if(connect4.isValidMove(testHorizontal, pointer)):
            connect4.makeMove(testHorizontal, pointer, 1)
            pointer += 1
        else:
            break
        
    print("Horizontal Test")
    print(testHorizontal)
    print(connect4.winningMove(testHorizontal, 1))
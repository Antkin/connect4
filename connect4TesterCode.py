from connect4 import connect4


tester = connect4()
    
testHorizontal = tester.create_new_board()
testVertical = tester.create_new_board()
testForwardDiagnol = tester.create_new_board()
testBackwardDiagnol = tester.create_new_board()

#Vertical 
while(True):
    if(tester.isValidMove(testVertical, 3)):
        tester.makeMove(testVertical, 3, 1)
    else:
        break
 
print("Vertical Test")
print(testVertical)
print(tester.winningMove(testVertical, 1))

#Horizontal
pointer = 0
while(True):
    if(tester.isValidMove(testHorizontal, pointer)):
        tester.makeMove(testHorizontal, pointer, 1)
        pointer += 1
    else:
        break
    
print("Horizontal Test")
print(testHorizontal)
print(str(tester.winningMove(testHorizontal, 1)) + "\n")

print("Empty space test")
print(tester.emptySpace(testHorizontal, 0, 4))
    

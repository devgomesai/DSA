def FuncThree():
    print("Three")
    
def FuncTwo():
    FuncThree()
    print('Two')
    
def FuncOne():
    FuncTwo()
    print('One')
    
FuncOne()
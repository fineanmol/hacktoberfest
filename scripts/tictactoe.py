def sum(a, b, c ):
    return a + b + c

def printBoard(xState, oState):
    zero = 'X' if xState[0] else ('O' if oState[0] else 0)
    one = 'X' if xState[1] else ('O' if oState[1] else 1)
    two = 'X' if xState[2] else ('O' if oState[2] else 2)
    three = 'X' if xState[3] else ('O' if oState[3] else 3)
    four = 'X' if xState[4] else ('O' if oState[4] else 4)
    five = 'X' if xState[5] else ('O' if oState[5] else 5)
    six = 'X' if xState[6] else ('O' if oState[6] else 6)
    seven = 'X' if xState[7] else ('O' if oState[7] else 7)
    eight = 'X' if xState[8] else ('O' if oState[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ") 

def checkWin(xState, oState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X Won the match")
            return 1
        if(sum(oState[win[0]], oState[win[1]], oState[win[2]]) == 3):
            print("O Won the match")
            return 0
    return -1


def valid(move, player):

    if move<0 or move>8:
        return False

    if player==1:

        return oState[move]!=1
    else:
        return xState[move]!=1 

    
if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    oState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe")
    while(True):
        printBoard(xState, oState)
        if(turn == 1):
            print("X's Chance")
            value = int(input("Please enter a value: "))
            while(not valid(value, 1)):
                print("=====INVALID MOVE=====! \n X's Chance")
                value = int(input("Please enter a value: "))
            xState[value] = 1
        else:
            print("O's Chance")
            value = int(input("Please enter a value: "))
            while(not valid(value, 0)):
                print("=====INVALID MOVE=====! \n O's Chance")
                value = int(input("Please enter a value: "))
            oState[value] = 1
        cwin = checkWin(xState, oState)
        if(cwin != -1):
            print("Match over")
            break
        
        turn = 1 - turn

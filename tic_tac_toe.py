board=[1,2,3,4,5,6,7,8,9]

def print_inst(board):
    print("Lets play TIC - TAC - TOE\n")
    print("This is the format of your game board - ")
    print_board(board)
    print("Here you just need to opt for position to fill your X or O")

def print_board(board):
    print("\n")
    print("{} | {} | {}".format(board[0],board[1],board[2]))
    print("{} | {} | {}".format(board[3], board[4], board[5]))
    print("{} | {} | {}".format(board[6], board[7], board[8]))
    print("\n")

def check(board):
    if((board[0] == board[1] == board[2] == "X") or (board[3] == board[4] == board[5] == "X") or (board[6] == board[7] == board[8] == "X") or (board[0] == board[4] == board[8] == "X") or (board[2] == board[4] == board[6] == "X") or (board[0] == board[3] == board[6] == "X") or (board[1] == board[4] == board[7] == "X") or (board[2] == board[5] == board[8] == "X")):
        return("X")
    elif((board[0] == board[1] == board[2] == "O") or (board[3] == board[4] == board[5] == "O") or (board[6] == board[7] == board[8] == "O") or (board[0] == board[4] == board[8] == "O") or (board[2] == board[4] == board[6] == "O") or (board[0] == board[3] == board[6] == "O") or (board[1] == board[4] == board[7] == "O") or (board[2] == board[5] == board[8] == "O")):
        return("O")
    elif((1 not in board) and (2 not in board) and (3 not in board) and (4 not in board) and (5 not in board) and (6 not in board) and (7 not in board) and (8 not in board) and (9 not in board)):
        return("Draw")
    else:
        return(0)

print_inst(board)
player1="X"
player2="O"
print("\nPlayer 1 - \"{}\" , Player 2 - \"{}\" \n".format(player1,player2))

while(True):
    choice1=int(input("Player1 choose your position: "))
    while(choice1 > 9 or choice1 < 1 ):
        print("Error: Invalid choice")
        choice1 = int(input("Player1 choose your position: "))
    while(board[choice1-1]=="X" or board[choice1-1]=="O"):
        print("Error: Position Already Occupied")
        choice1 = int(input("Player1 choose your position: "))
    board[choice1-1] = "X"

    result = check(board)
    if (result == "X"):
        print("\n>>>>> Player 1 won the game <<<<<")
        break
    elif (result == "O"):
        print("\n>>>>> Player 2 won the game <<<<<")
        break
    elif (result == "Draw"):
        print("\n>>>>> It's a Tie between Player 1 and Player 2 <<<<<")
        break

    choice2=int(input("Player2 choose your position: "))
    while (choice2 > 9 or choice2 < 1):
        print("Error: Invalid choice")
        choice2 = int(input("Player2 choose your position: "))
    while (board[choice2 - 1] == "X" or board[choice2 - 1] == "O"):
        print("Error: Position Already Occupied")
        choice2 = int(input("Player2 choose your position: "))
    board[choice2 - 1] = "O"

    print_board(board)
    result=check(board)
    if(result=="X"):
        print("\n>>>>> Player 1 won the game <<<<<")
        break
    elif(result=="O"):
        print("\n>>>>> Player 2 won the game <<<<<")
        break
    elif (result == "Draw"):
        print("\n>>>>> It's a Tie between Player 1 and Player 2 <<<<<")
        break

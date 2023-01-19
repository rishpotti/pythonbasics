#program to play tictactoe with two players

def run():                #this is the main logic module that runs the game.

    q = 'Y'
    while (q == 'Y' or q == 'y'):
    
        row1 = ['1', '2', '3']    #board definition
        row2 = ['4', '5', '6']
        row3 = ['7', '8', '9']
        board = [row1, row2, row3]#end of definition
        i = 1

        p1c = input("Please enter which symbol player one will use (X or O): ") #p1c = player one character
        while p1c != "X" and p1c != "O":
            p1c = input("Please enter which symbol player one will use (X or O): ")
        
        if (p1c == 'X'):
            p2c = 'O'
        else:
            p2c = 'X'

        f1 = 1
        while (i<=9 and f1 == 1):
            f2 = 0
            while (f2 == 0):
                printboard(board)
                print('Please play your move in an empty space.\n')
                if i%2 != 0:
                    x = player_one_input()
                else:
                    x = player_two_input()
                f2 = place_symbol(i, x, board, p1c, p2c)
                print(f2)
                if (f2 == 0):
                    i = i + 1 
                    
                

                if checkboard(i, board, p1c, p2c) == 1:
                    printboard(board)
                    print("Player One wins!")
                    f1 = 0
                    break

                elif checkboard(i, board, p1c, p2c) == 2:
                    printboard(board)
                    print("Player Two wins!")
                    f1 = 0
                    break
                elif (i == 10):
                    printboard(board)
                    print("Draw!")
                    break  

         
        
        f3 = 1
        while f3 == 1:
            q = input("Would you like to play again? (Y/N): ")
            if q == 'Y' or q == 'N' or q == 'y' or q == 'n':
                f3 = 2
            else:
                print("Invalid response.")

def printboard(board):      #this module prints the board's current state.
    print("\n {} | {} | {} \n---|---|---\n {} | {} | {} \n---|---|---\n {} | {} | {}\n".format(board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2], board[2][0], board[2][1], board[2][2]))

def checkboard(i, board, p1c, p2c):      #this module checks the board to see if a player has won
    #if (i%2 == 0):
    if ((board[0][0] == p1c and board[0][1] == p1c and board[0][2] == p1c) or 
    (board[1][0] == p1c and board[1][1] == p1c and board[1][2] == p1c) or
    (board[2][0] == p1c and board[2][1] == p1c and board[2][2] == p1c) or
    
    (board[0][0] == p1c and board[1][0] == p1c and board[2][0] == p1c) or
    (board[0][1] == p1c and board[1][1] == p1c and board[2][1] == p1c) or
    (board[0][2] == p1c and board[1][2] == p1c and board[2][2] == p1c) or

    (board[0][0] == p1c and board[1][1] == p1c and board[2][2] == p1c) or
    (board[0][2] == p1c and board[1][1] == p1c and board[2][0] == p1c)):
        return 1

    elif ((board[0][0] == p2c and board[0][1] == p2c and board[0][2] == p2c) or 
    (board[1][0] == p2c and board[1][1] == p2c and board[1][2] == p2c) or
    (board[2][0] == p2c and board[2][1] == p2c and board[2][2] == p2c) or
    
    (board[0][0] == p2c and board[1][0] == p2c and board[2][0] == p2c) or
    (board[0][1] == p2c and board[1][1] == p2c and board[2][1] == p2c) or
    (board[0][2] == p2c and board[1][2] == p2c and board[2][2] == p2c) or

    (board[0][0] == p2c and board[1][1] == p2c and board[2][2] == p2c) or
    (board[0][2] == p2c and board[1][1] == p2c and board[2][0] == p2c)):
        return 2
        
    else:
        return 0

def player_one_input():          #this module validates and inputs player one's plays
    f = 1
    player_one_position = ''
    player_one_position = input("Player one, enter where you want to place your symbol (1-9): ")
    while f == 1:
        if player_one_position.isdigit() == True:
            x = int(player_one_position)
            if x >= 1 and x <= 9:
                f = 0
            else:
                f = 1
        else:
            f = 1
        
        if f == 1:
            player_one_position = input("Enter where you want to place your symbol (1-9): ")
        

    
    return int(player_one_position)

def player_two_input():          #this module validates and inputs player two's plays
    f = 1
    player_two_position = ''
    player_two_position = input("Player two, enter where you want to place your symbol (1-9): ")
    while f == 1:
        if player_two_position.isdigit() == True:
            x = int(player_two_position)
            if x >= 1 and x <= 9:
                f = 0
            else:
                f = 1
        else:
            f = 1
        
        if f == 1:
            player_two_position = input("Enter where you want to place your symbol (1-9): ")
        

    
    return int(player_two_position)

def place_symbol(i, x, board, p1c, p2c):    #this module validates input and places the token
    if x == 1:
        if (board[0][0] != 'X' and board[0][0] != 'O'):
            if i%2 != 0:
                board[0][0] = p1c
            else:
                board[0][0] = p2c
            return(0)
        else:
            return(1)
    elif x == 2:
        if (board[0][1] != 'X' and board[0][1] != 'O'):
            if i%2 != 0:
                board[0][1] = p1c
            else:
                board[0][1] = p2c
            return(0)
        else:
            return(1)
    elif x == 3:
        if (board[0][2] != 'X' and board[0][2] != 'O'):
            if i%2 != 0:
                board[0][2] = p1c
            else:
                board[0][2] = p2c
            return(0)
        else:
            return(1)
    elif x == 4:
        if (board[1][0] != 'X' and board[1][0] != 'O'):
            if i%2 != 0:
                board[1][0] = p1c
            else:
                board[1][0] = p2c
            return(0)
        else:
            return(1)
    elif x == 5:
        if (board[1][1] != 'X' and board[1][1] != 'O'):
            if i%2 != 0:
                board[1][1] = p1c
            else:
                board[1][1] = p2c
            return(0)
        else:
            return(1)
    elif x == 6:
        if (board[1][2] != 'X' and board[1][2] != 'O'):
            if i%2 != 0:
                board[1][2] = p1c
            else:
                board[1][2] = p2c
            return(0)
        else:
            return(1)
    elif x == 7:
        if (board[2][0] != 'X' and board[2][0] != 'O'):
            if i%2 != 0:
                board[2][0] = p1c
            else:
                board[2][0] = p2c
            return(0)
        else:
            return(1)
    elif x == 8:
        if (board[2][1] != 'X' and board[2][1] != 'O'):
            if i%2 != 0:
                board[2][1] = p1c
            else:
                board[2][1] = p2c
            return(0)
        else:
            return(1)
    elif x == 9:
        if (board[2][2] != 'X' and board[2][2] != 'O'):
            if i%2 != 0:
                board[2][2] = p1c
            else:
                board[2][2] = p2c
            return(0)
        else:
            return(1)


run() #music plays
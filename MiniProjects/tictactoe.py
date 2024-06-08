"""
Make a tic-tac-toe game for two players.

Write a script to play two dimensional 
Tic-Tac-Toe between two human players
who alternate entering their moves
on the same computer. Use a 3-by-3
two-dimensional array. Each player indicates their
moves by entering a pair
of numbers representing the row and column indices of the
 square in which they
want to place their mark, either an 'X' or an 'O'. When the first player 
moves,
place an 'X' in the specified square. When the second player moves, place an
'O'
in the specified square. Each move must be to an empty square. After each move,
determine
whether the game has been won and whether it’s a draw.

Name: Sufyan Chaudhry
"""

import numpy as np
board = np.full((3,3), " ")
print(board)

win = "no"

while win == "no":
    row1 = eval(input("Player 1 pick a row (0-2): "))
    col1 = eval(input("Player 1 pick a column (0-2): "))
    while board[row1, col1] == " ":
        if board[row1, col1] == " ":
            board[row1, col1] = "X"
        else:
            print("Invalid input, try again.")
            row1 = eval(input("Player 1 pick a row (0-2): "))
            col1 = eval(input("Player 1 pick a column (0-2): "))
            
    print(board)

#horizontal
    for row in board:
        if " " not in row:
            column_1 = row[0]
            column_2 = row[1]
            column_3 = row[2]
            if column_1 == column_2 == column_3:
                print("You won!!!")
                win = "yes"
    if win == "yes":
        break
#vertical
    for col in range(len(board[0])):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != " ":
            print("You won!!!")
            win = "yes"
    if win == "yes":
        break

#diagnal
    if board[0,0] == board[1,1] == board[2,2] and board[0,0] != " ":
        print("You won!!!!")
        win = "yes"
    elif board[0,2] == board[1,1] == board[2,0] and board[0,2] != " ":
        print("You won!!!!")
        win = "yes"
    if win == "yes":
        break
    
#draw    
    if " " not in board:
        print("Game is a draw")
        break

    
    row2 = eval(input("Player 2 pick a row (0-2): "))
    col2 = eval(input("Player 2 pick a column (0-2): "))
    while board[row2, col2] == " ":
        if board[row2, col2] == " ":
            board[row2, col2] = "O"
        else:
            print("Invalid input, try again.")
            row2 = eval(input("Player 2 pick a row (0-2): "))
            col2 = eval(input("Player 2 pick a column (0-2): "))
    print(board)

#horizontal
    
    for row in board:
        if " " not in row:
           column_1 = row[0]
           column_2 = row[1]
           column_3 = row[2]
           if column_1 == column_2 == column_3:
               print("You won!!!")
               win = "yes"
    if win == "yes":
        break

#vertical
    for col in range(len(board[0])):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != " ":
                print("You won!!!")
                win = "yes"
    if win == "yes":
        break

#diagnal
    if board[0,0] == board[1,1] == board[2,2] and board[0,0] != " ":
        print("You won!!!!")
        win = "yes"
    elif board[0,2] == board[1,1] == board[2,0] and board[0,2] != " ":
        print("You won!!!!")
        win = "yes"
    if win == "yes":
        break

#draw  
    if " " not in board and win == "no":
        print("Game is a draw")
        break
    

import random

def print_board(board):
    print(board[0]+' |', board[1]+' |', board[2])
    print('---------')
    print(board[3]+' |', board[4]+' |', board[5])
    print('---------')
    print(board[6]+' |', board[7]+' |', board[8])

def player_move(board):
    p = input("Enter the location where you want to place (from 1-9): ")
    if p.isdigit():
        p = int(p)
        if 9 >= p >= 1:
            if board[p-1] == '-':
                board[p-1] = 'X'
                return True
            else:
                print("-Cell already occupied. Try again.")
                return False
        else:
            print("-Try again. You entered an invalid position.")
            return False
    else:
        print("-Try again. You entered an invalid position.")
        return False

def ai_move(board):
    # Check for winning moves
    for i in range(9):
        if board[i] == '-':
            board[i] = 'O'
            if check_win(board):
                return
            board[i] = '-'

    # Check for blocking moves
    for i in range(9):
        if board[i] == '-':
            board[i] = 'X'
            if check_win(board):
                board[i] = 'O'
                return
            board[i] = '-'

    # Choose a random move if no winning or blocking moves
    empty_cells = [i for i in range(9) if board[i] == '-']
    if empty_cells:
        move = random.choice(empty_cells)
        board[move] = 'O'


def check_win(board):
    if winlogic_row(board) or winlogic_column(board) or winlogic_diag(board):
        return True
    return False

def winlogic_row(board):
    if board[0] == board[1] == board[2] and board[0] != '-':
        return True
    elif board[3] == board[4] == board[5] and board[4] != '-':
        return True
    elif board[6] == board[7] == board[8] and board[8] != '-':
        return True
    return False

def winlogic_column(board):
    if board[0] == board[3] == board[6] and board[0] != '-':
        return True
    elif board[1] == board[4] == board[7] and board[4] != '-':
        return True
    elif board[2] == board[5] == board[8] and board[8] != '-':
        return True
    return False

def winlogic_diag(board):
    if board[0] == board[4] == board[8] and board[0] != '-':
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':
        return True
    return False

def check_draw(board):
    for cell in board:
        if cell == '-':
            return False
    return True

board = ['-','-','-',
         '-','-','-',
         '-','-','-'
        ]

player= "X"
ai_marker='O'
winner = None

while True:
    print_board(board)
    print("."*30)
    if player == "X":
        if player_move(board):
            if check_win(board):
                print_board(board)
                print("."*30)
                print("--Player X has won!")
                break
            if check_draw(board):
                print_board(board)
                print("."*30)
                print("--It's a draw!")
                break
            player = "O"
    else:
        ai_move(board)
        if check_win(board):
            print_board(board)
            print("."*30)
            print("--Player O has won!")
            break
        if check_draw(board):
            print_board(board)
            print("."*30)
            print("--It's a draw!")
            break
        player = "X"

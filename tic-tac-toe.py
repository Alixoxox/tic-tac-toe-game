import random

board = ['-','-','-',
         '-','-','-',
         '-','-','-'
        ]
player= "X"
ai_marker='O'
winner = None

## BOARD LOGIC
def print_board(board):
    print(board[0]+' |', board[1]+' |', board[2])
    print('---------')
    print(board[3]+' |', board[4]+' |', board[5])
    print('---------')
    print(board[6]+' |', board[7]+' |', board[8])

## PLAYER
def player_move(board):
    global player
    global winner
    p = int(input("Enter the location where you want to place (from 1-9): "))
    if 9 >= p >= 1:
        if board[p-1] == '-':
            board[p-1] = player
        else:
            print("Cell already occupied. Try again.")
            return player_move(board)
    elif p==0:
        print("Try again. You entered an invalid position.")
        return player_move(board)
    else:
        print("Try again. You entered an invalid position.")
        return player_move(board)
#AI
def ai_move(board):
    global winner
    position = random.randint(0, 8)
    if board[position] == '-':
        board[position] = ai_marker
    else:
        ai_move(board)

def alternation(board):
    global player
    global winner
    if player=='X' in board:
        if check_win is True:
            exit
        else:
            return ai_marker 
    elif player=='X' not in board:
        return player(board)


def winlogic_row(board):
    ## for row
    global winner
    if board[0] == board[1] == board[2] and board[0] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[8] != '-':
        winner = board[6]
        return True
    return False

def winlogic_column(board):
    ## for column
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True
    return False

def winlogic_diag(board):
    ## for diagonals
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True
    return False

def check_win(board):
    global winner
    if winlogic_row(board) or winlogic_column(board) or winlogic_diag(board):
        print(f"{winner} has won")
        exit()

while True:
    print_board(board)
    player_move(board)
    if check_win(board):
        print_board(board)
        print(f"{winner} has won!")
        break

    print_board(board)
    print("----------------xxxxx--------------------")
    ai_move(board)
    if check_win(board):
        print_board(board)
        print(f"{winner} has won!")
        break

board = ['-','-','-',
         '-','-','-',
         '-','-','-'
]
playerx = "X"
winner = None

## BOARD LOGIC
def printboard(board):
    print(board[0]+' |',board[1]+' |',board[2])
    print('----------')
    print(board[3]+' |',board[4]+' |',board[5])
    print('----------')
    print(board[6]+' |',board[7]+' |',board[8])

## PLAYER
def player(board):
    global playerx
    global winner
    p = int(input("Enter the location where you want to place (from 1-9): "))
    if 9 >= p >= 1:
        if board[p-1] == '-':
            board[p-1] = playerx
        else:
            print("Cell already occupied. Try again.")
            player(board)
    else:
        print("Try again. You entered an invalid position.")
        player(board)

def player2(board):
    global playerx
    global winner
    if playerx=='X':
        playerx='0'
        return player(board)
    elif playerx=='0':
        playerx='X'
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
    printboard(board)
    player(board)
    check_win(board)
    printboard(board)  # print the board after the first player's move
    player2(board)
    check_win(board)
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

####  HINT BOARD
board_example = ['1','2','3',
         '4','5','6',
         '7','8','9'
        ]

def print_board_example(board_example):
    print(board_example[0]+' |', board_example[1]+' |', board_example[2])
    print('---------')
    print(board_example[3]+' |', board_example[4]+' |', board_example[5])
    print('---------')
    print(board_example[6]+' |', board_example[7]+' |', board_example[8])

player= "X"
ai_marker='O'
winner = None

player_wins = 0
ai_wins = 0
draws = 0

while True:
    print("Welcome to Tic-Tac-Toe!")
    print("To place your 'X', enter the number corresponding to the position on the board.")
    print("Example Tic-Tac-Toe Board:")
    print_board_example(board_example)
    num_rounds = input("Enter the number of rounds you want to play (must be odd): ")

    if num_rounds.isdigit():
        num_round = int(num_rounds)

        if num_round % 2 != 0:
            for _ in range(1, num_round + 1):
                board = ['-','-','-',
                         '-','-','-',
                         '-','-','-'
                        ]
                player = "X"
                print(f"Round {_}")
                while True:
                    print_board(board)
                    print("." * 30)
                    if player == "X":
                        if player_move(board):
                            if check_win(board):
                                print_board(board)
                                print("." * 30)
                                print("--Player X has won this round!")
                                player_wins += 1
                                break
                            if check_draw(board):
                                print_board(board)
                                print("." * 30)
                                print("--It's a draw this round!")
                                draws += 1
                                break
                            player = "O"
                    else:
                        ai_move(board)
                        if check_win(board):
                            print_board(board)
                            print("." * 30)
                            print("--AI has won this round!")
                            ai_wins += 1
                            break
                        if check_draw(board):
                            print_board(board)
                            print("." * 30)
                            print("--It's a draw this round!")
                            draws += 1
                            break
                        player = "X"

                print("Current Score:")
                print(f"Player: {player_wins}")
                print(f"AI: {ai_wins}")
                print(f"Draws: {draws}")

                if player_wins > ai_wins:
                    print("Congratulations! You are currently winning!!")
                elif ai_wins > player_wins:
                    print("GET your game together, AI is winning against you!")
                else:
                    print("As of now, the current game is heading towards a draw")

            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != 'yes':
                print("Thanks for playing!")
                break
        else:
            print("Please enter an odd number!")
    else:
        print("Please enter a valid integer!!")
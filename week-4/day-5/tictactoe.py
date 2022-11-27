def display_board(board):

    out = ""

    for choice in board.keys():
        if choice % 3 == 0:
            out += '\n'
        if not board[choice]:
            out += f'| |'
        else:
            out += f'|{board[choice]}|'

    print(out)


def player_input(player,board):

    while True:
        player_in = input(f'Where to put your {player}: ')

        if player_in.isnumeric():
            player_in = int(player_in)

            if player_in in board:
                if board[player_in]:
                    print("Cell is occupied")
                else:
                    board[player_in] = player
                    break
            else:
                print("THERE's NOT such Key!")

        else:
            print("INCORRECT INPUT")
            continue

def check_win(board):
    winner = None 

    for row_idx1 in [0, 3, 6]:
        row_idx2, row_idx3 = row_idx1 + 1, row_idx1 + 2
        if board[row_idx1] == board[row_idx2] == board[row_idx3] != None:
            winner = board[row_idx1]

    for column_idx1 in [0, 1, 2]:
        column_idx2, column_idx3 = column_idx1 + 3, column_idx1 + 6
        if board[column_idx1] == board[column_idx2] == board[column_idx3] != None:
            winner = board[column_idx1]

    diag_index1 = 4
    for change in [4, 2]:              
        diag_index2, diag_index3 = diag_index1 - change, diag_index1 + change
        if board[diag_index1] == board[diag_index2] == board[diag_index3] != None:
            winner = board[diag_index1]

    if winner:
        print(f"THE WINNER IS {winner}")

    return winner

def play():
    pass
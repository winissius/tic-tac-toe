print(f'Tic-Tac-Toe\n')

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
counter = 0
end = False
win = " "


def print_board():
    for i in range(0, 3):
        if i == 0:
            print('   1   2   3')
        print(f'{i + 1} [{board[i][0]}] [{board[i][1]}] [{board[i][2]}]')


def def_users():
    player1 = input('Say the name of the first player who will play with X\n')
    player2 = input('Say the name of the second player who will play with O\n')
    atualPlayer = player1
    return player1, player2, atualPlayer


def chose_cell(atualPlayer, player1, player2):
    if atualPlayer == player1:
        symbol = "X"
    else:
        symbol = "O"
    full = is_full()
    while not full:
        end_game()
        choose = input(f"\nPlayer {atualPlayer}, please choose one cell, format 0x0\n")
        print(f'You choose {choose}')
        if board[(int(choose[0]) - 1)][(int(choose[2]) - 1)] == " ":
            board[(int(choose[0]) - 1)][(int(choose[2]) - 1)] = symbol
            break
        else:
            print("Invalid position")
    pass_turn(player1, player2)


def pass_turn(player1, player2):
    global atualPlayer
    if atualPlayer == player1:
        atualPlayer = player2
    else:
        atualPlayer = player1
    return atualPlayer


def end_game():
    global win
    global end
    win = winner()
    if is_full():
        end = True
        if win != player1 or win != player2:
            print(f"Game over\nThe game ended in a draw!")
    if win == player1 or win == player2:
        end = True
    if end:
        if win == player1 or win == player2:
            print(f"Game over\nThe winner is {winner}!")


def winner():
    global winner
    for line in range(0, 3):
        if board[line][0] == board[line][1] == board[line][2] == "X":
            winner = player1
            break
        if board[line][0] == board[line][1] == board[line][2] == "O":
            winner = player2
            break

    for column in range(0, 3):
        if board[0][column] == board[1][column] == board[2][column] == "X":
            winner = player1
            break
        if board[0][column] == board[1][column] == board[2][column] == "O":
            winner = player2
            break
    #diagonal
    if board[0][0] == board[1][1] == board[2][2] == "X":
        winner = player1
    if board[0][0] == board[1][1] == board[2][2] == "O":
        winner = player2
    if board[0][2] == board[1][1] == board[2][0] == "X":
        winner = player1
    if board[0][2] == board[1][1] == board[2][0] == "O":
        winner = player2
    return winner


def is_full():
    counterElements = 0
    for sub in board:
        for i in sub:
            if i != " ":
                counterElements += 1
    if counterElements >= 9:
        return True


player1, player2, atualPlayer = def_users()
print_board()

while not end:
    chose_cell(atualPlayer, player1, player2)
    print_board()
    end_game()







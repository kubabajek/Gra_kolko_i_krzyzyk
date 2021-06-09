from DataClasses.DataGamesResult import DataGamesResult


def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |     |     |")
    print("\t  {}  |  {}  |  {}  |  {}  |  {}".format(values[0], values[1], values[2], values[3], values[4]))
    print('\t_____|_____|_____|_____|_____')
    print("\t     |     |     |     |")
    print("\t  {}  |  {}  |  {}  |  {}  |  {}".format(values[5], values[6], values[7], values[8], values[9]))
    print('\t_____|_____|_____|_____|_____')
    print("\t     |     |     |     |")
    print("\t  {}  |  {}  |  {}  |  {}  |  {}".format(values[10], values[11], values[12], values[13], values[14]))
    print('\t_____|_____|_____|_____|_____')
    print("\t     |     |     |     |")
    print("\t  {}  |  {}  |  {}  |  {}  |  {}".format(values[15], values[16], values[17], values[18], values[19]))
    print('\t_____|_____|_____|_____|_____')
    print("\t     |     |     |     |")
    print("\t  {}  |  {}  |  {}  |  {}  |  {}".format(values[20], values[21], values[22], values[23], values[24]))
    print("\t     |     |     |     |")
    print("\n")


# Function to print the score-board
def print_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t          TABLICA WYNIKOW       ")
    print("\t--------------------------------")

    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])

    print("\t--------------------------------\n")


# Function to check if any player has won
def check_win(player_pos, cur_player):
    # All possible winning combinations
    soln = [[1,2,3], [2,3,4], [3,4,5], [6,7,8], [7,8,9], [8,9,10], [11, 12, 13], [12,13,14], [13,14,15,], [16,17,17], [17,18,19], [18,19,20], [21,22,23,], [22,23,24], [23,24,25],
            [1,6,11], [6,11,16], [11,16,21], [2,7,12], [7,12,17], [12,17,22], [3,8,13], [8,13,18], [13,18,23], [4,9,14], [9,14,19], [14,19,24], [5,10,15], [10,15,20], [15,20,25],
            [3,9,15], [2,8,14], [8,14,20], [1,7,13], [7,13,19], [13,19,25], [6,12,18], [12,18,24], [11,17,23],
            [3,7,11], [4,8,12], [8,12,16], [5,9,13], [9,13,17], [13,17,21], [10,14,18], [14,18,22], [15,19,23]]

    # Loop to check if any winning combination is satisfied
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):
            # Return True if any winning combination satisfies
            return True
    # Return False if no combination is satisfied
    return False


# Function to check if the game is drawn
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 25:
        return True
    return False


# Function for a single game of Tic Tac Toe
def single_game(cur_player):
    # Represents the Tic Tac Toe
    values = [' ' for x in range(25)]

    # Stores the positions occupied by X and O
    player_pos = {'X': [], 'O': []}

    # Game Loop for a single game of Tic Tac Toe
    while True:
        print_tic_tac_toe(values)

        # Try exception block for MOVE input
        try:
            print("Ruch gracza:  ", cur_player, ". Ktore pole? : ", end="")
            move = int(input())
        except ValueError:
            print("Nieprawidlowa wartosc, wpisz jeszcze raz")
            continue

        # Sanity check for MOVE inout
        if move < 1 or move > 25:
            print("Nieprawidlowa wartosc, wpisz jeszcze raz")
            continue

        # Check if the box is not occupied already
        if values[move - 1] != ' ':
            print("To pole jest juz zajete, wybierz inne")
            continue

        try:
            print("Czy chcesz cofnąć ruch? \n 1 - Tak \n 2 - Nie")
            remove = int(input())
        except ValueError:
            print("Nieprawidlowa wartosc, wpisz jeszcze raz")
            continue

        if remove == 1:
            continue
        elif remove == 2:
            values[move - 1] = cur_player
        else:
            print("Nieprawidlowa wartosc")
            continue

        # Updating player positions
        player_pos[cur_player].append(move)

        # Function call for checking win
        if check_win(player_pos, cur_player):
            print_tic_tac_toe(values)
            print("Gracz: ", cur_player, " zwyciezyl w pieknym stylu!!")
            print("\n")
            return cur_player

        # Function call for checking draw game
        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print("Remis")
            print("\n")
            return 'D'

        # Switch player moves
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'


def main():
    liczbagier = 0
    player1 = input("Graczu 1, podaj imie : ")
    player2 = input("Graczu 2, podaj imie : ")


    # Stores the player who chooses X and O
    cur_player = player1

    # Stores the choice of players
    player_choice = {'X': "", 'O': ""}

    # Stores the options
    options = ['X', 'O']

    # Stores the scoreboard
    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)

    # Game Loop for a series of Tic Tac Toe
    # The loop runs until the players quit
    while True:

        # Player choice Menu
        print("Gracz", cur_player,"wybiera czym bedzie")
        print("1 - X")
        print("2 - O")
        print("3 - Opusc gre")

        # Try exception for CHOICE input
        try:
            choice = int(input())
        except ValueError:
            print("Nieprawidlowa wartosc, wpisz dobra\n")
            continue

        # Conditions for player choice
        if choice == 1:
            liczbagier += 1
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1

        elif choice == 2:
            liczbagier += 1
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1

        elif choice == 3:
            print("Punktacja")
            print_scoreboard(score_board)
            break

        else:
            print("Nieprawidlowa wartosc, wpisz dobra\n")

        # Stores the winner in a single game of Tic Tac Toe
        winner = single_game(options[choice - 1])

        # Edits the scoreboard according to the winner
        if winner != 'D':
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1

        print_scoreboard(score_board)
        # Switch player who chooses X or O
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1

    return DataGamesResult(liczbagier, score_board)

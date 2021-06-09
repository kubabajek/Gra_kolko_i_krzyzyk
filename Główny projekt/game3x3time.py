from DataClasses.DataGamesResult import DataGamesResult
import time
from threading import Thread


def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
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
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    # Loop to check if any winning combination is satisfied
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):
            # Return True if any winning combination satisfies
            return True
    # Return False if no combination is satisfied
    return False


# Function to check if the game is drawn
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False




# Function for a single game of Tic Tac Toe
def single_game(cur_player):
    # Represents the Tic Tac Toe
    values = [' ' for x in range(9)]

    # Stores the positions occupied by X and O
    player_pos = {'X': [], 'O': []}

    print("Zdecydujcie ile czasu macie na przemyślenie ruch i podajcie go w następnym poleceniu.")

    t = int(input("Podaj czas w sekundach: "))

    # Game Loop for a single game of Tic Tac Toe

    while True:

        print_tic_tac_toe(values)

        # Try exception block for MOVE input
        thread = Thread(target=countdown(t))
        thread.start()

        try:
            print("Ruch gracza:  ", cur_player, ". Ktore pole? : ", end="")
            move = int(input())
        except ValueError:
            print("Nieprawidlowa wartosc, wpisz jeszcze raz")
            continue


        if move < 1 or move > 9:
            print("Nieprawidlowa wartosc, wpisz jeszcze raz")
            continue

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


        # Sanity check for MOVE inout


        # Check if the box is not occupied already


        # Update game information

        # Updating grid status
        values[move - 1] = cur_player

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



def countdown(t):

    while t >= 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1




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

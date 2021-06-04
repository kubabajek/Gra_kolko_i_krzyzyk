def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |     |")
    print("\t  {}  |  {}  |  {}  |  {}".format(values[0], values[1], values[2], values[3]))
    print('\t_____|_____|_____|_____')
    print("\t     |     |     |")
    print("\t  {}  |  {}  |  {}  |  {}".format(values[4], values[5], values[6], values[7]))
    print('\t_____|_____|_____|_____')
    print("\t     |     |     |")
    print("\t  {}  |  {}  |  {}  |  {}".format(values[8], values[9], values[10], values[11]))
    print('\t_____|_____|_____|_____')
    print("\t     |     |     |")
    print("\t  {}  |  {}  |  {}  |  {}".format(values[12], values[13], values[14], values[15]))
    print("\t     |     |     |")
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
    soln = [[1, 2, 3], [2, 3, 4], [5, 6, 7], [6,7,8], [9,10,11], [10,11,12], [13,14,15], [14,15,16],[1,5,9],[5,9,13],[2,6,10],[6,10,14],[3,7,11],[7,11,15],[4,8,12],[8,12,16],[2,7,12],[1,6,11],[6,11,16],[5,10,15],[3,6,9],[4,7,10],[7,10,13],[8,11,14]]

    # Loop to check if any winning combination is satisfied
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):
            # Return True if any winning combination satisfies
            return True
    # Return False if no combination is satisfied
    return False


# Function to check if the game is drawn
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 16:
        return True
    return False


# Function for a single game of Tic Tac Toe
def single_game(cur_player):
    # Represents the Tic Tac Toe
    values = [' ' for x in range(16)]

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
        if move < 1 or move > 16:
            print("Nieprawidlowa wartosc, wpisz jeszcze raz")
            continue

        # Check if the box is not occupied already
        if values[move - 1] != ' ':
            print("To pole jest juz zajete, wybierz inne")
            continue

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
    return liczbagier
# Global Var

# Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If game still going
game_still_going = True
winner = None
current_player = "X"

def maintic():

    def display_board():
        # takes board index 0 and puts a | next to it and repeats if for each board index to make the tic tac toe board... smart.
        print(board[0] + ' | ' + board[1] + ' | ' + board[2])
        print(board[3] + ' | ' + board[4] + ' | ' + board[5])
        print(board[6] + ' | ' + board[7] + ' | ' + board[8])

    def play_game():
        # First thing, display the board
        display_board()
        while game_still_going:
            handle_turn(current_player)
            check_if_game_over()
            flip_player()
        # game ended
        if winner == 'X' or winner == 'O':
            print(winner + ' won.')
        elif winner == None:
            print('Tie.')



    def handle_turn(player):
        print(player + "'s Turn.")
        position = input("Pick A Position From 1 to 9 -> ")

        valid = False
        while not valid:
            while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                position = input("Pick A Position From 1 to 9 -> ")

            position = int(position) - 1

            if board[position] == "-":
                valid = True
            else:
                print("You Can't Go There! Try Again!")

        board[position] = player
        display_board()

    def check_if_game_over():
        check_for_winner()
        check_if_tie()

    def check_for_winner():
        # global var
        global winner

        # Check rows
        row_winner = check_rows()
        # Check columns
        column_winner = check_columns()
        # Check diagonals
        diagonal_winner = check_diagonals()
        if row_winner:
            # win
            winner = row_winner
            winner = row_winner
        elif column_winner:
            # win
            winner = column_winner
        elif diagonal_winner:
            # win
            winner = diagonal_winner
        else:
            # no win. tie
            winner = None
        return

    def check_rows():
        # global var
        global game_still_going
        # my idea: if board[1 - 3] == "X" or board[1 - 3] == "O":
        # check if any rows have the same value and don't equal to -
        row_1 = board[0] == board[1] == board[2] != "-"
        row_2 = board[3] == board[4] == board[5] != "-"
        row_3 = board[6] == board[7] == board[8] != "-"
        # if any rows have a match, flag it.
        if row_1 or row_2 or row_3:
            game_still_going = False
        # return the winner (X or O)
        if row_1:
            return board[0]
        elif row_2:
            return board[3]
        elif row_3:
            return board[6]
        return
    def check_columns():
        # global var
        global game_still_going
        # my idea: if board[1 - 3] == "X" or board[1 - 3] == "O":
        # check if any columns have the same value and don't equal to -
        column_1 = board[0] == board[3] == board[6] != "-"
        column_2 = board[1] == board[4] == board[7] != "-"
        column_3 = board[2] == board[5] == board[8] != "-"
        # if any column have a match, flag it.
        if column_1 or column_2 or column_3:
            game_still_going = False
        # return the winner (X or O)
        if column_1:
            return board[0]
        elif column_2:
            return board[1]
        elif column_3:
            return board[2]
        return
    def check_diagonals():
        # global var
        global game_still_going
        # my idea: if board[1 - 3] == "X" or board[1 - 3] == "O":
        # check if any diagonals have the same value and don't equal to -
        diagonal_1 = board[0] == board[4] == board[8] != "-"
        diagonal_2 = board[6] == board[4] == board[2] != "-"
        # if any diagonals have a match, flag it.
        if diagonal_1 or diagonal_2:
            game_still_going = False
        # return the winner (X or O)
        if diagonal_1:
            return board[0]
        elif diagonal_2:
            return board[6]
        return

    def check_if_tie():
        global game_still_going
        if '-' not in board:
            game_still_going = False
            return
        return

    def flip_player():
        # global var
        global current_player
        # switch player from X to O and so on
        if current_player == 'X':
            current_player = 'O'
        elif current_player == 'O':
            current_player = 'X'
            return
    play_game()
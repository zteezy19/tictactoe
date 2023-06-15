import random


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('_')
                self.board.append(row)

# function to randomly pick a player
    def get_random_first_player(self):
        return random.randint(0, 1)

# function to fix a player's spot on the board
    def fix_spot(self, row, col, player):
        self.board[row][col] = player

class TicTacToe:

    def __init__(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def show_board(self):
        for row in self.board:
            print(' '.join(row))

    def make_move(self, row, col):
        if self.board[row][col] == '-':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Invalid move. Please try again.")

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != '-':
                return row[0]

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '-':
                return self.board[0][col]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '-':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '-':
            return self.board[0][2]

        return None

    def is_board_full(self):
        for row in self.board:
            if '-' in row:
                return False
        return True

    def start_game(self):
        while True:
            self.show_board()

            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))

            self.make_move(row, col)

            winner = self.check_winner()
            if winner:
                print(f"Player {winner} wins!")
                break
            elif self.is_board_full():
                print("It's a draw!")
                break


tic_tac_toe = TicTacToe()
tic_tac_toe.start_game()

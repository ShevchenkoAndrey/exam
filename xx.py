class InvalidInputError(Exception):
    pass

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 5)

    def check_winner(self):
        for row in self.board:
            if len(set(row)) == 1 and row[0] != ' ':
                return row[0]

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != ' ':
                return self.board[0][col]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return self.board[0][2]

        return None

    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                row = int(input(f"Player {self.current_player}, enter row (0, 1, 2): "))
                col = int(input(f"Player {self.current_player}, enter column (0, 1, 2): "))
                if row not in range(3) or col not in range(3):
                    raise InvalidInputError("Row and column values must be between 0 and 2.")
                if self.board[row][col] != ' ':
                    raise InvalidInputError("This position is already taken. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            except InvalidInputError as e:
                print(e)
                continue

            self.board[row][col] = self.current_player
            winner = self.check_winner()

            if winner:
                self.print_board()
                print(f"Player {winner} wins!")
                break

            if self.is_board_full():
                self.print_board()
                print("It's a tie!")
                break

            self.current_player = 'O' if self.current_player == 'X' else 'X'

if __name__ == "__main__":
    game = TicTacToe()
    game.play()

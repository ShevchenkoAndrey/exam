class TicTacToe:
    def __init__(self):
        self.board = Board()
        self.current_player = 'X'

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        while True:
            self.board.print_board()
            row = int(input(f"Player {self.current_player}, enter row (0, 1, 2): "))
            col = int(input(f"Player {self.current_player}, enter column (0, 1, 2): "))

            try:
                self.board.mark_position(row, col, self.current_player)
            except ValueError as e:
                print(e)
                continue

            if self.board.check_winner():
                self.board.print_board()
                print(f"Player {self.current_player} wins!")
                break

            if self.board.is_full():
                self.board.print_board()
                print("It's a tie!")
                break

            self.switch_player()


class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 5)

    def mark_position(self, row, col, player):
        if self.board[row][col] == ' ':
            self.board[row][col] = player
        else:
            raise ValueError("This position is already taken. Try again.")

    def check_winner(self):
        for row in self.board:
            if len(set(row)) == 1 and row[0] != ' ':
                return True

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != ' ':
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return True

        return False

    def is_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True


def main():
    game = TicTacToe()
    game.play()


if __name__ == "__main__":
    main()

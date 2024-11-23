# Tic Tac Toe...

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def print_board(self):
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("---------")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("---------")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

    def winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], 
            [0, 3, 6], [1, 4, 7], [2, 5, 8], 
            [0, 4, 8], [2, 4, 6]
        ]
        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != " ":
                return self.board[combination[0]]
        return None

    def draw(self):
        return " " not in self.board

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            return True
        else:
            print("\tPosition is already occupied! Choose another.\n")
            return False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def game_begin(self):
        while True:
            self.print_board()
            try:
                position = int(input(f"Player {self.current_player},Enter a position 1-9: ")) - 1
            except ValueError:
                print("\tInvalid input. Please enter a number between 1 - 9.")
                continue

            if position < 0 or position >= 9:
                print("\tInvalid position. Please choose a number between 1 - 9.")
                continue

            if not self.make_move(position):
                continue

            winner = self.winner()
            if winner:
                self.print_board()
                print(f"\t Congrats! Player {winner} wins the game!")
                break

            if self.draw():
                self.print_board()
                print("\tOops! It is a tie!")
                break

            self.switch_player()

tic_tac_toe=TicTacToe()
tic_tac_toe.game_begin()


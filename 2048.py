import os
import random

BOARD_SIZE = 4
EMPTY_CELL = 0
WINNING_CELL = 16
POSSIBLE_NEW_NUMBERS = [2, 4]


class Game:
    def __init__(self) -> None:
        self.board = self.init_board()
        self.has_lost = False
        self.has_won = False

        self.print_board(self.board)

        self.start_game()

    def start_game(self):
        while not self.has_won and not self.has_lost:
            move = self.get_move_input()

            if move == "W":
                new_board = self.rotate_matrix_90_clockwise(
                    self.rotate_matrix_90_clockwise(self.board)
                )
                new_board = self.move_logic(new_board)
                self.board = self.rotate_matrix_90_counterclockwise(
                    self.rotate_matrix_90_counterclockwise(new_board)
                )

            elif move == "D":
                new_board = self.rotate_matrix_90_clockwise(self.board)
                new_board = self.move_logic(new_board)
                self.board = self.rotate_matrix_90_counterclockwise(new_board)

            elif move == "A":
                new_board = self.rotate_matrix_90_counterclockwise(self.board)
                new_board = self.move_logic(new_board)
                self.board = self.rotate_matrix_90_clockwise(new_board)

            elif move == "S":
                self.board = self.move_logic(self.board)

            self.insert_new_number()
            self.print_board(self.board)

            if self.has_won:
                print("congrats! you won :)")
                return

        if self.has_lost:
            print("game over :(")

    def init_board(self) -> list[list[int]]:
        board = [[EMPTY_CELL] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        pos1, pos2 = self.randomize_initial_positions()
        board[pos1[0]][pos1[1]] = self.randomize_new_number()
        board[pos2[0]][pos2[1]] = self.randomize_new_number()
        return board

    def randomize_new_number(
        self,
    ) -> int:
        return random.choice(POSSIBLE_NEW_NUMBERS)

    def randomize_position(
        self,
    ) -> tuple[int, int]:
        return (random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1))

    def randomize_initial_positions(
        self,
    ) -> tuple[tuple[int, int], tuple[int, int]]:
        pos1 = self.randomize_position()
        pos2 = self.randomize_position()

        while pos1 == pos2:  # Ensure the positions are distinct
            pos2 = self.randomize_position()
        return pos1, pos2

    def print_board(self, board: list[list[int]]):
        self.clear()
        print("-" * 10)
        for row in board:
            for cell in row:
                print(" " if cell == EMPTY_CELL else cell, sep="|", end=" ")
            print()
        print("-" * 10)
        print()

    def get_move_input(self) -> str:
        move = input("Enter the next move (W/A/S/D): ").upper()
        while move.upper() not in ["W", "A", "S", "D"]:
            move = input("Invalid move. Please enter W/A/S/D:").upper()
        return move

    def check_for_empty_cells(self) -> bool:
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.board[i][j] == 0:
                    return True
        return False

    def insert_new_number(self):
        if self.check_for_empty_cells():
            pos = self.randomize_position()
            while self.board[pos[0]][pos[1]] != EMPTY_CELL:
                pos = self.randomize_position()
            self.board[pos[0]][pos[1]] = self.randomize_new_number()
            return
        self.has_lost = True

    def clear(
        self,
    ):
        os.system("clear")

    def rotate_matrix_90_clockwise(self, matrix) -> list[list[int]]:
        transposed_matrix = list(zip(*matrix))
        rotated_matrix = [list(reversed(row)) for row in transposed_matrix]
        return rotated_matrix

    def rotate_matrix_90_counterclockwise(self, matrix) -> list[list[int]]:
        """Rotate the matrix 90 degrees counterclockwise."""
        transposed_matrix = list(zip(*matrix))
        rotated_matrix = transposed_matrix[::-1]
        return [list(row) for row in rotated_matrix]

    def move_logic(self, board: list[list[int]]) -> list[list[int]]:
        for row in range(BOARD_SIZE - 2, -1, -1):  # traverse rows from bottom to top
            for col in range(BOARD_SIZE):
                if board[row][col] == EMPTY_CELL:
                    continue
                non_empty_cells_in_col = [
                    i for i in range(row + 1, BOARD_SIZE) if board[i][col] != EMPTY_CELL
                ]
                if len(non_empty_cells_in_col) > 0:
                    next_non_empty_cell_in_col = min(non_empty_cells_in_col)
                    if board[next_non_empty_cell_in_col][col] == board[row][col]:
                        # merge values
                        new_value = board[next_non_empty_cell_in_col][col] * 2
                        board[next_non_empty_cell_in_col][col] = new_value
                        board[row][col] = EMPTY_CELL
                        self.has_won = new_value == WINNING_CELL
                    else:
                        board[next_non_empty_cell_in_col - 1][col] = board[row][col]
                        if next_non_empty_cell_in_col - 1 > row:
                            board[row][col] = EMPTY_CELL
                else:
                    next_cell_row = max([i for i in range(row + 1, BOARD_SIZE)])
                    board[next_cell_row][col] = board[row][col]
                    board[row][col] = EMPTY_CELL
        return board


def main():
    game = Game()


if __name__ == "__main__":
    main()

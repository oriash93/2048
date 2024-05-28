import os
import random

BOARD_SIZE = 4
EMPTY_CELL = 0
WINNING_CELL = 2048
POSSIBLE_NEW_NUMBERS = [2, 4]


def init_board() -> list[list[int]]:
    board = [[EMPTY_CELL] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    pos1, pos2 = randomize_initial_positions()
    board[pos1[0]][pos1[1]] = randomize_new_number()
    board[pos2[0]][pos2[1]] = randomize_new_number()
    return board


def randomize_new_number() -> int:
    return random.choice(POSSIBLE_NEW_NUMBERS)


def randomize_position() -> tuple[int, int]:
    return (random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1))


def randomize_initial_positions() -> tuple[tuple[int, int], tuple[int, int]]:
    pos1 = randomize_position()
    pos2 = randomize_position()

    while pos1 == pos2:  # Ensure the positions are distinct
        pos2 = randomize_position()
    return pos1, pos2


def print_board(board: list[list[int]]):
    for row in board:
        for cell in row:
            if cell == EMPTY_CELL:
                print(" ", end=" ")
            else:
                print(cell, end=" ")
        print()
    print()


def get_move_input() -> str:
    move = input("Enter the next move (W/A/S/D):\n").upper()
    while move not in ["W", "A", "S", "D"]:
        move = input("Invalid move. Please enter W/A/S/D:")
    return move


def insert_new_number(board: list[list[int]]):
    pos = randomize_position()
    while board[pos[0]][pos[1]] != EMPTY_CELL:
        pos = randomize_position()
    board[pos[0]][pos[1]] = randomize_new_number()


# def old_logic(board, move):
#     if move == "W":
#         row = None
#         while row == None:
#             col = random.randint(0, BOARD_SIZE - 1)
#             empty_cells = [
#                 i for i in range(0, BOARD_SIZE) if board[i][col] == EMPTY_CELL
#             ]
#             if len(empty_cells):
#                 row = min(empty_cells)
#     elif move == "A":
#         pass
#     elif move == "S":
#         pass
#     elif move == "D":
#         row = None
#         while row == None:
#             col = random.randint(0, BOARD_SIZE - 1)
#             empty_cells = [
#                 i for i in range(0, BOARD_SIZE) if board[i][col] == EMPTY_CELL
#             ]
#             if len(empty_cells):
#                 row = min(empty_cells)


def clear_board():
    os.system("clear")


def main():
    win = False
    lose = False
    board = init_board()
    while not win and not lose:
        print_board(board)
        move = get_move_input()
        if move == "W":
            for row in range(BOARD_SIZE - 1, 0, -1):  # merge rows from bottom to top
                lower_row = board[row]
                upper_row = board[row - 1]
                for col in range(BOARD_SIZE):
                    if upper_row[col] == EMPTY_CELL:
                        upper_row[col] = lower_row[col]
                        lower_row[col] = EMPTY_CELL
                    elif upper_row[col] == lower_row[col]:
                        upper_row[col] *= 2
                        lower_row[col] = EMPTY_CELL
                        win = upper_row[col] == WINNING_CELL
                board[row] = lower_row
                board[row - 1] = upper_row
            insert_new_number(board)

        elif move == "A":
            pass

        elif move == "S":
            pass

        elif move == "D":
            for row in range(BOARD_SIZE - 1):  # merge rows from top to bottom
                upper_row = board[row]
                lower_row = board[row + 1]
                for col in range(BOARD_SIZE):
                    if lower_row[col] == EMPTY_CELL:
                        lower_row[col] = upper_row[col]
                        upper_row[col] = EMPTY_CELL
                    elif lower_row[col] == upper_row[col]:
                        lower_row[col] *= 2
                        upper_row[col] = EMPTY_CELL
                        win = upper_row[col] == WINNING_CELL
                board[row] = upper_row
                board[row + 1] = lower_row
            insert_new_number(board)

        # clear_board()


if __name__ == "__main__":
    main()

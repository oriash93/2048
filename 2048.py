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
    print("-" * 10)
    for row in board:
        for cell in row:
            print(" " if cell == EMPTY_CELL else cell, sep="|", end=" ")
        print()
    print("-" * 10)
    print()


def get_move_input() -> str:
    move = input("Enter the next move (W/A/S/D): ").upper()
    while move not in ["W", "A", "S", "D"]:
        move = input("Invalid move. Please enter W/A/S/D:")
    return move


def check_for_empty_cells(board: list[list[int]]) -> bool:
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == 0:
                return True
    return False


def insert_new_number(board: list[list[int]]) -> bool:
    if check_for_empty_cells(board):
        pos = randomize_position()
        while board[pos[0]][pos[1]] != EMPTY_CELL:
            pos = randomize_position()
        board[pos[0]][pos[1]] = randomize_new_number()
        return True
    return False


def clear():
    os.system("clear")


def main():
    is_winning_cell = False
    is_board_full = False
    board = init_board()
    while not is_winning_cell and not is_board_full:
        clear()
        print_board(board)
        move = get_move_input()

        if move == "W":
            pass

        elif move == "A":
            pass

        elif move == "D":
            pass

        elif move == "S":
            for row in range(
                BOARD_SIZE - 2, -1, -1
            ):  # traverse rows from bottom to top
                for col in range(BOARD_SIZE):
                    if board[row][col] == EMPTY_CELL:
                        continue
                    non_empty_cells_in_col = [
                        i
                        for i in range(row + 1, BOARD_SIZE)
                        if board[i][col] != EMPTY_CELL
                    ]
                    if len(non_empty_cells_in_col) > 0:
                        next_non_empty_cell_in_col = min(non_empty_cells_in_col)
                        if board[next_non_empty_cell_in_col][col] == board[row][col]:
                            # merge values
                            new_value = board[next_non_empty_cell_in_col][col] * 2
                            board[next_non_empty_cell_in_col][col] = new_value
                            board[row][col] = EMPTY_CELL
                            is_winning_cell = new_value == WINNING_CELL
                        else:
                            board[next_non_empty_cell_in_col - 1][col] = board[row][col]
                            if next_non_empty_cell_in_col - 1 > row:
                                board[row][col] = EMPTY_CELL
                    else:
                        next_cell_row = max([i for i in range(row + 1, BOARD_SIZE)])
                        board[next_cell_row][col] = board[row][col]
                        board[row][col] = EMPTY_CELL

        is_board_full = not insert_new_number(board)

    if is_winning_cell:
        print("congrats! you won :)")
    elif is_board_full:
        print("game over :(")


if __name__ == "__main__":
    main()

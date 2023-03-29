import numpy as np
from numpy import random, resize


def build_board(size):
    board = random.choice(['Empty', 'Red', 'Black'], size=(size, size))
    return board


def get_count(board, item):
    count = 0
    for row in board:
        for column in row:
            if column == item:
                count += 1
    return count


def resize_board(board, new_size):
    new_board = resize(board, (new_size, new_size))
    return new_board


def pivot_board(board):
    pivoted_board = np.empty((board.shape[1], board.shape[0]), dtype=board.dtype)
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            pivoted_board[j][i] = board[i][j]
    return pivoted_board





if __name__ == '__main__':
    print("This file is not intended to be run as a main file.")

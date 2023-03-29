import numpy as np
from numpy import random, count_nonzero, resize


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
    n = board.shape[0]
    new_board = np.empty(board)
    for i in range(n):
        for j in range(n):
            new_board[i][j] = board[j][i]
    return new_board


if __name__ == '__main__':
    print("This file is not intended to be run as a main file.")

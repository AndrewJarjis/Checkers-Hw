import checkers


def game():
    size = int(input("Enter board size (minimum of 4, maximum of 16): "))
    if size < 4 or size > 16:
        print("Invalid board size.")
        return

    board = checkers.build_board(size)

    print(board)

    empty_count = checkers.get_count(board, 'Empty')
    red_count = checkers.get_count(board, 'Red')
    black_count = checkers.get_count(board, 'Black')

    print("Empty cells: ", empty_count)
    print("Red checkers: ", red_count)
    print("Black checkers: ", black_count)


if __name__ == '__main__':
    game()

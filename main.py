from lib.board import Board
from copy import deepcopy

def find_all_victories(board, solutions=[]):
    if board.last_placed_piece == 9:
        solutions.append(board.plays[:])
        return

    for start in board.available_paths:
        for end in board.available_paths[start]:
            new_board = deepcopy(board)
            if new_board.place_piece(start, end):
                find_all_victories(new_board, solutions)

    return solutions


if __name__ == '__main__':
    initialBoard = Board()
    victories = find_all_victories(initialBoard)

    print(f'Total victories found {len(victories)}')

    for v in victories:
        print(v)

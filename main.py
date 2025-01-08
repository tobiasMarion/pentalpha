from lib.board import Board
from lib.tree import Node, writeTreeToFile
from copy import deepcopy

def find_all_victories(board, parent_node, solutions=[]):
    if board.last_placed_piece == 9:
        solutions.append(board.plays[:])
        return True

    found_victory = False
    for start in board.available_paths:
        for end in board.available_paths[start]:
            new_board = deepcopy(board)
            if new_board.place_piece(start, end):
                node = Node((start, end))
                child_win = find_all_victories(new_board, node, solutions)

                if child_win:
                    parent_node.add_child(node)
                    found_victory = True

    return found_victory


if __name__ == '__main__':
    initialBoard = Board()
    root = Node()
    wins = []
    find_all_victories(initialBoard, root, wins)

    print(f'Total victories found {len(wins)}')

    for w in wins:
        print(w)

    with open("tree_output.txt", "w") as file:
        writeTreeToFile(root, file)

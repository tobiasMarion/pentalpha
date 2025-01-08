PATHS = {
    'A': ['C', 'F'],
    'E': ['D', 'G'],
    'I': ['B', 'F'],
    'O': ['C', 'G'],
    'U': ['D', 'B'],
    'B': ['I', 'U'],
    'C': ['A', 'O'],
    'D': ['E', 'U'],
    'F': ['A', 'I'],
    'G': ['E', 'O'],
}


class Board:
    def __init__(self):
        self.last_placed_piece = 0
        self.available_paths = PATHS
        self.vertices = {}
        self.plays = []

        for v in PATHS.keys():
            self.vertices[v] = 0

    def is_play_valid(self, to_place, to_move):
        if self.vertices[to_place] != 0:
            return False

        if self.vertices[to_move] != 0:
            return False

        if to_move not in self.available_paths[to_place]:
            return  False

        return  True

    def place_piece(self, initial, moved_to):
        if not self.is_play_valid(initial, moved_to):
            return False

        self.last_placed_piece += 1
        self.vertices[moved_to] = self.last_placed_piece

        for neighbor in self.available_paths[moved_to]:
            self.available_paths[neighbor].remove(moved_to)

        self.available_paths[moved_to] = []

        self.plays.append((initial, moved_to))
        return True
from copy import deepcopy

class Board:
    def __init__(self):
        self.board = []
        self.rows = 6
        self.columns = 7
        for r in range(self.rows):
            row = []
            for c in range(self.columns):
                row.append("")

    def copyBoard(self):
        return deepcopy(self.board)

from copy import deepcopy

class Board:
    def __init__(self):
        self.board = []
<<<<<<< HEAD
        self.rows = 6
        self.columns = 7
        for r in range(self.rows):
            row = []
            for c in range(self.columns):
                row.append("")

    def copyBoard(self):
        return deepcopy(self.board)
=======
        for _ in range(6):
            for _ in range(7):
                
>>>>>>> 66ba5311eaf429b5210f4e3a121e1a25cca585eb

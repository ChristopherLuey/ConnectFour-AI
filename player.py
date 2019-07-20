class Player:
    def __init__(self, piece = "X"):
        self.piece = piece

    def Col(self):
        return int(input("What column to place?"))

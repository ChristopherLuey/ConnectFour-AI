class Player:
    def __init__(self, piece = "X"):
        self.piece = piece

    def Col(self):
        try:
            in1 = int(input("What column to place? "))

            if 1 <= in1 < 8:
                return in1 -1
            else:
                print("Choose a new column")
                return self.Col()
        except:
            return self.Col()

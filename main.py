import Board
import player

def main():
    p = player.Player()
    p2 = player.Player("o")
    board = Board.Board()
    win = False
    turn = p

    while(not win):
        board.printBoard()
        col = turn.Col()
        row = board.findRow(col)
        board.placePiece(row, col, turn)
        if(board.win(row, col, turn) == True):
            win = True;
        if(turn == p):
            turn = p2
        elif(turn == p2):
            turn = p


if __name__ == "__main__":
  main()

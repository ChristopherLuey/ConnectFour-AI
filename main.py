import Board
import player
import tensorflow as tf

def main():
    p = player.Player()
    p2 = player.Player("0")
    board = Board.Board()
    win = False
    turn = p
    board.printBoard()

    while(not win):
        col = turn.Col()
        row = board.findRow(col)
        if (row > 5):
            print("Choose a different column")
            continue
        board.placePiece(row, col, turn)
        if(board.win(row, col, turn) == True):
            win = True;
        if(turn == p):
            turn = p2
        elif(turn == p2):
            turn = p
        board.printBoard()
    print("win")


if __name__ == "__main__":
  main()

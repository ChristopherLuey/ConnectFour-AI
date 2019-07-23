from __future__ import absolute_import, division, print_function, unicode_literals

import Board
import player
import tensorflow as tf
import random

def main():

    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(1,42)),
        tf.keras.layers.Dense(28, activation=tf.nn.relu),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(7, activation=tf.nn.softmax)
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model2 = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(1,42)),
        tf.keras.layers.Dense(28, activation=tf.nn.relu),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(7, activation=tf.nn.softmax)
    ])
    model2.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    mnist = tf.keras.datasets.mnist

    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    # print(x_test)
    # print(x_train)
    # print(y_test)
    # print(y_train)
    idk2 = []
    idk7 = []

    # [[],[],]
    for k in range(7):
        idk5 = []
        for i in range(1):
            idk4 = []
            for j in range(42):
                idk4.append(random.randint(1,3)*0.3)
                print(random.randint(1,3)*0.3)

            idk5.append(idk4)
        idk2.append(idk5)
    idk7.append(idk2)


    idk3 = [random.randint(0,6)for i in range(7)]


    # model.evaluate(idk3, idk2)
    model.fit(idk7, idk3, epochs=100)
    model2.fit(idk7, idk3, epochs=100)
    model.evaluate(idk7, idk3)

    # model2.fit(x_train, y_train, epochs=5)

    for i in range(100):
        p = player.Player()
        p2 = player.Player("0")
        board = Board.Board()
        win = False
        turn = p
        modelV = model
        board.printBoard()
        idk = [0.0 for i in range(42)]

        while(not win):
            for i in range(board.rows):
                for a in range(board.columns):
                    idk[i*a+a] = board.getValue(i, a, p, p2)

            but = []
            final = []
            for k in range(7):
                z = []
                z.append(idk)
                but.append(z)
            final.append(but)
            idk3 = [random.randint(0, 6) for i in range(7)]

            print(modelV.evaluate(final, idk3))



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

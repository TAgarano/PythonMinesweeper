#
# Minesweeper with 3 levels
# Practice: allows you to clear board without ending on a mine
# Intermediate: gives you 3 lives to clear the board
# Hard: typical minesweeper, one life
#
# Created by: Travis A, Andrew H, Matthew P
#

import random
from tkinter import *


# everything that goes into the window
def create_window(window):

    # titles window Minesweeper
    window.title("Minesweeper")

    # cannot resize window, dim 550x700, starts at 50, 50 on screen
    window.resizable(width=FALSE, height=FALSE)
    window.geometry('554x691+50+50')

    # place and create buttons
    practice_btn = Button(window, text="Practice", width=25, height=2).place(x=1, y=650)
    intermediate_btn = Button(window, text="Intermediate", width=25, height=2).place(x=185, y=650)
    hard_btn = Button(window, text="Hard", width=25, height=2).place(x=369, y=650)

    # lives label
    lives_lbl = Label(window, text="Lives: ", font="Times 16 bold", bg="darkgray").place(x=20, y=604)


def create_board(board):

    # creates the background of the gameboard
    board.create_rectangle(10, 10, 544, 641, outline='gray', fill='darkgray', width = 10)
    board.create_rectangle(10, 590, 544, 600, outline='gray', fill='gray')


def main():

    # creates window
    window = Tk()

    # creates space for objects to be placed on the window
    board = Canvas(window, width=550, height=700)
    board.pack()

    create_window(window)
    create_board(board)

    window.mainloop()


if __name__ == "__main__":
    main()

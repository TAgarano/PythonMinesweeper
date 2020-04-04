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

    # lives labels
    lives_lbl = Label(window, text="Lives: ", font="Times 16 bold", bg="darkgray").place(x=28, y=604)
    active_lives = Label(window, text="0", font="Times 16 bold", bg="darkgray").place(x=87, y=604)


def create_board(board):

    # creates the background of the gameboard
    board.create_rectangle(10, 10, 544, 641, outline='gray', fill='darkgray', width=36)
    board.create_rectangle(10, 590, 545, 603, outline='gray', fill='gray')
    board.create_rectangle(30, 620, 525, 633, outline='darkgray', fill='darkgray')


def button_grid(window):

    # creates grid of buttons, dim 11x14
    x = 29
    while x <= 500:
        y = 29
        while y <= 550:
            button1 = Button(window, width=5, height=2, bg='gray').place(x=x, y=y)
            y = y + 40
        x = x + 45


def main():

    # creates window
    window = Tk()

    # creates space for objects to be placed on the window
    board = Canvas(window, width=550, height=700)
    board.pack()

    create_window(window)
    create_board(board)
    button_grid(window)

    window.mainloop()


if __name__ == "__main__":
    main()

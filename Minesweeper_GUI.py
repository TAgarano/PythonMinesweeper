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
def create_window():
    # Creates window
    window = Tk()

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
    lives_lbl = Label(window, text="Lives: ", font="Times 16 bold").place(x=5, y=610)

    window.mainloop()


def main():
    create_window()


if __name__ == "__main__":
    main()

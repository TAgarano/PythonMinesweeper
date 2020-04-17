#
# Minesweeper with 3 levels
# Practice: allows you to clear board without ending on a mine
# Intermediate: gives you 3 lives to clear the board
# Hard: typical minesweeper, one life
#
# Created by: Travis A, Andrew H, Matthew P
#

from tkinter import *
from Minesweeper_mines import *

# button_locations0 = [[Button for i in range(11)] for j in range(11)]
button_locations1 = []


# everything that goes into the window
def create_window():
    # creates window
    window = Tk()

    # titles window Minesweeper
    window.title("Minesweeper")

    frame = Frame(window, background='dark gray')

    frame.pack(side='top', fill='both', expand='true')

    # cannot resize window, dim 550x700, starts at 50, 50 on screen
    window.resizable(width=FALSE, height=FALSE)
    window.geometry('554x585+50+50')

    return window, frame


def create_board(window):
    # creates space for objects to be placed on the window
    board = Canvas(window, width=550, height=700)
    board.pack()

    # creates the background of the gameboard
    board.create_rectangle(10, 10, 544, 641, outline='gray', fill='darkgray', width=36)
    board.create_rectangle(10, 590, 544, 471, outline='gray', fill='gray')
    board.create_rectangle(27, 525, 525, 480, outline='darkgray', fill='darkgray')

    # place and create buttons
    practice_btn = Button(window, text="Practice", width=25, height=2).place(x=1, y=550)
    intermediate_btn = Button(window, text="Intermediate", width=25, height=2).place(x=185, y=550)
    hard_btn = Button(window, text="Hard", width=25, height=2).place(x=369, y=550)

    # lives labels
    lives_lbl = Label(window, text="Lives: ", font="Times 16 bold", bg="darkgray").place(x=28, y=490)
    active_lives = Label(window, text="0", font="Times 16 bold", bg="darkgray").place(x=87, y=490)


def button_grid(frame):
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_columnconfigure(1, weight=1)

    column = 0

    while column < 11:
        row = 0
        while row < 11:
            button = Button(frame, width=5, height=2, bg='gray')
            button.grid(row=row, column=column)
            row += 1
        column += 1


# TODO: hide button || change button text
def clicked(event):
    x = button_locations1.index(event)
    button_locations1[x].place_forget()


def main():
    # creates window
    window, frame = create_window()

    # creates map to be "linked" with buttons
    create_map()

    create_board(window)
    button_grid(frame)

    window.mainloop()


if __name__ == "__main__":
    main()

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
def create_window(window):
    # titles window Minesweeper
    window.title("Minesweeper")

    # cannot resize window, dim 550x700, starts at 50, 50 on screen
    window.resizable(width=FALSE, height=FALSE)
    window.geometry('554x585+50+50')

    # place and create buttons
    practice_btn = Button(window, text="Practice", width=25, height=2).place(x=1, y=550)
    intermediate_btn = Button(window, text="Intermediate", width=25, height=2).place(x=185, y=550)
    hard_btn = Button(window, text="Hard", width=25, height=2).place(x=369, y=550)

    # lives labels
    lives_lbl = Label(window, text="Lives: ", font="Times 16 bold", bg="darkgray").place(x=28, y=490)
    active_lives = Label(window, text="0", font="Times 16 bold", bg="darkgray").place(x=87, y=490)


def create_board(board):
    # creates the background of the gameboard
    board.create_rectangle(10, 10, 544, 641, outline='gray', fill='darkgray', width=36)
    board.create_rectangle(10, 590, 544, 471, outline='gray', fill='gray')
    board.create_rectangle(27, 525, 525, 480, outline='darkgray', fill='darkgray')


def button_grid(window):
    # global button_locations
    global button_locations1

    # creates grid of buttons & labels, dim 11x11
    x = 29
    while x < 500:
        y = 29
        while y < 450:
            elements = Label(window, text=field[int((x - 29) / 45)][int((y - 29) / 40)], font="Times 16 bold",
                             fg="black", bg="darkgray").place(x=x + 13, y=y + 5)

            button = Button(window, width=5, height=2, bg='gray',  command=lambda: clicked(button))

            # FIXME: Tried 2 ways of adding button to a list
#            button_locations0[int((x - 29) / 45)][int((y - 29) / 40)] = button
            button_locations1.append(button)
            button.place(x=x, y=y)
            y = y + 40
        x = x + 45
    # FIXME: Last position of x & y are passed in for function "clicked"
    # FIXME: can test with below values
    # y = 0
    # x = 0


# TODO: hide button || change button text
def clicked(event):
    x = button_locations1.index(event)
    button_locations1[x].place_forget()


def main():
    # creates window
    window = Tk()

    # creates map to be "linked" with buttons
    create_map()

    # creates space for objects to be placed on the window
    board = Canvas(window, width=550, height=700)
    board.pack()

    create_window(window)
    create_board(board)
    button_grid(window)

    window.mainloop()


if __name__ == "__main__":
    main()
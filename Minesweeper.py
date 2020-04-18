#
# Minesweeper with 3 levels
# Practice: allows you to clear board without ending on a mine
# Intermediate: gives you 3 lives to clear the board
# Hard: typical minesweeper, one life
#
# Created by: Travis A, Andrew H, Matthew P
#

#
# imports
#
import random as r
from tkinter import *

#
# GLOBALS
#
# list of buttons
button_locations = []

# list for the map
field = [[0 for i in range(11)] for j in range(11)]

# mine count
num_mines = 18


# used to place the mines
def mines():
    global field

    i = 0
    while i != num_mines:
        x = r.randint(0, 10)
        y = r.randint(0, 10)

        # place mine
        if field[x][y] != 9:
            field[x][y] = 9
            i += 1


# increment numbers around mines
def increment_neighbors():
    global field

    for row in range(len(field)):
        for col in range(len(field[row])):
            # mine
            if field[row][col] == 9:

                # To the right
                if col + 1 < len(field) and field[row][col + 1] != 9:
                    field[row][col + 1] += 1

                # Below the mine
                if row + 1 < len(field) and field[row + 1][col] != 9:
                    field[row + 1][col] += 1

                # Above the mine
                if row - 1 >= 0 and field[row - 1][col] != 9:
                    field[row - 1][col] += 1

                # To the left
                if col - 1 >= 0 and field[row][col - 1] != 9:
                    field[row][col - 1] += 1

                # Down right
                if row + 1 < len(field) and col + 1 < len(field[row]) and field[row + 1][col + 1] != 9:
                    field[row + 1][col + 1] += 1

                # Up right
                if row - 1 >= 0 and col + 1 < len(field[row]) and field[row - 1][col + 1] != 9:
                    field[row - 1][col + 1] += 1

                # Up left
                if row - 1 >= 0 and col - 1 >= 0 and field[row - 1][col - 1] != 9:
                    field[row - 1][col - 1] += 1

                # Down left
                if row + 1 < len(field) and col - 1 >= 0 and field[row + 1][col - 1] != 9:
                    field[row + 1][col - 1] += 1


# text based map for testing
def print_map():
    for i in range(len(field)):
        print(field[i])
    print()


# adds mines and the numbers to list: fields
def create_map():
    mines()
    increment_neighbors()
    print_map()


# everything that goes into the window
def create_window():
    # creates window
    window = Tk()

    # titles window Minesweeper
    window.title("Minesweeper")

    # cannot resize window, dim 550x700, starts at 50, 50 on screen
    window.resizable(width=FALSE, height=FALSE)
    window.geometry('554x585+50+50')

    return window


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


def button_grid(window):
    # list of buttons
    global button_locations

    # button id
    id = 0

    # creates grid of buttons & labels, dim 11x11
    x = 29
    while x < 500:
        y = 29
        print(field[int((x - 29) / 45)])
        while y < 450:
            elements = Label(window, text=field[int((y - 29) / 40)][int((x - 29) / 45)], font="Times 16 bold",
                             fg="black", bg="darkgray").place(x=x + 13, y=y + 5)

            button = Button(window, width=5, height=2, bg='gray', command=lambda c=str(id): clicked(c))

            button_locations.append(button)
            button.place(x=x, y=y)
            id += 1
            y = y + 40
        x = x + 45


def clicked(index):
    button_locations[int(index)]["state"] = DISABLED
    button_locations[int(index)].place_forget()

    # Button above
    if (int(index) - 1) % 11 <= 9 and int(index) - 1 < 121 and field[int(index) % 11][int(int(index) / 11)] == 0\
            and button_locations[int(index) - 1]["state"] == NORMAL:
        clicked(int(index) - 1)

    # Button left
    if int(index) - 11 > 0 and field[int(index) % 11][int(int(index) / 11)] == 0\
            and button_locations[int(index) - 11]["state"] == NORMAL:
        clicked(int(index) - 11)

    # Button down
    if (int(index) + 1) % 11 != 0 and field[int(index) % 11][int(int(index) / 11)] == 0\
            and button_locations[int(index) + 1]["state"] == NORMAL:
        clicked(int(index) + 1)

    # Button right
    if int(index) + 11 < 121 and field[int(index) % 11][int(int(index) / 11)] == 0\
            and button_locations[int(index) + 11]["state"] == NORMAL:
        clicked(int(index) + 11)

    # Button right/down
    if int(index) + 12 < 121 and (int(index) + 12) % 11 != 0 and field[int(index) % 11][int(int(index) / 11)] == 0\
            and button_locations[int(index) + 12]["state"] == NORMAL:
        clicked(int(index) + 12)

    # Button right/up
    if (int(index) + 10) % 11 != 10 and int(index) + 10 < 121 and field[int(index) % 11][int(int(index) / 11)] == 0 \
            and button_locations[int(index) + 10]["state"] == NORMAL:
        clicked(int(index) + 10)

    # Button left/up
    if int(index) - 12 > 0 and (int(index) + 10) % 11 != 10 and field[int(index) % 11][int(int(index) / 11)] == 0\
            and button_locations[int(index) - 12]["state"] == NORMAL:
        clicked(int(index) - 12)

    # Button left/down
    if int(index) - 10 > 0 and (int(index) + 12) % 11 != 0 and field[int(index) % 11][int(int(index) / 11)] == 0\
            and button_locations[int(index) - 10]["state"] == NORMAL:
        clicked(int(index) - 10)


def main():
    # creates window
    window = create_window()

    create_map()

    # creates map to be "linked" with buttons
    create_board(window)
    button_grid(window)

    window.mainloop()


if __name__ == "__main__":
    main()

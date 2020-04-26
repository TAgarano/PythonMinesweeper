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
start_buttons = []
# window
window = Tk()


class Mines(object):
    # list for the map
    field = [[0 for i in range(11)] for j in range(11)]
    # number of mines
    num_mines = 18

    # used to place the mines
    def set_mines(self):
        i = 0
        while i != Mines.num_mines:
            x = r.randint(0, 10)
            y = r.randint(0, 10)

            # place mine
            if Mines.field[x][y] != 9:
                Mines.field[x][y] = 9
                i += 1

    # increment numbers around mines
    def increment_neighbors(self):
        for row in range(len(Mines.field)):
            for col in range(len(Mines.field[row])):

                # mine
                if Mines.field[row][col] == 9:

                    # To the right
                    if col + 1 < len(Mines.field) and Mines.field[row][col + 1] != 9:
                        Mines.field[row][col + 1] += 1

                    # Below the mine
                    if row + 1 < len(Mines.field) and Mines.field[row + 1][col] != 9:
                        Mines.field[row + 1][col] += 1

                    # Above the mine
                    if row - 1 >= 0 and Mines.field[row - 1][col] != 9:
                        Mines.field[row - 1][col] += 1

                    # To the left
                    if col - 1 >= 0 and Mines.field[row][col - 1] != 9:
                        Mines.field[row][col - 1] += 1

                    # Down right
                    if row + 1 < len(Mines.field) and col + 1 < len(Mines.field[row]) and Mines.field[row + 1][col + 1] != 9:
                        Mines.field[row + 1][col + 1] += 1

                    # Up right
                    if row - 1 >= 0 and col + 1 < len(Mines.field[row]) and Mines.field[row - 1][col + 1] != 9:
                        Mines.field[row - 1][col + 1] += 1

                    # Up left
                    if row - 1 >= 0 and col - 1 >= 0 and Mines.field[row - 1][col - 1] != 9:
                        Mines.field[row - 1][col - 1] += 1

                    # Down left
                    if row + 1 < len(Mines.field) and col - 1 >= 0 and Mines.field[row + 1][col - 1] != 9:
                        Mines.field[row + 1][col - 1] += 1

    # text based map
    def print_map(self):
        for i in range(len(Mines.field)):
            print(Mines.field[i])
        print()

    # adds mines and the numbers to list: fields
    def create_map(self):
        Mines.set_mines(self)
        Mines.increment_neighbors(self)
        Mines.print_map(self)


class Window(object):

    # everything that goes into the window
    def create_window(self, win):
        # titles window Minesweeper
        win.title("Minesweeper")

        # cannot resize window, dim 550x700, starts at 50, 50 on screen
        win.resizable(width=FALSE, height=FALSE)
        win.geometry('554x585+50+50')

        return win

    def create_board(self, win):
        c = Commands()

        # creates space for objects to be placed on the window
        board = Canvas(window, width=550, height=700)
        board.pack()

        # creates the background of the gameboard
        board.create_rectangle(10, 10, 544, 641, outline='gray', fill='darkgray', width=36)
        board.create_rectangle(10, 590, 544, 471, outline='gray', fill='gray')
        board.create_rectangle(27, 525, 525, 480, outline='darkgray', fill='darkgray')

        # place and create buttons
        practice_btn = Button(win, text="Practice", width=25, height=2,
                              command=lambda m=str(300): c.practice(m))
        start_buttons.append(practice_btn)
        practice_btn.place(x=1, y=550)

        intermediate_btn = Button(win, text="Intermediate", width=25, height=2,
                                  command=lambda m=str(301): c.intermediate(m))
        start_buttons.append(intermediate_btn)
        intermediate_btn.place(x=185, y=550)

        hard_btn = Button(win, text="Hard", width=25, height=2, command=lambda m=str(302): c.hard(m))
        start_buttons.append(hard_btn)
        hard_btn.place(x=369, y=550)

        # lives label
        lives_lbl = Label(win, text="Lives: ", font="Times 16 bold", bg="darkgray").place(x=28, y=490)


def button_grid(win):
    # list of buttons
    global button_locations
    com = Commands()

    # button id
    id = 0

    # creates grid of buttons & labels, dim 11x11
    x = 29
    while x < 500:
        y = 29
        print(Mines.field[int((x - 29) / 45)])
        while y < 450:
            if Mines.field[int((y - 29) / 40)][int((x - 29) / 45)] == 9:
                elements = Label(win, text="*", font="Times 16 bold",
                                 fg="black", bg="darkgray").place(x=x + 13, y=y + 11)
            else:
                elements = Label(win, text=Mines.field[int((y - 29) / 40)][int((x - 29) / 45)], font="Times 16 bold",
                                 fg="black", bg="darkgray").place(x=x + 13, y=y + 5)

            button = Button(win, width=5, height=2, bg='gray', command=lambda c=str(id): com.clicked(c))

            button_locations.append(button)
            button.place(x=x, y=y)
            id += 1
            y = y + 40
        x = x + 45


class Commands(object):
    spaces = 121 - Mines.num_mines
    active_lives = Label(window)

    def clicked(self, index):
        button_locations[int(index)]["state"] = DISABLED
        button_locations[int(index)].place_forget()

        Commands.remove_space(self)
        # Button above
        if (int(index) - 1) % 11 <= 9 and int(index) - 1 < 121 and\
                Mines.field[int(index) % 11][int(int(index) / 11)] == 0\
                and button_locations[int(index) - 1]["state"] == NORMAL:
            Commands.clicked(self, int(index) - 1)

        # Button left
        if int(index) - 11 > 0 and Mines.field[int(index) % 11][int(int(index) / 11)] == 0\
                and button_locations[int(index) - 11]["state"] == NORMAL:
            Commands.clicked(self, int(index) - 11)

        # Button down
        if (int(index) + 1) % 11 != 0 and Mines.field[int(index) % 11][int(int(index) / 11)] == 0\
                and button_locations[int(index) + 1]["state"] == NORMAL:
            Commands.clicked(self, int(index) + 1)

        # Button right
        if int(index) + 11 < 121 and Mines.field[int(index) % 11][int(int(index) / 11)] == 0\
                and button_locations[int(index) + 11]["state"] == NORMAL:
            Commands.clicked(self, int(index) + 11)

        # Button right/down
        if int(index) + 12 < 121 and (int(index) + 12) % 11 != 0 and\
                Mines.field[int(index) % 11][int(int(index) / 11)] == 0\
                and button_locations[int(index) + 12]["state"] == NORMAL:
            Commands.clicked(self, int(index) + 12)

        # Button right/up
        if (int(index) + 10) % 11 != 10 and int(index) + 10 < 121 and \
                Mines.field[int(index) % 11][int(int(index) / 11)] == 0 \
                and button_locations[int(index) + 10]["state"] == NORMAL:
            Commands.clicked(self, int(index) + 10)

        # Button left/up
        if int(index) - 12 > 0 and (int(index) + 10) % 11 != 10 and\
            Mines.field[int(index) % 11][int(int(index) / 11)] == 0\
                and button_locations[int(index) - 12]["state"] == NORMAL:
            Commands.clicked(self, int(index) - 12)

        # Button left/down
        if int(index) - 10 > 0 and (int(index) + 12) % 11 != 0 and\
            Mines.field[int(index) % 11][int(int(index) / 11)] == 0\
                and button_locations[int(index) - 10]["state"] == NORMAL:
            Commands.clicked(self, int(index) - 10)

    def practice(self, idx):
        mine_c = Mines()
        mine_c.create_map()

        Commands.active_lives = Label(window, text="99", font="Times 16 bold", bg="darkgray").place(x=88, y=490)

        # creates map to be "linked" with buttons
        button_grid(window)

        # disables other start buttons
        for i in range(len(start_buttons)):
            start_buttons[i]['state'] = DISABLED

    def intermediate(self, idx):
        mine_c = Mines()
        mine_c.create_map()

        Commands.active_lives = Label(window, text="3", font="Times 16 bold", bg="darkgray").place(x=88, y=490)

        # creates map to be "linked" with buttons
        button_grid(window)

        # disables other start buttons
        for i in range(len(start_buttons)):
            start_buttons[i]['state'] = DISABLED

    def hard(self, idx):
        mine_c = Mines()
        mine_c.create_map()

        Commands.active_lives = Label(window, text="1", font="Times 16 bold", bg="darkgray").place(x=88, y=490)

        # creates map to be "linked" with buttons
        button_grid(window)

        # disables other start buttons
        for i in range(len(start_buttons)):
            start_buttons[i]['state'] = DISABLED

    def remove_space(self):
        Commands.spaces -= 1

        if Commands.spaces == 0:
            for i in range(len(button_locations)):
                button_locations[i]['state'] = DISABLED

                
def main():
    global window

    # Window class
    screen = Window()
    screen.create_window(window)
    screen.create_board(window)

    window.mainloop()


if __name__ == "__main__":
    main()

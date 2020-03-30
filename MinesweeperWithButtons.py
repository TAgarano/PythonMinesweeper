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
    
    button1 = Button(board, text=" ", width=4, height=2).place(x=15, y=15)
    button2 = Button(board, text=" ", width=4, height=2).place(x=55, y=15)  
    button3 = Button(board, text=" ", width=4, height=2).place(x=95, y=15) 
    button4 = Button(board, text=" ", width=4, height=2).place(x=135, y=15)
    button5 = Button(board, text=" ", width=4, height=2).place(x=175, y=15) 
    button6 = Button(board, text=" ", width=4, height=2).place(x=215, y=15)
    button7 = Button(board, text=" ", width=4, height=2).place(x=255, y=15)
    button8 = Button(board, text=" ", width=4, height=2).place(x=295, y=15)
    button9 = Button(board, text=" ", width=4, height=2).place(x=335, y=15)
    button10 = Button(board, text=" ", width=4, height=2).place(x=375, y=15)
    
    button11 = Button(board, text=" ", width=4, height=2).place(x=15, y=50)
    button12 = Button(board, text=" ", width=4, height=2).place(x=55, y=50)  
    button13 = Button(board, text=" ", width=4, height=2).place(x=95, y=50) 
    button14 = Button(board, text=" ", width=4, height=2).place(x=135, y=50)
    button15 = Button(board, text=" ", width=4, height=2).place(x=175, y=50) 
    button16 = Button(board, text=" ", width=4, height=2).place(x=215, y=50)
    button17 = Button(board, text=" ", width=4, height=2).place(x=255, y=50)
    button18 = Button(board, text=" ", width=4, height=2).place(x=295, y=50)
    button19 = Button(board, text=" ", width=4, height=2).place(x=335, y=50)
    button20 = Button(board, text=" ", width=4, height=2).place(x=375, y=50)
    
    button21 = Button(board, text=" ", width=4, height=2).place(x=15, y=85)
    button22 = Button(board, text=" ", width=4, height=2).place(x=55, y=85)  
    button23 = Button(board, text=" ", width=4, height=2).place(x=95, y=85) 
    button24 = Button(board, text=" ", width=4, height=2).place(x=135, y=85)
    button25 = Button(board, text=" ", width=4, height=2).place(x=175, y=85) 
    button26 = Button(board, text=" ", width=4, height=2).place(x=215, y=85)
    button27 = Button(board, text=" ", width=4, height=2).place(x=255, y=85)
    button28 = Button(board, text=" ", width=4, height=2).place(x=295, y=85)
    button29 = Button(board, text=" ", width=4, height=2).place(x=335, y=85)
    button30 = Button(board, text=" ", width=4, height=2).place(x=375, y=85)
    
    button31 = Button(board, text=" ", width=4, height=2).place(x=15, y=120)
    button32 = Button(board, text=" ", width=4, height=2).place(x=55, y=120)  
    button33 = Button(board, text=" ", width=4, height=2).place(x=95, y=120) 
    button34 = Button(board, text=" ", width=4, height=2).place(x=135, y=120)
    button35 = Button(board, text=" ", width=4, height=2).place(x=175, y=120) 
    button36 = Button(board, text=" ", width=4, height=2).place(x=215, y=120)
    button37 = Button(board, text=" ", width=4, height=2).place(x=255, y=120)
    button38 = Button(board, text=" ", width=4, height=2).place(x=295, y=120)
    button39 = Button(board, text=" ", width=4, height=2).place(x=335, y=120)
    button40 = Button(board, text=" ", width=4, height=2).place(x=375, y=120)
    
    button41 = Button(board, text=" ", width=4, height=2).place(x=15, y=155)
    button42 = Button(board, text=" ", width=4, height=2).place(x=55, y=155)  
    button43 = Button(board, text=" ", width=4, height=2).place(x=95, y=155) 
    button44 = Button(board, text=" ", width=4, height=2).place(x=135, y=155)
    button45 = Button(board, text=" ", width=4, height=2).place(x=175, y=155) 
    button46 = Button(board, text=" ", width=4, height=2).place(x=215, y=155)
    button47 = Button(board, text=" ", width=4, height=2).place(x=255, y=155)
    button48 = Button(board, text=" ", width=4, height=2).place(x=295, y=155)
    button49 = Button(board, text=" ", width=4, height=2).place(x=335, y=155)
    button50 = Button(board, text=" ", width=4, height=2).place(x=375, y=155)
    
    button51 = Button(board, text=" ", width=4, height=2).place(x=15, y=190)
    button52 = Button(board, text=" ", width=4, height=2).place(x=55, y=190)  
    button53 = Button(board, text=" ", width=4, height=2).place(x=95, y=190) 
    button54 = Button(board, text=" ", width=4, height=2).place(x=135, y=190)
    button55 = Button(board, text=" ", width=4, height=2).place(x=175, y=190) 
    button56 = Button(board, text=" ", width=4, height=2).place(x=215, y=190)
    button57 = Button(board, text=" ", width=4, height=2).place(x=255, y=190)
    button58 = Button(board, text=" ", width=4, height=2).place(x=295, y=190)
    button59 = Button(board, text=" ", width=4, height=2).place(x=335, y=190)
    button60 = Button(board, text=" ", width=4, height=2).place(x=375, y=190)
    
    button61 = Button(board, text=" ", width=4, height=2).place(x=15, y=225)
    button62 = Button(board, text=" ", width=4, height=2).place(x=55, y=225)  
    button63 = Button(board, text=" ", width=4, height=2).place(x=95, y=225) 
    button64 = Button(board, text=" ", width=4, height=2).place(x=135, y=225)
    button65 = Button(board, text=" ", width=4, height=2).place(x=175, y=225) 
    button66 = Button(board, text=" ", width=4, height=2).place(x=215, y=225)
    button67 = Button(board, text=" ", width=4, height=2).place(x=255, y=225)
    button68 = Button(board, text=" ", width=4, height=2).place(x=295, y=225)
    button69 = Button(board, text=" ", width=4, height=2).place(x=335, y=225)
    button70 = Button(board, text=" ", width=4, height=2).place(x=375, y=225)
    
    button71 = Button(board, text=" ", width=4, height=2).place(x=15, y=260)
    button72 = Button(board, text=" ", width=4, height=2).place(x=55, y=260)  
    button73 = Button(board, text=" ", width=4, height=2).place(x=95, y=260) 
    button74 = Button(board, text=" ", width=4, height=2).place(x=135, y=260)
    button75 = Button(board, text=" ", width=4, height=2).place(x=175, y=260) 
    button76 = Button(board, text=" ", width=4, height=2).place(x=215, y=260)
    button77 = Button(board, text=" ", width=4, height=2).place(x=255, y=260)
    button78 = Button(board, text=" ", width=4, height=2).place(x=295, y=260)
    button79 = Button(board, text=" ", width=4, height=2).place(x=335, y=260)
    button80 = Button(board, text=" ", width=4, height=2).place(x=375, y=260)
    
    button81 = Button(board, text=" ", width=4, height=2).place(x=15, y=295)
    button82 = Button(board, text=" ", width=4, height=2).place(x=55, y=295)  
    button83 = Button(board, text=" ", width=4, height=2).place(x=95, y=295) 
    button84 = Button(board, text=" ", width=4, height=2).place(x=135, y=295)
    button85 = Button(board, text=" ", width=4, height=2).place(x=175, y=295) 
    button86 = Button(board, text=" ", width=4, height=2).place(x=215, y=295)
    button87 = Button(board, text=" ", width=4, height=2).place(x=255, y=295)
    button88 = Button(board, text=" ", width=4, height=2).place(x=295, y=295)
    button89 = Button(board, text=" ", width=4, height=2).place(x=335, y=295)
    button90 = Button(board, text=" ", width=4, height=2).place(x=375, y=295)
    
    button91 = Button(board, text=" ", width=4, height=2).place(x=15, y=330)
    button92 = Button(board, text=" ", width=4, height=2).place(x=55, y=330)  
    button93 = Button(board, text=" ", width=4, height=2).place(x=95, y=330) 
    button94 = Button(board, text=" ", width=4, height=2).place(x=135, y=330)
    button95 = Button(board, text=" ", width=4, height=2).place(x=175, y=330) 
    button96 = Button(board, text=" ", width=4, height=2).place(x=215, y=330)
    button97 = Button(board, text=" ", width=4, height=2).place(x=255, y=330)
    button98 = Button(board, text=" ", width=4, height=2).place(x=295, y=330)
    button99 = Button(board, text=" ", width=4, height=2).place(x=335, y=330)
    button100 = Button(board, text=" ", width=4, height=2).place(x=375, y=330)
    
    
        


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

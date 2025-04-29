#Help websites:
#https://www.tutorialspoint.com/python/python_gui_programming.htm
#http://effbot.org/tkinterbook/
#http://effbot.org/tkinterbook/grid.htm

import tkinter
from tkinter import *


# ------------------- Button Function DEFs ---------------
#a function to get the entered first and last name and
#displays the info as full name
def show_name():
    print(f"First Name: {e1.get()}")
    name = f"Your first name is {e1.get()}."
    answer.configure(text=name)
   

#a function to quit the window
def quit_window():
    pass
    #root.destroy()
    #sys.exit(0)



#-------------------- GUI TKInter Setup ------------------
root = Tk()
# window title bar
root.title("What's your name?")
#set the GUI dimensions
root.geometry("300x300")


# add label in the first cell
f_name = Label(root, text="First Name").grid(row=0, column=0, sticky=N)


# text field for text entry
e1 = Entry(root)
# add it to the grid
e1.grid(row=0, column=1, pady=4)



# add buttons to grid layout
q_btn = Button(root, text='Quit', command=quit_window).grid(row=4, column=0, sticky=N, pady=4)
show_btn = Button(root, text='Show Name', command=show_name)
show_btn.grid(row=4, column=1, sticky=N, pady=4)


answer = tkinter.Label(root, text="Please enter your first name.", pady=10)
answer.grid(row=3, column=0, columnspan=2)








mainloop( )

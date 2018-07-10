# https://www.tutorialspoint.com/python/tk_checkbutton.htm

import tkinter
from tkinter import *

top = tkinter.Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()

# The Checkbutton widget is used to display a number of options to a user as toggle buttons.
# The user can then select one or more options by clicking the button corresponding to each option.
C1 = Checkbutton(top, text="Music", variable=CheckVar1, onvalue=1, offvalue=0, height=5, width=20)
C2 = Checkbutton(top, text="Video", variable=CheckVar2, onvalue=1, offvalue=0, height=5, width=20)

C1.pack()
C2.pack()

top.mainloop()

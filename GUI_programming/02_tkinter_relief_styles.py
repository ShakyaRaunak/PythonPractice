# https://www.tutorialspoint.com/python/tk_relief.htm

import tkinter
from tkinter import *

top = tkinter.Tk()

"""
The relief style of a widget refers to certain simulated 3-D effects around the outside of the widget.
"""

B1 = tkinter.Button(top, text="FLAT", relief=FLAT)
B2 = tkinter.Button(top, text="RAISED", relief=RAISED)
B3 = tkinter.Button(top, text="SUNKEN", relief=SUNKEN)
B4 = tkinter.Button(top, text="GROOVE", relief=GROOVE)
B5 = tkinter.Button(top, text="RIDGE", relief=RIDGE)

B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()

top.mainloop()

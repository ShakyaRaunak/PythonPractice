# https://www.tutorialspoint.com/python/tk_cursors.htm

import tkinter
from tkinter import *

top = tkinter.Tk()

"""
Python Tkinter supports quite a number of different mouse cursors available. The exact graphic may vary according to 
your operating system.
"""

B1 = tkinter.Button(top, text="circle", relief=RAISED, cursor="circle")
B2 = tkinter.Button(top, text="plus", relief=RAISED, cursor="plus")
B1.pack()
B2.pack()

top.mainloop()

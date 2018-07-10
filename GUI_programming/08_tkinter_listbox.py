# https://www.tutorialspoint.com/python/tk_listbox.htm

from tkinter import *

top = Tk()

# The Listbox widget is used to display a list of items from which a user can select a number of items.
Lb1 = Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")

Lb1.pack()

top.mainloop()

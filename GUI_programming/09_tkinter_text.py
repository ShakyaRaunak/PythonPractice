# https://www.tutorialspoint.com/python/tk_text.htm

"""
Text widgets provide advanced capabilities that allow you to edit a multiline text and format the way it has to be displayed,
such as changing its color and font.
"""

from tkinter import *


def onclick():
    pass


root = Tk()

text = Text(root)
text.insert(INSERT, "Hello.....")
text.insert(END, "Bye Bye.....")

text.pack()

text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
text.tag_config("here", background="yellow", foreground="blue")
text.tag_config("start", background="black", foreground="green")

root.mainloop()
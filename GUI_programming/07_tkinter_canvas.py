# https://www.tutorialspoint.com/python/tk_canvas.htm

import tkinter

top = tkinter.Tk()

# The Canvas is a rectangular area intended for drawing pictures or other complex layouts.
# You can place graphics, text, widgets or frames on a Canvas.
C = tkinter.Canvas(top, bg="blue", height=250, width=300)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")

C.pack()

top.mainloop()

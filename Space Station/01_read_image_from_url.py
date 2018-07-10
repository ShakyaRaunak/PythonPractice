# https://stackoverflow.com/questions/33010401/need-help-converting-jpg-link-to-gif-format

from PIL import Image, ImageTk
from io import BytesIO
import urllib.request
import tkinter as tk

root = tk.Tk()
url = "http://www.wired.com/wp-content/uploads/2015/03/10182025tonedfull-660x441.jpg"
u = urllib.request.urlopen(url)
raw_data = u.read()
u.close()

image_file = Image.open(BytesIO(raw_data))
photo_image = ImageTk.PhotoImage(image_file)
label = tk.Label(image=photo_image)
label.pack()
root.mainloop()

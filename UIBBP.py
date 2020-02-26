import tkinter as tk
from tkinter.filedialog import askopenfile
import subprocess
import PIL.Image
import PIL.ImageTk
import PIL.ImageFilter
import skimage
import numpy
import os

HEIGHT = 800
WIDTH = 800
filtered_image = ' '


def image_file_search():
    file_image = PIL.Image.open(askopenfile("r").name).convert('LA')
    resizer = (500, 500)
    file_image = file_image.resize(resizer)
    global filtered_image
    filtered_image = file_image.filter(PIL.ImageFilter.FIND_EDGES)
    tk_ready_image = PIL.ImageTk.PhotoImage(filtered_image)
    image_label = tk.Label(center_frame, image=tk_ready_image)
    image_label.image = tk_ready_image
    image_label.place(relx=.5, rely=.5, anchor="center")


def image_snipping_process():
    printer_coord = []
    width, height = filtered_image.size
    left = 0
    top = 0
    right = 490
    bottom = 0
    counter = 0
    pix_val = list(filtered_image.getdata())
    for x in range(width):
        for y in range(height):
            if 255 in pix_val[counter]:
                printer_coord.append((x, y))
            counter += 1
    print(printer_coord)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

top_frame = tk.Frame(root, bg="#696969")
top_frame.place(relheight=0.1, relwidth=1.0, relx=.5, rely=.01, anchor="n")

intro_text = tk.Label(top_frame, text="The Ultimate Blackboard Printer", font=40)
intro_text.place(relx=0.5, rely=0.5, anchor="center")

center_frame = tk.Frame(root, bg="black")
center_frame.place(relheight=0.8, relwidth=1.0, relx=.5, rely=.13, anchor="n")

bottom_frame = tk.Frame(root, bg="#696969")
bottom_frame.place(relheight=0.05, relwidth=1.0, relx=.5, rely=.94, anchor="n")

search_file = tk.Button(bottom_frame, text="Click to search explorer", command=image_file_search)
search_file.place(relx=.45, rely=.5, anchor="center")

search_file = tk.Button(bottom_frame, text="Print", command=image_snipping_process)
search_file.place(relx=.6, rely=.5, anchor="center")

root.mainloop()






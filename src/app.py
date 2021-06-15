import tkinter as tk
from tkinter import filedialog, Text
import os
from datetime import datetime

def close_func():
    print('paok')
    root.destroy()

def print_paok():
    time = datetime.now()
    for widget in frame.winfo_children():
        widget.destroy()
    label = tk.Label(frame, text=f'paok {time}')
    label.pack()

root = tk.Tk()

canvas = tk.Canvas(root, height=600, width=700)
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

closeApp = tk.Button(root, text='close app', command=close_func)
closeApp.pack()

printPaok = tk.Button(root, text='print paok', command=print_paok)
printPaok.pack()

root.mainloop()

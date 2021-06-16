import tkinter as tk
from tkinter import filedialog, Text
import os
from datetime import datetime

def close_func():
    print('paok')
    root.destroy()


def insert_words():
    popupInsert = tk.Toplevel(root)
    popupInsert.geometry("400x400")
    span = tk.Label(popupInsert, text='spanish')
    span.grid(row=0, column=0)
    eng = tk.Label(popupInsert, text='english')
    eng.grid(row=0, column=1)
    span_words = []
    eng_words = []
    for i in range(5):
        temp_span = tk.Entry(popupInsert)
        temp_span.grid(row=i+1, column=0)
        temp_eng = tk.Entry(popupInsert)
        temp_eng.grid(row=i+1, column=1)
        span_words.append(temp_span)
        eng_words.append(temp_eng)
    addCellsButton=tk.Button(popupInsert, text='add cells', command=lambda: print_all_entries(span_words, eng_words))
    addCellsButton.grid()
    importWordsButton=tk.Button(popupInsert, text='import words', command=lambda: print_all_entries(span_words, eng_words))
    importWordsButton.grid()


def print_all_entries(list1, list2):
    for item in list1:
        print(item.get())
    for item in list2:
        print(item.get())


root = tk.Tk()

canvas = tk.Canvas(root, height=600, width=700)
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

closeAppButton = tk.Button(root, text='close app', command=close_func)
closeAppButton.pack()

insertWordsButton = tk.Button(frame, text='insert words', command=insert_words)
insertWordsButton.pack()

root.mainloop()

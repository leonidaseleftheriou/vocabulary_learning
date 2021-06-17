import tkinter as tk
from tkinter import filedialog, Text
import os
from datetime import datetime
import json

def close_func():
    print('paok')
    root.destroy()


def insert_words():
    popupInsert = tk.Toplevel(root)
    popupInsert.geometry("400x400")
    span = tk.Label(popupInsert, text='spanish')
    span.grid(row=0, column=0)
    eng = tk.Label(popupInsert, text='english')
    eng.grid(row=0, column=2)
    span_words = []
    eng_words = []
    for i in range(5):
        temp_span = tk.Entry(popupInsert)
        temp_span.grid(row=i+1, column=0)
        temp_equal = tk.Label(popupInsert, text='=')
        temp_equal.grid(row=i+1, column=1)
        temp_eng = tk.Entry(popupInsert)
        temp_eng.grid(row=i+1, column=2)
        span_words.append(temp_span)
        eng_words.append(temp_eng)
    addCellsButton=tk.Button(popupInsert, text='add cells', command=lambda: print_all_entries(span_words, eng_words))
    addCellsButton.grid()
    importWordsButton=tk.Button(popupInsert, text='import words', command=lambda: print_all_entries(span_words, eng_words))
    importWordsButton.grid()


def delete_words():
    popupDelete = tk.Toplevel(root)
    popupDelete.geometry("400x400")
    listOfWords = tk.Listbox(popupDelete, selectmode='multiple')
    for i, (k, v) in enumerate(voc_dict.items()):
        listOfWords.insert(i, f"{k}, {v}")
    listOfWords.pack()
    deleteButton = tk.Button(popupDelete, text='delete now', command=lambda: delete_words_after_selecting(listOfWords))
    deleteButton.pack()

def delete_words_after_selecting(listbox):
    for idx in listbox.curselection():
        comb_to_remove = listbox.get(idx)
        words = comb_to_remove.split(', ')
        key = words[0]
        voc_dict.pop(key, None)
    with open('vocabulary.json', 'w') as f:
        json.dump(voc_dict, f)



def print_all_entries(list1, list2):
    for item in list1:
        print(item.get())
    for item in list2:
        print(item.get())


with open('vocabulary.json') as f:
    voc_dict = json.load(f)

root = tk.Tk()

canvas = tk.Canvas(root, height=600, width=700)
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

closeAppButton = tk.Button(root, text='close app', command=close_func)
closeAppButton.pack()

insertWordsButton = tk.Button(frame, text='insert words', command=insert_words)
insertWordsButton.pack()

deleteWordsButton = tk.Button(frame, text='delete words', command=delete_words)
deleteWordsButton.pack()

root.mainloop()

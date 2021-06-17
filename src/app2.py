import tkinter as tk
import json


class App:
    def __init__(self):
        self.root = tk.Tk()

        with open('vocabulary.json') as f:
            self.voc_dict = json.load(f)

        self.canvas = tk.Canvas(self.root, height=600, width=700)
        self.canvas.pack()

        self.frame = tk.Frame(self.root, bg='white')
        self.frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        self.closeAppButton = tk.Button(self.root, text='close app', command=self.close_func)
        self.closeAppButton.pack()

        self.insertWordsButton = tk.Button(self.frame, text='insert words', command=self.insert_words)
        self.insertWordsButton.pack()

        self.deleteWordsButton = tk.Button(self.frame, text='delete words', command=self.delete_words)
        self.deleteWordsButton.pack()

        self.root.mainloop()

    def close_func(self):
        self.root.destroy()

    def insert_words(self):
        pass

    def delete_words(self):
        DeletePopup(self)


class DeletePopup:
    def __init__(self, main_app):
        self.main_app = main_app

        self.popupDelete = tk.Toplevel(self.main_app.root)
        self.popupDelete.geometry("300x100")

        rootHeight = self.popupDelete.winfo_height()
        rootWidth = self.popupDelete.winfo_width()

        self.listOfWords = tk.Listbox(self.popupDelete, selectmode='multiple')
        self.print_list_of_words()
        self.listOfWords.pack(side='left', fill='y')

        self.scrollbar = tk.Scrollbar(self.popupDelete, orient="vertical")
        self.scrollbar.config(command=self.listOfWords.yview)
        self.scrollbar.pack(side='left', fill='y')

        self.listOfWords.config(yscrollcommand=self.scrollbar.set)

        self.deleteButton = tk.Button(self.popupDelete, text='delete now',
                command=lambda: self.delete_words_after_selecting(self.listOfWords))
        self.deleteButton.pack(anchor='nw')

    def print_list_of_words(self):
        for i, (k, v) in enumerate(self.main_app.voc_dict.items()):
            self.listOfWords.insert(i, f"{v} = {k}")

    def delete_words_after_selecting(self, listbox):
        for idx in listbox.curselection():
            comb_to_remove = listbox.get(idx)
            words = comb_to_remove.split(' = ')
            key = words[1]
            self.main_app.voc_dict.pop(key, None)
        with open('vocabulary.json', 'w') as f:
            json.dump(self.main_app.voc_dict, f)
        self.listOfWords.delete('0', 'end')
        self.print_list_of_words()


def main():
    app = App()


if __name__ == '__main__':
    main()

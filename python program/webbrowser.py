import tkinter as tk
from tkinter import*

win = tk.Tk()
win.title("web browser")
win.geometry("250x150")


igoogle = PhotoImage(file="google.png")
google = tk.Button(win,image=igoogle)

win.mainloop()
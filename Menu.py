import tkinter as tk

win = tk.Tk()
win.geometry('400x300')

lab = tk.Label(win, text="Demo application")
win.update()

menu = tk.Menu(win)
win.mainloop()
#Excerpt From: David Love. “Tkinter GUI Programming by Example.” Apple Books. https://books.apple.com/us/book/tkinter-gui-programming-by-example/id1368888083
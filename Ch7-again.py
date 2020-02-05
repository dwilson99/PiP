import tkinter as tk

win = tk.Tk()
win.geometry('400x300')

lab = tk.Label(win, text="Demo application")
menu = tk.Menu(win)
menu.add_command(label='Change Label Text', command=lambda: lab.configure(text='Menu Item Clicked'))
menu.add_command(label='Change Window Size', command=lambda: win.geometry('600x600'))
lab.pack()
w = tk.Label(win, 
          justify=left,
          compound = left,
          padx = 10, 
          text="explanation", 
          image=logo).pack(side="right")


win=Window()

win.update()
win.mainloop()
#Excerpt From: David Love. “Tkinter GUI Programming by Example.” Apple Books. https://books.apple.com/us/book/tkinter-gui-programming-by-example/id1368888083
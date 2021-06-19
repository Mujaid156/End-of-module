
from tkinter import *

root = Tk()
root.title("Title")
root.geometry('600x600')

bgImage = PhotoImage(file=r"index.png")
Label(root, image=bgImage).place(relwidth=1, relheight=1)


root.mainloop()

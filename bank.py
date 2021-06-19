from tkinter import *

prize = Tk()
prize.title("Claim your prize")
prize.geometry("500x500")
prize.config(bg="#ffcc00")

# Creating Labels
head = Label(prize, text="Bank Details", font="arial 20 italic", bg="#ffcc00")
details = Label(prize, text="Enter bank details to collect your prize", font="arial 15 italic", bg="#ffcc00")
holder = Label(prize, text="Enter account holder name", bg="#ffcc00")
account = Label(prize, text="Account Number", bg="#ffcc00")
name_bank = Label(prize, text="Name of bank", bg="#ffcc00")

# Creating Entries
holder_input = Entry(prize)
account_input = Entry(prize)
age_entry = Entry(prize, state='readonly')

# Placing Entries
holder_input.place(x=280, y=170)
account_input.place(x=280, y=220)

def cleared():
    holder_input.delete(0, END)
    account_input.delete(0, END)

def exit_program():
    return prize.destroy()

# Creating Buttons
clear = Button(prize, text="Clear", command=cleared)
send = Button(prize, text="claim")
close = Button(prize, text="Exit", command=exit_program)

# Placing Buttons
clear.place(x=50, y=400)
send.place(x=200, y=400)
close.place(x=350, y=400)

# Creating Dropdown #
options = ['Banks...', "Standard Bank", "Capitec", "Absa Bank", "Nedbank"]
variable = StringVar(prize)
variable.set(options[0])

gender_menu = OptionMenu(prize, variable, *options)

gender_menu.place(x=280, y=270)

# Placing Labels
head.place(x=170, y=50)
details.place(x=80, y=120)
holder.place(x=50, y=170)
account.place(x=50, y=220)
name_bank.place(x=50, y=270)


prize.mainloop()

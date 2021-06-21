# Mujaid Kariem
# Class 2

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import smtplib
import requests
from playsound import playsound

prize = Tk()
prize.title("Claim your prize")
prize.geometry("600x700")
prize.config(bg="#ffcc00")


class ClaimPrizes:
    def __init__(self, master):
        # Creating Labels
        self.head = Label(master, text="Bank Details", font="arial 20 italic", bg="#ffcc00")
        self.details = Label(master, text="Enter bank details to collect your prize", font="arial 15 italic", bg="#ffcc00")
        self.holder = Label(master, text="Enter account holder name", bg="#ffcc00")
        self.account = Label(master, text="Account Number", bg="#ffcc00")
        self.name_bank = Label(master, text="Name of bank", bg="#ffcc00")
        self.convert = Label(master, text="Convert Currency", bg="#ffcc00")
        self.convert.place(x=50, y=350)
        self.won = Label(master, text="Winnings")
        self.current = Label(master, text="Conversion")
        self.won.place(x=300, y=350)
        self.current.place(x=300, y=450)

        # Creating Entries
        self.holder_input = Entry(master)
        self.account_input = Entry(master)
        self.age_entry = Entry(master, state='readonly')

        # Placing Entries
        self.holder_input.place(x=280, y=170)
        self.account_input.place(x=280, y=220)

        # Creating Buttons
        self.clear = Button(master, text="Clear", command=self.cleared)
        self.send = Button(master, text="claim")
        self.close = Button(master, text="Exit", command=self.exit_program)

        # Placing Buttons
        self.clear.place(x=50, y=600)
        self.send.place(x=200, y=600)
        self.close.place(x=350, y=600)
        self.cashed.place(x=50, y=400)

        # Creating Dropdown #
        self.options = ['Banks...', "Standard Bank", "Capitec", "Absa Bank", "Nedbank"]
        self.variable = StringVar(prize)
        self.variable.set(self.options[0])

        self.gender_menu = OptionMenu(prize, self.variable, self.options)

        self.gender_menu.place(x=280, y=270)

        # Placing Labels
        self.head.place(x=170, y=50)
        self.details.place(x=80, y=120)
        self.holder.place(x=50, y=170)
        self.account.place(x=50, y=220)
        self.name_bank.place(x=50, y=270)

        self.url = 'https://v6.exchangerate-api.com/v6/5f809448d8e0bf0ba369b44d/latest/ZAR'
        self.response = requests.get(self.url)
        self.data = self.response.json()
        self.rates = self.data['conversion_rates']
        self.currency_list = []
        for i in self.rates.keys():
            self.currency_list.append(i)
        self.cashed = ttk.Combobox()
        self.cashed['values'] = self.currency_list
        self.cashed['state'] = 'readonly'
        self.cashed.set("Select Currency")


    def convert_func(self):
        try:
            x = self.data['conversion_rates'][self.cashed.get()]
            mywinnings = []
            with open("cash.txt", "rt") as myfile:
                for myline in myfile:
                    mywinnings.append(int(myline))
                    self.won.config(text=mywinnings[0])
            new_currency = x * float(mywinnings[0])
            self.current.config(text=new_currency)
        except requests.exceptions.ConnectionError:
            messagebox.showerror("Invalid", "Wrong input")

    def submit_line(self):
        email_line = []
        try:
            with open("info.txt", "+a") as w:
                w.write("Account Name: " + str(self.holder_input.get()))
                w.write("\n")
                w.write("Account Number: " + str(int(self.account_input.get())))
                w.write("\n")
            with open("info.txt", "+r") as f:
                line = f.readline()
                email_line.append(line)
                line2 = f.read()
            s = smtplib.SMTP('smtp.gmail.com', 587)
            sender = 'lifechoiceslotto147@gmail.com'
            receive = str(email_line[0])
            password = 'lifechoices2021'
            s.starttls()
            s.login(sender, password)
            message = str(line2)
            s.sendmail(sender, receive, message)
            s.quit()
        except ValueError:
            if self.holder_input.get() != str:
                messagebox.showerror("Error", "Must be in letters or characters or strings")
            if self.account_input.get() != int:
                messagebox.showerror("Error", "Must be in numbers")
        except smtplib.SMTPException:
            pass

    def cleared(self):
        self.holder_input.delete(0, END)
        self.account_input.delete(0, END)

    def exit_program(self):
        return prize.destroy()



ClaimPrizes(prize)
prize.mainloop()

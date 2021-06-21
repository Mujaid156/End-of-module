# Mujaid Kariem
# Class 2

from tkinter import *
from datetime import datetime
from tkinter import messagebox
from email_validator import validate_email, EmailNotValidError
from playsound import playsound

lotto = Tk()
lotto.title("Lottery")
lotto.geometry("500x700")
lotto.config(bg="#ffcc00")


class login:
    def __init__(self, master):
        # Creating Labels
        self.register = Label(master, text="Register", font="arial 20 italic", bg="#ffcc00")
        self.name = Label(master, text="Please enter fullname: ", bg="#ffcc00")
        self.email = Label(master, text="Please enter email: ", bg="#ffcc00")
        self.address = Label(master, text="Please enter address: ", bg="#ffcc00")
        self.id = Label(master, text="Please enter ID: ", bg="#ffcc00")

        # Creating Entries
        self.name_input = Entry(master)
        self.email_input = Entry(master)
        self.address_input = Entry(master)
        self.id_input = Entry(master)

        # Creating Buttons
        self.clear = Button(master, text="Clear", border=10, width=7, command=self.clear)
        self.confirm = Button(master, text="Confirm", border=10, command=self.email_val)
        self.exit = Button(master, text="Exit", command=self.exit_program, border=10, width=7)

        # Creating Canvas
        self.img = PhotoImage(file="Ithuba-logo-removebg-preview.png")
        self.canvas = Canvas(master, width=400, height=250, bg="#ffcc00", highlightthickness=0, relief='ridge')
        self.canvas.create_image(0, 0, anchor=NW, image=self.img)
        self.canvas.place(x=120, y=10)

        # Placing Labels
        self.register.place(x=200, y=280)
        self.name.place(x=20, y=400)
        self.email.place(x=20, y=450)
        self.address.place(x=20, y=500)
        self.id.place(x=20, y=550)

        # Placing entries
        self.name_input.place(x=240, y=400)
        self.email_input.place(x=240, y=450)
        self.address_input.place(x=240, y=500)
        self.id_input.place(x=240, y=550)

        # Placing Buttons
        self.clear.place(x=50, y=620)
        self.confirm.place(x=200, y=620)
        self.exit.place(x=350, y=620)

        self.unique_id = ""
        self.details = open("info.txt", 'w')

    def email_val(self):
        self.unique_id += "FullName: " + self.name_input.get() + '\n' + "Email Address: " + self.email_input.get() + '\n' + "Address: " + self.address_input.get() + '\n' + "ID Number: " + self.id_input.get() + '\n'
        self.details.write(self.unique_id)

        try:
            validate_email(self.email_input.get())

        except EmailNotValidError:
            messagebox.showerror("Invalid Entry", "Please enter correct email")
            playsound('erro.mp3')

        try:
            age = datetime.today()
            year = int(age.strftime("%y"))
            for entry in range(int(self.id_input.get())):
                age_valid = int(self.id_input.get()[0:2]) - year
                if age_valid >= 18:
                    messagebox.showinfo("You qualify", "You are old enough to try your luck.")
                    lotto.destroy()
                    import lotto_draw
                elif age_valid != 18:
                    messagebox.showerror("You don not qualify", "Sorry, you are not there yet.")
                    playsound('erro.mp3')
                    break
                elif self.id_input.get() != 13:
                    messagebox.showerror("ID number invalid", "Please try again.")
                    playsound('erro.mp3')
                    break
        except ValueError:
            messagebox.showerror("Invalid entry", "Please only use numbers.")
            playsound('erro.mp3')

    def clear(self):
        playsound('button-28.mp3')
        self.name_input.delete(0, END)
        self.email_input.delete(0, END)
        self.address_input.delete(0, END)
        self.id_input.delete(0, END)

    def exit_program(self):
        playsound('windows-xp-startup.mp3')
        return lotto.destroy()


login(lotto)
lotto.mainloop()

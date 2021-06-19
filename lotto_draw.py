# Mujaid Kariem
# Class 2

from tkinter import *
from tkinter import messagebox
from random import sample
from itertools import chain

lotto_draw = Tk()
lotto_draw.title("Lottery Draw")
lotto_draw.geometry("600x900")
lotto_draw.config(bg="#ffcc00")

class lottery:
    def __init__(self, slave):
        # Creating Labels
        self.luck = Label(slave, text="Wanna try your Luck!", font="arial 20 italic", bg="#ffcc00")
        self.choose = Label(slave, text="Choose 6 numbers", font="arial 20 italic", bg="#ffcc00")
        self.your_luck = Label(slave, text="Let's see how lucky you are", font="arial 20 italic", bg="#ffcc00")
        self.results = Label(slave, text="", bg="#ffcc00")

        # Placing Labels
        self.luck.place(x=180, y=190)
        self.choose.place(x=190, y=300)
        self.your_luck.place(x=120, y=650)
        self.results.place(x=120, y=700)

        # Creating Canvas
        self.img = PhotoImage(file="index.png")
        self.canvas = Canvas(lotto_draw, width=400, height=190, bg="#ffcc00", highlightthickness=0, relief='ridge')
        self.canvas.create_image(0, 0, anchor=NW, image=self.img)
        self.canvas.place(x=150, y=10)
        self.play_try = []
        self.play_try2 = []
        self.play_try3 = []

        self.guess1 = Label(lotto_draw, textvariable=self.play_try, width=20)
        self.guess2 = Label(lotto_draw, width=20, textvariable=self.play_try2)
        self.guess3 = Label(lotto_draw, width=20, textvariable=self.play_try3)

        # Placing Entries
        self.guess1.place(x=30, y=250)
        self.guess2.place(x=220, y=250)
        self.guess3.place(x=400, y=250)

        # Creating the clear, check and exit Buttons
        self.again = Button(slave, text="Play again", command=self.again)
        self.play = Button(slave, text="Let's play!", command=self.play_game)
        self.claim = Button(slave, text="Claim prize", command=self.claim)

        self.again.place(x=120, y=800)
        self.play.place(x=260, y=800)
        self.claim.place(x=400, y=800)

        # Creating Buttons
        self.num1 = Button(slave, text="1", width=2, command=lambda: self.btn(1))
        self.num2 = Button(slave, text="2", width=2, command=lambda: self.btn(2))
        self.num3 = Button(slave, text="3", width=2, command=lambda: self.btn(3))
        self.num4 = Button(slave, text="4", width=2, command=lambda: self.btn(4))
        self.num5 = Button(slave, text="5", width=2, command=lambda: self.btn(5))
        self.num6 = Button(slave, text="6", width=2, command=lambda: self.btn(6))
        self.num7 = Button(slave, text="7", width=2, command=lambda: self.btn(7))
        self.num8 = Button(slave, text="8", width=2, command=lambda: self.btn(8))
        self.num9 = Button(slave, text="9", width=2, command=lambda: self.btn(9))
        self.num10 = Button(slave, text="10", command=lambda: self.btn(10))
        self.num11 = Button(slave, text="11", command=lambda: self.btn(11))
        self.num12 = Button(slave, text="12", command=lambda: self.btn(12))
        self.num13 = Button(slave, text="13", command=lambda: self.btn(13))
        self.num14 = Button(slave, text="14", command=lambda: self.btn(14))
        self.num15 = Button(slave, text="15", command=lambda: self.btn(15))
        self.num16 = Button(slave, text="16", command=lambda: self.btn(16))
        self.num17 = Button(slave, text="17", command=lambda: self.btn(17))
        self.num18 = Button(slave, text="18", command=lambda: self.btn(18))
        self.num19 = Button(slave, text="19", command=lambda: self.btn(19))
        self.num20 = Button(slave, text="20", command=lambda: self.btn(20))
        self.num21 = Button(slave, text="21", command=lambda: self.btn(21))
        self.num22 = Button(slave, text="22", command=lambda: self.btn(22))
        self.num23 = Button(slave, text="23", command=lambda: self.btn(23))
        self.num24 = Button(slave, text="24", command=lambda: self.btn(24))
        self.num25 = Button(slave, text="25", command=lambda: self.btn(25))
        self.num26 = Button(slave, text="26", command=lambda: self.btn(26))
        self.num27 = Button(slave, text="27", command=lambda: self.btn(27))
        self.num28 = Button(slave, text="28", command=lambda: self.btn(28))
        self.num29 = Button(slave, text="29", command=lambda: self.btn(29))
        self.num30 = Button(slave, text="30", command=lambda: self.btn(30))
        self.num31 = Button(slave, text="31", command=lambda: self.btn(31))
        self.num32 = Button(slave, text="32", command=lambda: self.btn(32))
        self.num33 = Button(slave, text="33", command=lambda: self.btn(33))
        self.num34 = Button(slave, text="34", command=lambda: self.btn(34))
        self.num35 = Button(slave, text="35", command=lambda: self.btn(35))
        self.num36 = Button(slave, text="36", command=lambda: self.btn(36))
        self.num37 = Button(slave, text="37", command=lambda: self.btn(37))
        self.num38 = Button(slave, text="38", command=lambda: self.btn(38))
        self.num39 = Button(slave, text="39", command=lambda: self.btn(39))
        self.num40 = Button(slave, text="40", command=lambda: self.btn(40))
        self.num41 = Button(slave, text="41", command=lambda: self.btn(41))
        self.num42 = Button(slave, text="42", command=lambda: self.btn(42))
        self.num43 = Button(slave, text="43", command=lambda: self.btn(43))
        self.num44 = Button(slave, text="44", command=lambda: self.btn(44))
        self.num45 = Button(slave, text="45", command=lambda: self.btn(45))
        self.num46 = Button(slave, text="46", command=lambda: self.btn(46))
        self.num47 = Button(slave, text="47", command=lambda: self.btn(47))
        self.num48 = Button(slave, text="48", command=lambda: self.btn(48))
        self.num49 = Button(slave, text="49", command=lambda: self.btn(49))

        # Placing Buttons
        self.num1.place(x=50, y=350)
        self.num2.place(x=100, y=350)
        self.num3.place(x=150, y=350)
        self.num4.place(x=200, y=350)
        self.num5.place(x=250, y=350)
        self.num6.place(x=300, y=350)
        self.num7.place(x=350, y=350)
        self.num8.place(x=400, y=350)
        self.num9.place(x=450, y=350)
        self.num10.place(x=500, y=350)
        self.num11.place(x=50, y=400)
        self.num12.place(x=100, y=400)
        self.num13.place(x=150, y=400)
        self.num14.place(x=200, y=400)
        self.num15.place(x=250, y=400)
        self.num16.place(x=300, y=400)
        self.num17.place(x=350, y=400)
        self.num18.place(x=400, y=400)
        self.num19.place(x=450, y=400)
        self.num20.place(x=500, y=400)
        self.num21.place(x=50, y=450)
        self.num22.place(x=100, y=450)
        self.num23.place(x=150, y=450)
        self.num24.place(x=200, y=450)
        self.num25.place(x=250, y=450)
        self.num26.place(x=300, y=450)
        self.num27.place(x=350, y=450)
        self.num28.place(x=400, y=450)
        self.num29.place(x=450, y=450)
        self.num30.place(x=500, y=450)
        self.num31.place(x=50, y=500)
        self.num32.place(x=100, y=500)
        self.num33.place(x=150, y=500)
        self.num34.place(x=200, y=500)
        self.num35.place(x=250, y=500)
        self.num36.place(x=300, y=500)
        self.num37.place(x=350, y=500)
        self.num38.place(x=400, y=500)
        self.num39.place(x=450, y=500)
        self.num40.place(x=500, y=500)
        self.num41.place(x=75, y=550)
        self.num42.place(x=125, y=550)
        self.num43.place(x=175, y=550)
        self.num44.place(x=225, y=550)
        self.num45.place(x=275, y=550)
        self.num46.place(x=325, y=550)
        self.num47.place(x=375, y=550)
        self.num48.place(x=425, y=550)
        self.num49.place(x=475, y=550)

    def claim(self):
        return lotto_draw.destroy()

    def again(self):
        self.guess1.config(text='')
        self.guess2.config(text='')
        self.guess3.config(text='')
        self.results.config(text='')
        del self.play_try[:]
        del self.play_try3[:]
        del self.play_try2[:]

    def btn(self, x):
        try:
            if len(self.play_try) <= 5 and x not in self.play_try:
                self.play_try.append(x)
                self.guess1.config(text=self.play_try)

            elif len(self.play_try) == 6 and len(self.play_try2) <= 5 and x not in self.play_try2:
                self.play_try2.append(x)
                self.guess2.config(text=self.play_try2)

            elif len(self.play_try2) == 6 and len(self.play_try3) <= 5 and x not in self.play_try3:
                self.play_try3.append(x)
                self.guess3.config(text=self.play_try3)

            else:
                messagebox.showerror("Invalid Entry", "A number can only be chosen once.")
        except:
            return 'nothing'

    def play_game(self):
        lotto_numbers = sample(range(1, 50), 6)
        try:
            numbers = list(chain(self.play_try, self.play_try2, self.play_try3))
            winnings = set(numbers).intersection(lotto_numbers)
            if len(winnings) == 0:
                self.results.config(text='Your numbers are ' + '\n' + str(numbers) + '\n' + 'Winning numbers' + str(lotto_numbers) + "\n" + 'You are broke')
            elif len(winnings) == 1:
                self.results.config(text='Your numbers are: ' + '\n' + str(numbers) + '\n' + 'Winning numbers are: ' + str(lotto_numbers) + "\n" + 'You do not win anything')
            elif len(winnings) == 2:
                self.results.config(text='Your numbers are: ' + '\n' + str(numbers) + '\n' + 'Winning numbers are: ' + str(lotto_numbers) + "\n" + 'You are a R20 richer')
            elif len(winnings) == 3:
                self.results.config(text='Your numbers are: ' + '\n' + str(numbers) + '\n' + 'Winning numbers are: ' + str(lotto_numbers) + "\n" + 'You are a R100.50 richer')
            elif len(winnings) == 4:
                self.results.config(text='Your numbers are: ' + '\n' + str(numbers) + '\n' + 'Winning numbers are: ' + str(lotto_numbers) + "\n" + 'You are a R2384 richer')
            elif len(winnings) == 5:
                self.results.config(text='Your numbers are: ' + '\n' + str(numbers) + '\n' + 'Winning numbers are: ' + str(lotto_numbers) + "\n" + 'You are a R8584 richer')
            elif len(winnings) == 6:
                self.results.config(text='Your numbers are: ' + '\n' + str(numbers) + '\n' + 'Winning numbers are: ' + str(lotto_numbers) + "\n" + 'You are a R10 000 000 richer')
            else:
                self.results.config(text='You are unlucky, try again when you are feeling lucky')
        finally:
            return 'nothing'


lottery(lotto_draw)
lotto_draw.mainloop()

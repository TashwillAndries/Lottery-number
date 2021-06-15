from tkinter import *
from tkinter import messagebox
# importing a randomizer
import random

lottery = Tk()
lottery.config(bg="yellow")
lottery.title("Lottery Entry")
lottery.geometry("550x650")

canvas = Canvas(lottery, width=385, height=130)
image = PhotoImage(file="index.png")
canvas.create_image(0, 0, anchor=NW, image=image)
canvas.pack()


class LotteryNumbers:
    def __init__(self, master):
        self.numbers_label = Label(master, text="Please Choose 6 unique numbers between 1 - 49", font="poppins 10", bg="yellow")
        self.numbers_label.place(x=120, y=150)
        self.btn1 = Button(master, text=1, padx=15, command=lambda: self.on_click(1))
        self.btn1.place(x=50, y=190)
        self.btn2 = Button(master, text=2, padx=15, command=lambda: self.on_click(2))
        self.btn2.place(x=100, y=190)
        self.btn3 = Button(master, text=3, padx=15, command=lambda: self.on_click(3))
        self.btn3.place(x=150, y=190)
        self.btn4 = Button(master, text=4, padx=15, command=lambda: self.on_click(4))
        self.btn4.place(x=200, y=190)
        self.btn5 = Button(master, text=5, padx=15, command=lambda: self.on_click(5))
        self.btn5.place(x=250, y=190)
        self.btn6 = Button(master, text=6, padx=15, command=lambda: self.on_click(6))
        self.btn6.place(x=300, y=190)
        self.btn7 = Button(master, text=7, padx=15, command=lambda: self.on_click(7))
        self.btn7.place(x=350, y=190)
        self.btn8 = Button(master, text=8, padx=15, command=lambda: self.on_click(8))
        self.btn8.place(x=400, y=190)
        self.btn9 = Button(master, text=9, padx=15, command=lambda: self.on_click(9))
        self.btn9.place(x=450, y=190)
        self.btn10 = Button(master, text=10, command=lambda: self.on_click(10))
        self.btn10.place(x=50, y=230)
        self.btn11 = Button(master, text=11, command=lambda: self.on_click(11))
        self.btn11.place(x=100, y=230)
        self.btn12 = Button(master, text=12, command=lambda: self.on_click(12))
        self.btn12.place(x=150, y=230)
        self.btn13 = Button(master, text=13, command=lambda: self.on_click(13))
        self.btn13.place(x=200, y=230)
        self.btn14 = Button(master, text=14, command=lambda: self.on_click(14))
        self.btn14.place(x=250, y=230)
        self.btn15 = Button(master, text=15, command=lambda: self.on_click(15))
        self.btn15.place(x=300, y=230)
        self.btn16 = Button(master, text=16, command=lambda: self.on_click(16))
        self.btn16.place(x=350, y=230)
        self.btn17 = Button(master, text=17, command=lambda: self.on_click(17))
        self.btn17.place(x=400, y=230)
        self.btn18 = Button(master, text=18, command=lambda: self.on_click(18))
        self.btn18.place(x=450, y=230)
        self.btn19 = Button(master, text=19, command=lambda: self.on_click(19))
        self.btn19.place(x=50, y=270)
        self.btn20 = Button(master, text=20, command=lambda: self.on_click(20))
        self.btn20.place(x=100, y=270)
        self.btn21 = Button(master, text=21, command=lambda: self.on_click(21))
        self.btn21.place(x=150, y=270)
        self.btn22 = Button(master, text=22, command=lambda: self.on_click(22))
        self.btn22.place(x=200, y=270)
        self.btn23 = Button(master, text=23, command=lambda: self.on_click(23))
        self.btn23.place(x=250, y=270)
        self.btn24 = Button(master, text=24, command=lambda: self.on_click(24))
        self.btn24.place(x=300, y=270)
        self.btn25 = Button(master, text=25, command=lambda: self.on_click(25))
        self.btn25.place(x=350, y=270)
        self.btn26 = Button(master, text=26, command=lambda: self.on_click(26))
        self.btn26.place(x=400, y=270)
        self.btn27 = Button(master, text=27, command=lambda: self.on_click(27))
        self.btn27.place(x=450, y=270)
        self.btn28 = Button(master, text=28, command=lambda: self.on_click(28))
        self.btn28.place(x=50, y=310)
        self.btn29 = Button(master, text=29, command=lambda: self.on_click(29))
        self.btn29.place(x=100, y=310)
        self.btn30 = Button(master, text=30, command=lambda: self.on_click(30))
        self.btn30.place(x=150, y=310)
        self.btn31 = Button(master, text=31, command=lambda: self.on_click(31))
        self.btn31.place(x=200, y=310)
        self.btn32 = Button(master, text=32, command=lambda: self.on_click(32))
        self.btn32.place(x=250, y=310)
        self.btn33 = Button(master, text=33,command=lambda: self.on_click(33))
        self.btn33.place(x=300, y=310)
        self.btn34 = Button(master, text=34, command=lambda: self.on_click(34))
        self.btn34.place(x=350, y=310)
        self.btn35 = Button(master, text=35, command=lambda: self.on_click(35))
        self.btn35.place(x=400, y=310)
        self.btn36 = Button(master, text=36, command=lambda: self.on_click(36))
        self.btn36.place(x=450, y=310)
        self.btn37 = Button(master, text=37, command=lambda: self.on_click(37))
        self.btn37.place(x=50, y=350)
        self.btn38 = Button(master, text=38, command=lambda: self.on_click(38))
        self.btn38.place(x=100, y=350)
        self.btn39 = Button(master, text=39, command=lambda: self.on_click(39))
        self.btn39.place(x=150, y=350)
        self.btn40 = Button(master, text=40, command=lambda: self.on_click(40))
        self.btn40.place(x=200, y=350)
        self.btn41 = Button(master, text=41, command=lambda: self.on_click(41))
        self.btn41.place(x=250, y=350)
        self.btn42 = Button(master, text=42, command=lambda: self.on_click(42))
        self.btn42.place(x=300, y=350)
        self.btn43 = Button(master, text=43, command=lambda: self.on_click(43))
        self.btn43.place(x=350, y=350)
        self.btn44 = Button(master, text=44, command=lambda: self.on_click(44))
        self.btn44.place(x=400, y=350)
        self.btn45 = Button(master, text=45, command=lambda: self.on_click(45))
        self.btn45.place(x=450, y=350)
        self.btn46 = Button(master, text=46, command=lambda: self.on_click(46))
        self.btn46.place(x=250, y=390)
        self.btn47 = Button(master, text=47, command=lambda: self.on_click(47))
        self.btn47.place(x=300, y=390)
        self.btn48 = Button(master, text=48, command=lambda: self.on_click(48))
        self.btn48.place(x=350, y=390)
        self.btn49 = Button(master, text=49, command=lambda: self.on_click(49))
        self.btn49.place(x=400, y=390)
        self.user_answers1 = Label(master, bg="red", width=25, height=2)
        self.user_answers1.place(x=200, y=450)
        self.user_answers2 = Label(master, bg="red", width=25, height=2)
        self.user_answers2.place(x=200, y=500)
        self.user_answers3 = Label(master, bg="red", width=25, height=2)
        self.user_answers3.place(x=200, y=550)
        self.play_btn = Button(master, text="Play", command=self.play)
        self.play_btn.place(x=150, y=600)
        self.claim_btn = Button(master, text="Claim")
        self.claim_btn.place(x=250, y=600)
        self.replay_btn = Button(master, text="Play Again")
        self.replay_btn.place(x=350, y=600)
        self.lottery_set1 = []
        self.lottery_set2 = []
        self.lottery_set3 = []

    def on_click(self, num):
        if len(self.lottery_set1) <= 5 and num not in self.lottery_set1:
            self.lottery_set1.append(num)
            self.user_answers1.config(text=self.lottery_set1)

        elif len(self.lottery_set1) == 6 and len(self.lottery_set2) <= 5 and num not in self.lottery_set2:
            self.lottery_set2.append(num)
            self.user_answers2.config(text=self.lottery_set2)
        elif len(self.lottery_set2) == 6 and len(self.lottery_set3) <= 5 and num not in self.lottery_set3:
            self.lottery_set3.append(num)
            self.user_answers3.config(text=self.lottery_set3)
        else:
            messagebox.showerror("Error", "You can only choose one number")

    def play(self):
        correct = 0
        correct2 = 0
        correct3 = 0
        lotto_list = random.sample(range(1, 49), 6)
        for number in self.lottery_set1:
            if number in lotto_list:
                correct += 1
        for number in self.lottery_set2:
            if number in lotto_list:
                correct2 += 1
        for number in self.lottery_set3:
            if number in lotto_list:
                correct3 += 1
        if correct >= 2:
            messagebox.showinfo("Congratulations", "You won" + 20 + "bucks")



numbers = LotteryNumbers(lottery)
lottery.mainloop()

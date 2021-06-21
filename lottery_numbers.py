# importing a randomizer
import random
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from playsound import playsound
from main import player
lottery = Tk()
lottery.config(bg="yellow")
lottery.title("Lottery Entry")
lottery.geometry("550x650")

canvas = Canvas(lottery, width=385, height=130)
image = PhotoImage(file="index.png")
canvas.create_image(0, 0, anchor=NW, image=image)
canvas.pack()
winnings = 0

class LotteryNumbers:
    def __init__(self, master):
        self.master = master
        self.numbers_label = Label(master, text="Please Choose 6 unique numbers between 1 - 49", font="poppins 10",
                                   bg="yellow")
        self.numbers_label.place(x=120, y=150)
        self.btn1 = Button(master, text=1, padx=15, command=lambda: self.on_click(1), border=4, bg="#1e90ff", fg="blue")
        self.btn1.place(x=50, y=190)
        self.btn2 = Button(master, text=2, padx=15, command=lambda: self.on_click(2), border=4, bg="#1e90ff", fg="blue")
        self.btn2.place(x=100, y=190)
        self.btn3 = Button(master, text=3, padx=15, command=lambda: self.on_click(3), border=4, bg="#1e90ff", fg="blue")
        self.btn3.place(x=150, y=190)
        self.btn4 = Button(master, text=4, padx=15, command=lambda: self.on_click(4), border=4, bg="#1e90ff", fg="blue")
        self.btn4.place(x=200, y=190)
        self.btn5 = Button(master, text=5, padx=15, command=lambda: self.on_click(5), border=4, bg="#1e90ff", fg="blue")
        self.btn5.place(x=250, y=190)
        self.btn6 = Button(master, text=6, padx=15, command=lambda: self.on_click(6), border=4, bg="#1e90ff", fg="blue")
        self.btn6.place(x=300, y=190)
        self.btn7 = Button(master, text=7, padx=15, command=lambda: self.on_click(7), border=4, bg="#1e90ff", fg="blue")
        self.btn7.place(x=350, y=190)
        self.btn8 = Button(master, text=8, padx=15, command=lambda: self.on_click(8), border=4, bg="#1e90ff", fg="blue")
        self.btn8.place(x=400, y=190)
        self.btn9 = Button(master, text=9, padx=15, command=lambda: self.on_click(9), border=4, bg="#1e90ff", fg="blue")
        self.btn9.place(x=450, y=190)
        self.btn10 = Button(master, text=10, command=lambda: self.on_click(10), border=4, bg="#1e90ff", fg="blue")
        self.btn10.place(x=50, y=230)
        self.btn11 = Button(master, text=11, command=lambda: self.on_click(11), border=4, bg="#1e90ff", fg="blue")
        self.btn11.place(x=100, y=230)
        self.btn12 = Button(master, text=12, command=lambda: self.on_click(12), border=4, bg="#1e90ff", fg="blue")
        self.btn12.place(x=150, y=230)
        self.btn13 = Button(master, text=13, command=lambda: self.on_click(13), border=4, bg="#1e90ff", fg="blue")
        self.btn13.place(x=200, y=230)
        self.btn14 = Button(master, text=14, command=lambda: self.on_click(14), border=4, bg="#1e90ff", fg="blue")
        self.btn14.place(x=250, y=230)
        self.btn15 = Button(master, text=15, command=lambda: self.on_click(15), border=4, bg="#1e90ff", fg="blue")
        self.btn15.place(x=300, y=230)
        self.btn16 = Button(master, text=16, command=lambda: self.on_click(16), border=4, bg="#1e90ff", fg="blue")
        self.btn16.place(x=350, y=230)
        self.btn17 = Button(master, text=17, command=lambda: self.on_click(17), border=4, bg="#1e90ff", fg="blue")
        self.btn17.place(x=400, y=230)
        self.btn18 = Button(master, text=18, command=lambda: self.on_click(18), border=4, bg="#1e90ff", fg="blue")
        self.btn18.place(x=450, y=230)
        self.btn19 = Button(master, text=19, command=lambda: self.on_click(19), border=4, bg="#1e90ff", fg="blue")
        self.btn19.place(x=50, y=270)
        self.btn20 = Button(master, text=20, command=lambda: self.on_click(20), border=4, bg="#1e90ff", fg="blue")
        self.btn20.place(x=100, y=270)
        self.btn21 = Button(master, text=21, command=lambda: self.on_click(21), border=4, bg="#1e90ff", fg="blue")
        self.btn21.place(x=150, y=270)
        self.btn22 = Button(master, text=22, command=lambda: self.on_click(22), border=4, bg="#1e90ff", fg="blue")
        self.btn22.place(x=200, y=270)
        self.btn23 = Button(master, text=23, command=lambda: self.on_click(23), border=4, bg="#1e90ff", fg="blue")
        self.btn23.place(x=250, y=270)
        self.btn24 = Button(master, text=24, command=lambda: self.on_click(24), border=4, bg="#1e90ff", fg="blue")
        self.btn24.place(x=300, y=270)
        self.btn25 = Button(master, text=25, command=lambda: self.on_click(25), border=4, bg="#1e90ff", fg="blue")
        self.btn25.place(x=350, y=270)
        self.btn26 = Button(master, text=26, command=lambda: self.on_click(26), border=4, bg="#1e90ff", fg="blue")
        self.btn26.place(x=400, y=270)
        self.btn27 = Button(master, text=27, command=lambda: self.on_click(27), border=4, bg="#1e90ff", fg="blue")
        self.btn27.place(x=450, y=270)
        self.btn28 = Button(master, text=28, command=lambda: self.on_click(28), border=4, bg="#1e90ff", fg="blue")
        self.btn28.place(x=50, y=310)
        self.btn29 = Button(master, text=29, command=lambda: self.on_click(29), border=4, bg="#1e90ff", fg="blue")
        self.btn29.place(x=100, y=310)
        self.btn30 = Button(master, text=30, command=lambda: self.on_click(30), border=4, bg="#1e90ff", fg="blue")
        self.btn30.place(x=150, y=310)
        self.btn31 = Button(master, text=31, command=lambda: self.on_click(31), border=4, bg="#1e90ff", fg="blue")
        self.btn31.place(x=200, y=310)
        self.btn32 = Button(master, text=32, command=lambda: self.on_click(32), border=4, bg="#1e90ff", fg="blue")
        self.btn32.place(x=250, y=310)
        self.btn33 = Button(master, text=33, command=lambda: self.on_click(33), border=4, bg="#1e90ff", fg="blue")
        self.btn33.place(x=300, y=310)
        self.btn34 = Button(master, text=34, command=lambda: self.on_click(34), border=4, bg="#1e90ff", fg="blue")
        self.btn34.place(x=350, y=310)
        self.btn35 = Button(master, text=35, command=lambda: self.on_click(35), border=4, bg="#1e90ff", fg="blue")
        self.btn35.place(x=400, y=310)
        self.btn36 = Button(master, text=36, command=lambda: self.on_click(36), border=4, bg="#1e90ff", fg="blue")
        self.btn36.place(x=450, y=310)
        self.btn37 = Button(master, text=37, command=lambda: self.on_click(37), border=4, bg="#1e90ff", fg="blue")
        self.btn37.place(x=50, y=350)
        self.btn38 = Button(master, text=38, command=lambda: self.on_click(38), border=4, bg="#1e90ff", fg="blue")
        self.btn38.place(x=100, y=350)
        self.btn39 = Button(master, text=39, command=lambda: self.on_click(39), border=4, bg="#1e90ff", fg="blue")
        self.btn39.place(x=150, y=350)
        self.btn40 = Button(master, text=40, command=lambda: self.on_click(40), border=4, bg="#1e90ff", fg="blue")
        self.btn40.place(x=200, y=350)
        self.btn41 = Button(master, text=41, command=lambda: self.on_click(41), border=4, bg="#1e90ff", fg="blue")
        self.btn41.place(x=250, y=350)
        self.btn42 = Button(master, text=42, command=lambda: self.on_click(42), border=4, bg="#1e90ff", fg="blue")
        self.btn42.place(x=300, y=350)
        self.btn43 = Button(master, text=43, command=lambda: self.on_click(43), border=4, bg="#1e90ff", fg="blue")
        self.btn43.place(x=350, y=350)
        self.btn44 = Button(master, text=44, command=lambda: self.on_click(44), border=4, bg="#1e90ff", fg="blue")
        self.btn44.place(x=400, y=350)
        self.btn45 = Button(master, text=45, command=lambda: self.on_click(45), border=4, bg="#1e90ff", fg="blue")
        self.btn45.place(x=450, y=350)
        self.btn46 = Button(master, text=46, command=lambda: self.on_click(46), border=4, bg="#1e90ff", fg="blue")
        self.btn46.place(x=250, y=390)
        self.btn47 = Button(master, text=47, command=lambda: self.on_click(47), border=4, bg="#1e90ff", fg="blue")
        self.btn47.place(x=300, y=390)
        self.btn48 = Button(master, text=48, command=lambda: self.on_click(48), border=4, bg="#1e90ff", fg="blue")
        self.btn48.place(x=350, y=390)
        self.btn49 = Button(master, text=49, command=lambda: self.on_click(49), border=4, bg="#1e90ff", fg="blue")
        self.btn49.place(x=400, y=390)
        self.user_answers1 = Label(master, bg="red", width=25, height=2)
        self.user_answers1.place(x=320, y=450)
        self.user_answers2 = Label(master, bg="red", width=25, height=2)
        self.user_answers2.place(x=320, y=500)
        self.user_answers3 = Label(master, bg="red", width=25, height=2)
        self.user_answers3.place(x=320, y=550)
        self.play_btn = Button(master, text="Play", command=self.play, border=5, bg="#1e90ff", fg="blue", width=10)
        self.play_btn.place(x=20, y=600)
        self.claim_btn = Button(master, text="Claim Price", border=5, bg="#1e90ff", fg="blue", command=self.claim)
        self.claim_btn.place(x=310, y=600)
        self.replay_btn = Button(master, text="Play Again", command=self.play_again, border=5, bg="#1e90ff", fg="blue")
        self.replay_btn.place(x=430, y=600)
        self.show_btn = Button(master, text="Show Winnings", command=self.winnings, border=5, bg="#1e90ff", fg="blue")
        self.show_btn.place(x=150, y=600)
        self.winning = Label(master, bg="yellow", text="Winnings")
        self.winning.place(x=120, y=530)
        self.prizes_label = Label(master, bg="green", width=25, height=2)
        self.prizes_label.place(x=50, y=550)
        self.winning_numbers = Label(master, bg="yellow", text="Winning Numbers")
        self.winning_numbers.place(x=90, y=430)
        self.lotto_no = Label(master, bg="green", width=25, height=2)
        self.lotto_no.place(x=50, y=452)
        self.lottery_set1 = []
        self.lottery_set2 = []
        self.lottery_set3 = []


    def on_click(self, pick):
        playsound("click.mp3")
        if len(self.lottery_set1) <= 5 and pick not in self.lottery_set1:
            self.lottery_set1.append(pick)
            self.user_answers1.config(text=self.lottery_set1)
        elif len(self.lottery_set1) == 6 and len(self.lottery_set2) <= 5 and pick not in self.lottery_set2:
            self.lottery_set2.append(pick)
            self.user_answers2.config(text=self.lottery_set2)

        elif len(self.lottery_set2) == 6 and len(self.lottery_set3) <= 5 and pick not in self.lottery_set3:
            self.lottery_set3.append(pick)
            self.user_answers3.config(text=self.lottery_set3)
        else:
            if len(self.lottery_set3) == 6:
                messagebox.showerror("Error", "Entries are full")
            elif pick in self.lottery_set3:
                messagebox.showerror("Error", "Number already chosen")
            elif pick in self.lottery_set2:
                messagebox.showerror("Error", "Number already chosen")
            elif pick in self.lottery_set1:
                messagebox.showerror("Error", "Number already chosen")

    def play(self):
        correct = 0
        correct2 = 0
        correct3 = 0
        self.earnings1 = 0
        self.earnings2 = 0
        self.earnings3 = 0
        prizes = [0, 0, 20, 100.50, 2384, 8584, 10000000]  # prizes in rands
        self.lotto_list = random.sample(range(1, 49), 6)
        self.lotto_list.sort()
        matching1 = set(self.lottery_set1).intersection(set(self.lotto_list))
        matching2 = set(self.lottery_set2).intersection(set(self.lotto_list))
        matching3 = set(self.lottery_set3).intersection(set(self.lotto_list))
        for number in self.lottery_set1:
            if number in self.lotto_list:
                correct += 1
            if correct == 2:
                self.earnings1 = prizes[2]
            elif correct == 3:
                self.earnings1 = prizes[3]
            elif correct == 4:
                self.earnings1 = prizes[4]
            elif correct == 5:
                self.earnings1 = prizes[5]
            elif correct == 6:
                self.earnings1 = prizes[6]
        else:
            messagebox.showerror("Matches", "Matches in set one: " + str(correct) + "\nEarnings: " + "R"
                                 + str(self.earnings1) +
                                 "\nMatching number: " + str(matching1))

        for number in self.lottery_set2:
            if number in self.lotto_list:
                correct2 += 1
            if correct2 == 2:
                self.earnings2 = prizes[2]
            elif correct2 == 3:
                self.earnings2 = prizes[3]
            elif correct2 == 4:
                self.earnings2 = prizes[4]
            elif correct2 == 5:
                self.earnings2 = prizes[5]
            elif correct2 == 6:
                self.earnings2 = prizes[6]
        else:
            messagebox.showerror("Matches", "Matches in set one: " + str(correct2) + "\nEarnings: " +
                                 "R" + str(self.earnings2) + "\nMatching number: " + str(matching2))

        for number in self.lottery_set3:
            if number in self.lotto_list:
                correct3 += 1
            if correct3 == 2:
                self.earnings3 = prizes[2]
            elif correct3 == 3:
                self.earnings3 = prizes[3]
            elif correct3 == 4:
                self.earnings3 = prizes[4]
            elif correct3 == 5:
                self.earnings3 = prizes[5]
            elif correct3 == 6:
                self.earnings3 = prizes[6]
        else:
            messagebox.showerror("Matches", "Matches in set one: " + str(correct3) + "\nEarnings: " +
                                 "R" + str(self.earnings3) + "\nMatching number: " + str(matching3))

    # function that calculates winnings
    def winnings(self):
        global winnings
        if len(self.lottery_set1) == 6 and len(self.lottery_set2) == 6 and len(self.lottery_set3) == 6:
            winnings = float(self.earnings1 + self.earnings2 + self.earnings3)
            self.prizes_label.config(text="R" + str(winnings))
            self.lotto_no.config(text=self.lotto_list)
            return winnings
        else:
            messagebox.showinfo("Error", "Please use all your tries first")

    def play_again(self):
        self.user_answers1.config(text="")
        self.user_answers2.config(text="")
        self.user_answers3.config(text="")
        self.prizes_label.config(text="")
        self.lotto_no.config(text="")
        self.lottery_set1 = []
        self.lottery_set2 = []
        self.lottery_set3 = []

    # send users to the bank details window
    def claim(self):
        if winnings >= 20:
            lottery.withdraw()
            self.new_window = Toplevel(self.master)
            self.new_window.config(bg="yellow")
            self.new_window.title("Banking Details")
            self.new_window.geometry("550x650")
            self.detail = Window2(self.new_window)
        else:
            messagebox.showerror("Error", "No prize to claim")


class Window2:
    def __init__(self, master):
        self.master = master
        # bank details and api details
        self.banks = ["Capitec", "ABSA", "Nedbank", "Standard bank"]
        self.currency = requests.get('https://v6.exchangerate-api.com/v6/3b6104d9c62069d198e73219/latest/ZAR')
        self.currency_json = self.currency.json()
        self.conversion_rate = self.currency_json['conversion_rates']
        self.v = StringVar()
        self.header = Label(master, text="Banking Details", font=("Times", "40", "bold italic"), bg="yellow")
        self.header.place(x=100, y=20)
        self.drop_label = Label(master, text="Please select which bank you are with: ", bg="yellow")
        self.drop_label.place(x=20, y=100)
        self.combo = ttk.Combobox(master, value=self.banks, width=19)
        self.combo.place(x=350, y=100)
        self.holder_name_label = Label(master, text="Please enter Account holders name: ", bg="yellow")
        self.holder_name_label.place(x=20, y=150)
        self.holder_name_entry = Entry(master)
        self.holder_name_entry.place(x=350, y=150)
        # self.holder_name_entry.bind("<KeyRelease>", self.caps)
        self.bank_number_label = Label(master, text="Please enter your account number: ", bg="yellow")
        self.bank_number_label.place(x=20, y=200)
        self.bank_number_entry = Entry(master)
        self.bank_number_entry.place(x=350, y=200)
        self.account_type_label = Label(master, text="Please Enter the account Type: ", bg="yellow")
        self.account_type_label.place(x=20, y=250)
        self.account_type_entry = Entry(master)
        self.account_type_entry.place(x=350, y=250)
        self.email = Label(master, text="Please Enter email address: ", bg='yellow')
        self.email.place(x=20, y=300)
        self.email_entry = Entry(master)
        self.email_entry.place(x=350, y=300)
        self.winnings_label = Label(master, text="Enter Winnings to Convert: ", bg="yellow")
        self.winnings_label.place(x=20, y=350)
        self.winnings_entry = Entry(master)
        self.winnings_entry.place(x=350, y=350)
        self.conversion_label = Label(master, width=20, bg="green")
        self.conversion_label.place(x=355, y=430)
        self.conversion_btn = Button(master, text="Convert currency", border=5, bg="#1e90ff", fg="blue", command=self.convert)
        self.conversion_btn.place(x=250, y=510)
        self.send_email = Button(master, text="Confirm Details", border=5, bg="#1e90ff", fg="blue", command=self.confirm)
        self.send_email.place(x=400, y=510)
        # self.holder_name_entry.swapcase()
        self.currency_box = ttk.Combobox(master)
        self.convert_list = Listbox(master, width=20)
        for i in self.conversion_rate.keys():
            self.convert_list.insert(END, str(i))
        self.convert_list.place(x=20, y=450)

# function to convert to different currency
    def convert(self):
        for i in self.conversion_rate.keys():
            num = float(self.winnings_entry.get())
            # print(self.currency_json['conversion_rates'][self.convert_list.get(ACTIVE)])
            answer = num * self.currency_json['conversion_rates'][self.convert_list.get(ACTIVE)]
            self.conversion_label['text'] = round(answer, 2)

    def confirm(self):
        number = self.bank_number_entry.get()
        account_type = self.account_type_entry.get()
        holder = self.holder_name_entry.get()
        s = smtplib.SMTP('smtp.gmail.com', 587)
        sender_email_id = 'tashwilla27@gmail.com'
        receiver_email_id = self.email_entry.get()
        password = "N@ruto56"

        subject = "Details confirmation"
        msg = MIMEMultipart()
        msg['from'] = sender_email_id
        msg['To'] = receiver_email_id
        msg['Subject'] = subject

        body = "Player ID: " + str(player()) + "\nWinnings: " + str(winnings) + "\n Bank Holder name: " \
               + str(holder) + "\n Account type: " + str(account_type)
        body = body + "\n Account Number: " + str(number)

        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        s.starttls()
        s.login(sender_email_id, password)

        s.sendmail(sender_email_id, receiver_email_id, text)
        s.quit()


# numbers = LotteryNumbers(lottery)
details = LotteryNumbers(lottery)
lottery.mainloop()


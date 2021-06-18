from tkinter import *
from tkinter import ttk
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from main import player
from lottery_numbers import LotteryNumbers
from tkinter import messagebox

details = Tk()
details.config(bg="yellow")
details.title("Banking Details")
details.geometry("550x650")

# bank details and api details
banks = ["Capitec", "ABSA", "Nedbank", "Standard bank"]
currency = requests.get('https://v6.exchangerate-api.com/v6/3b6104d9c62069d198e73219/latest/ZAR')
currency_json = currency.json()
conversion_rate = currency_json['conversion_rates']


def caps(event):
    v.set(v.get().upper())

v = StringVar()

header = Label(details, text="Banking Details", font=("Times", "40", "bold italic"), bg="yellow")
header.place(x=100, y=20)
drop_label = Label(details, text="Please select which bank you are with: ", bg="yellow")
drop_label.place(x=20, y=100)
combo = ttk.Combobox(details, value=banks, width=19)
combo.place(x=350, y=100)
holder_name_label = Label(details, text="Please enter Account holders name: ", bg="yellow")
holder_name_label.place(x=20, y=150)
holder_name_entry = Entry(details, textvariable=v)
holder_name_entry.place(x=350, y=150)
holder_name_entry.bind("<KeyRelease>", caps)
bank_number_label = Label(details, text="Please enter your account number: ", bg="yellow")
bank_number_label.place(x=20, y=200)
bank_number_entry = Entry(details)
bank_number_entry.place(x=350, y=200)
account_type_label = Label(details, text="Please Enter the account Type: ", bg="yellow")
account_type_label.place(x=20, y=250)
account_type_entry = Entry(details)
account_type_entry.place(x=350, y=250)
winnings_label = Label(details, text="Enter Winnings to Convert: ", bg="yellow")
winnings_label.place(x=20, y=300)
winnings_entry = Entry(details)
winnings_entry.place(x=350, y=300)
conversion_label = Label(details, width=20, bg="green")
conversion_label.place(x=355, y=360)


currency_list = []
for i in conversion_rate.keys():
    currency_list.append(i)

# Combobox that contains the different currency
currency_box = ttk.Combobox(details)
currency_box['values'] = currency_list
currency_box['state'] = 'readonly'
currency_box.set('Select Currency')
currency_box.place(x=20, y=360)


# function to convert from ZAR to any other currency
def convert():
    amount = float(winnings_entry.get())
    print(currency_json['conversion_rates'][currency_box.get()])
    answer = amount * currency_json['conversion_rates'][currency_box.get()]
    conversion_label['text'] = round(answer, 2)


def confirm():
    pass
    # number = bank_number_entry.get()
    # account_type = account_type_entry.get()
    # s = smtplib.SMTP('smtp.gmail.com', 587)
    # sender_email_id = 'tashwilla27@gmail.com'
    # receiver_email_id = 'jamestjay85@gmail.com'
    # password =
    #
    # subject = "Greetings"
    # msg = MIMEMultipart()
    # msg['from'] = sender_email_id
    # msg['To'] = receiver_email_id
    # msg['Subject'] = subject
    # body = "Player ID: " + str(player()) + "'\n'Winnings: " + str(LotteryNumbers.play()) + "'\n' Bank Holder name: "
    # body = body + "How was your task yesterday"
    #
    # msg.attach(MIMEText(body, 'plain'))
    # text = msg.as_string()
    # s.starttls()
    # s.login(sender_email_id, password)
    #
    # s.sendmail(sender_email_id, receiver_email_id, text)
    # s.quit()


conversion_btn = Button(details, text="Convert currency", border=5, bg="#1e90ff", fg="blue", command=convert)
conversion_btn.place(x=20, y=450)
send_email = Button(details, text="Confirm Details", border=5, bg="#1e90ff", fg="blue", command=confirm)
send_email.place(x=400, y=450)
details.mainloop()

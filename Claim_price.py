from tkinter import *
from tkinter import ttk
from tkinter import messagebox

details = Tk()
details.config(bg="yellow")
details.title("Banking Details")
details.geometry("550x350")

banks = ["Capitec", "ABSA", "Nedbank", "Standard bank"]

header = Label(details, text="Banking Details", font=("Times", "40", "bold italic"), bg="yellow")
header.place(x=100, y=20)
drop_label = Label(details, text="Please select which bank you are with: ", bg="yellow")
drop_label.place(x=20, y=100)
combo = ttk.Combobox(details, value=banks, width=19)
combo.place(x=350, y=100)
holder_name_label = Label(details, text="Please enter Account holders name: ", bg="yellow")
holder_name_label.place(x=20, y=150)
holder_name_entry = Entry(details)
holder_name_entry.place(x=350, y=150)
bank_number_label = Label(details, text="Please enter your account number: ", bg="yellow")
bank_number_label.place(x=20, y=200)
bank_number_entry = Entry(details)
bank_number_entry.place(x=350, y=200)
account_type_label = Label(details, text="Please Enter the account Type", bg="yellow")
account_type_label.place(x=20, y=250)
account_type_entry = Entry(details)
account_type_entry.place(x=350, y=250)

details.mainloop()

# Tashwill Andries, class group 2
from tkinter import *
from tkinter import messagebox
from datetime import datetime, timedelta
import rsaidnumber

# setup of tkinter window
login = Tk()
login.config(bg="yellow")
login.title("Login Form")
login.geometry("450x450")

canvas = Canvas(login, width=385, height=130)
image = PhotoImage(file="index.png")
canvas.create_image(0, 0, anchor=NW, image=image)
canvas.pack()


class Verify:

    def __init__(self, master):
        self.username_label = Label(master, text="Please enter your name: ", font="poppins 10", bg="yellow")
        self.username_label.place(x=20, y=150)
        self.username_entry = Entry(master, font="poppins 10")
        self.username_entry.place(x=250, y=153)

        self.email_label = Label(master, text="Please enter your email address: ", font="poppins 10", bg="yellow")
        self.email_label.place(x=20, y=215)
        self.email_entry = Entry(master, font="poppins 10")
        self.email_entry.place(x=250, y=215)

        self.address_label = Label(master, text="Please enter your street address: ", font="poppins 10", bg="yellow")
        self.address_label.place(x=20, y=277)
        self.address_entry = Entry(master, font="poppins 10")  # street address
        self.address_entry.place(x=250, y=277)

        self.id_no_label = Label(master, text="Please enter your ID number: ", font="poppins 10", bg="yellow")
        self.id_no_label.place(x=20, y=339)
        self.id_no_entry = Entry(master, font="poppins 10")  # 13 digits only
        self.id_no_entry.place(x=250, y=339)

        self.verify_btn = Button(master, text="Verify", font="poppins 10", bg="light blue", command=self.age_check)
        self.verify_btn.place(x=190, y=390)

# checking if the user is older than 18
    def age_check(self):
        id_number = rsaidnumber.parse(self.id_no_entry.get())
        age = str((datetime.today() - id_number.date_of_birth) // timedelta(days=365.25))
        try:
            if int(age) >= 18:
                messagebox.showinfo("Qualified", "lets play")
            elif int(age) < 18:
                ages = str(int(age) - 18)
                messagebox.showerror("Error", "You don't qualify try again in " + ages + " year/s")
        except ValueError:
            messagebox.showerror("Error", "Enter a Valid ID number")


verify = Verify(login)
login.mainloop()

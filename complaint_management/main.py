from tkinter import *
from tkinter import messagebox, ttk
import sqlite3


# Creating a Database connection
class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
                    CREATE TABLE IF NOT EXISTS complaintList(
                        id Integer Primary Key,
                        name text,
                        age text,
                        email text,
                        contact text,
                        complaint text
                    )
                    """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name, age, email, contact, complaint):
        self.cur.execute("insert into complaintList values (NULL,?,?,?,?,?)",
                         (name, age, email, contact, complaint))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from complaintList")
        rows = self.cur.fetchall()
        # print(rows)
        return rows


def displayAll():
    clearAll()
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)


def addComplaint():
    if (name.get() == "" or age.get() == "" or email.get() == "" or
            contact.get() == "" or complainttxt.get(1.0, END) == ""):
        messagebox.showerror("Field is emplty", "Please fill all the details")
        return
    db.insert(nametxt.get(), agetxt.get(), emailtxt.get(), contacttxt.get(), complainttxt.get(1.0, END))
    messagebox.showinfo("Success", "Complaint Registered Successfully")
    clearAll()


def clearAll():
    name.set("")
    age.set("")
    email.set("")
    contact.set("")
    complainttxt.delete(1.0, END)


def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    name.set(row[1])
    age.set(row[2])
    email.set(row[3])
    contact.set(row[4])
    complainttxt.delete(1.0, END)
    complainttxt.insert(END, row[5])


db = Database("Complaints.db")
window = Tk()
window.title("Complaint Management System")
window.geometry("1980x1080+0+0")
window.config(bg="#2C3E50")
window.state("zoomed")
labels = ("Name", "Age", "Email", "Contact No", "Complaints")

name = StringVar()
age = StringVar()
email = StringVar()
contact = StringVar()

# Entries Frame
entries_frame = Frame(window, bg="#2C3E50")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Register your Queries", anchor="center",
              font=("Calibri", 20, "bold"), bg="#2C3E50", fg="White")
title.grid(row=0, column=2, padx=10, pady=10, sticky="w")

for i in range(len(labels)):
    Label(entries_frame, text=labels[i], font=("Calibri", 12), bg="#2C3E50",
          fg="white").grid(row=i + 1, column=0, padx=10, pady=10, sticky="w")

nametxt = Entry(entries_frame, textvariable=name, font=("Calibri", 12), width=30)
nametxt.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="w")
agetxt = Entry(entries_frame, textvariable=age, font=("Calibri", 12), width=30)
agetxt.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="w")
emailtxt = Entry(entries_frame, textvariable=email, font=("Calibri", 12), width=30)
emailtxt.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky="w")
contacttxt = Entry(entries_frame, textvariable=contact, font=("Calibri", 12), width=30)
contacttxt.grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky="w")
complainttxt = Text(entries_frame, width=60, height=5, font=("Calibri", 12))
complainttxt.grid(row=5, column=1,
                  columnspan=4, padx=10, pady=10, sticky="w")

# Creating the button
buttonFrame = Frame(entries_frame, bg="#2C3E50")
buttonFrame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")

submit = Button(buttonFrame, command=addComplaint, text="Submit", width=8,
                font=("Calibri", 13, "bold"), fg="white",
                bg="#5193B3", bd=0)
submit.grid(row=0, column=0, padx=10)
clear = Button(buttonFrame, command=clearAll, text="Clear", width=8,
               font=("Calibri", 13, "bold"), fg="white",
               bg="#5193B3", bd=0)
clear.grid(row=0, column=1, padx=10)
clear1 = Button(buttonFrame, command=displayAll, text="Complaint Lists", width=15,
                font=("Calibri", 13, "bold"), fg="white",
                bg="#5193B3", bd=0)
clear1.grid(row=0, column=2, padx=10)

# Table Frame
tree_frame = Frame(window, bg="#ecf0f1")
tree_frame.place(x=0, y=420, width=1540, height=520)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=3)
tv.heading("2", text="Name")
tv.column("2", width=12)
tv.heading("3", text="Age")
tv.column("3", width=4)
tv.heading("4", text="Email")
tv.column("4", width=15)
tv.heading("5", text="Contact")
tv.column("5", width=12)
tv.heading("6", text="Complaints")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)
window.mainloop()
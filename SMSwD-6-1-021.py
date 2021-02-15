from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="Student Management System", bd=10, relief=GROOVE,
                      font=("times new roman", 40, "bold"), bg="yellow", fg="red")
        title.pack(side=TOP, fill=X)

        # ===========All Variables====================
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        # ==============Manage frm===========================================================
        manage_frm = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        manage_frm.place(x=20, y=100, width=450, height=580)

        m_title = Label(manage_frm, text="Manage Students", font=("times new roman", 20, "bold"), bg="crimson",
                        fg="white")
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll = Label(manage_frm, text="Roll No.", font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_roll = Entry(manage_frm, textvariable=self.Roll_No_var, bd=5, relief=GROOVE,
                         font=("times new roman", 15, "bold"), bg="white")
        txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(manage_frm, text="Name", font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(manage_frm, bd=5, textvariable=self.name_var, relief=GROOVE,
                         font=("times new roman", 15, "bold"), bg="white")
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_email = Label(manage_frm, text="E-Mail", font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_email = Entry(manage_frm, bd=5, textvariable=self.email_var, relief=GROOVE,
                          font=("times new roman", 15, "bold"), bg="white")
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(manage_frm, text="Gender", font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        cmb_gender = ttk.Combobox(manage_frm, textvariable=self.gender_var, font=("times new roman", 13, "bold"),
                                  state="readonly")
        cmb_gender['values'] = ("Male", "Female", "Other")
        cmb_gender.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        lbl_contact = Label(manage_frm, text="Contact", font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_contact = Entry(manage_frm, bd=5, relief=GROOVE, textvariable=self.contact_var,
                            font=("times new roman", 15, "bold"), bg="white")
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_dob = Label(manage_frm, text="D.O.B", font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_dob = Entry(manage_frm, bd=5, relief=GROOVE, textvariable=self.dob_var,
                        font=("times new roman", 15, "bold"), bg="white")
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_address = Label(manage_frm, text="Address", font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_address = Text(manage_frm, width=30, height=4, font=("", 10))
        self.txt_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        # ======================Button frm======================================================
        btn_frm = Frame(manage_frm, bd=4, relief=RIDGE, bg="crimson")
        btn_frm.place(x=15, y=500, width=420)

        addbtn = Button(btn_frm, text="Add", width=10, command=self.add_students).grid(row=0, column=0, padx=10,
                                                                                       pady=10)
        updatebtn = Button(btn_frm, text="Update", width=10, command=self.update_data).grid(row=0, column=1, padx=10,
                                                                                            pady=10)
        deletebtn = Button(btn_frm, text="Delete", width=10, command=self.delete_data).grid(row=0, column=2, padx=10,
                                                                                            pady=10)
        clearbtn = Button(btn_frm, text="Clear", width=10, command=self.clear).grid(row=0, column=3, padx=10, pady=10)

        # ==============Show frm===========================================================
        detail_frm = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        detail_frm.place(x=500, y=100, width=800, height=580)

        lbl_search = Label(detail_frm, text="Search By", font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        cmb_search = ttk.Combobox(detail_frm, textvariable=self.search_by, width=10,
                                  font=("times new roman", 13, "bold"), state="readonly")
        cmb_search['values'] = ("Roll_No", "Name", "Contact")
        cmb_search.grid(row=0, column=1, pady=10, padx=20, sticky="w")

        txt_search = Entry(detail_frm, textvariable=self.search_txt, width=15, bd=5, relief=GROOVE,
                           font=("times new roman", 10, "bold"))
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(detail_frm, text="Search", width=10, pady=5, command=self.search_data).grid(row=0, column=3,
                                                                                                       padx=10, pady=10)
        showallbtn = Button(detail_frm, text="Show All", width=10, command=self.fetch_data).grid(row=0, column=4,
                                                                                                 padx=10, pady=10)

        # ==============Table frm====================================
        table_frm = Frame(detail_frm, bd=4, relief=RIDGE, bg="crimson")
        table_frm.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(table_frm, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frm, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frm,
                                          columns=("roll", "name", "email", "gender", "contact", "dob", "address"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("roll", text="Roll No.")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("email", text="E-Mail")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("contact", text="Contact")
        self.student_table.heading("dob", text="D.O.B.")
        self.student_table.heading("address", text="Address")
        self.student_table['show'] = 'headings'
        self.student_table.column("roll", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("contact", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("address", width=150)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_students(self):

        if self.Roll_No_var.get() == "" or self.name_var.get() == "" or self.email_var.get() == "" or self.gender_var.get()=="" or self.contact_var.get() == "" or self.dob_var.get() == "" or len(self.txt_address.get("1.0", "end-1c")) == 0:
            messagebox.showerror("Error", "All fields are REqured!!!")
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="stm")
            cur = con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)", (self.Roll_No_var.get(),
                                                                              self.name_var.get(),
                                                                              self.email_var.get(),
                                                                              self.gender_var.get(),
                                                                              self.contact_var.get(),
                                                                              self.dob_var.get(),
                                                                              self.txt_address.get("1.0", END)
                                                                              ))
            con.commit()

            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Record has been inserted")

    def fetch_data(self):   
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="stm")
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0", END)

    def get_cursor(self, ev):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[6])

    def update_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="stm")
        cur = con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s", (
            self.name_var.get(),
            self.email_var.get(),
            self.gender_var.get(),
            self.contact_var.get(),
            self.dob_var.get(),
            self.txt_address.get('1.0', END),
            self.Roll_No_var.get()))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="stm")
        cur = con.cursor()
        cur.execute("delete from students where roll_no=%s",(self.Roll_No_var.get(),))
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        if self.search_by.get() == "" or self.search_txt.get() == "":
            messagebox.showerror("Error", "Enter some data inside a Search Entry")
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="stm")
            cur = con.cursor()
            cur.execute("select * from students where " + str(self.search_by.get()) + " LIKE '%" + str(
                self.search_txt.get()) + "%'")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert('', END, values=row)
                con.commit()
            con.close()


root = Tk()
obj = Student(root)
root.mainloop()
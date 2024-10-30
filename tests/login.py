import tkinter as tk
import sqlite3
from registration import reg
from terminal import main

root = tk.Tk()
root.title("Grass Terminal")
# Functions
def log_in():
    global username
    global password
    username = user_var.get()
    password = pass_var.get()

    conn = sqlite3.connect('logins.db')
    conn.row_factory = lambda cursor, row: row[0]
    cursor = conn.cursor()
    logins = cursor.execute("SELECT password FROM logins WHERE username ='{}'".format(username)).fetchall()
    if not logins:
        error_label = tk.Label(root, text="Login doesnt exist").grid(row=3, column=0, columnspan=2)
    elif password == logins[0]:
        root.after(50, lambda: root.destroy())
        main()
    else:
        wrong_label = tk.Label(root, text="Wrong password").grid(row=3, column=0, columnspan=2)


# Username
user_var = tk.StringVar()
username = ""
usernameLabel = tk.Label(root, text="Username:").grid(row=0)
username_entry = tk.Entry(root, textvariable=user_var).grid(row=0, column=1)

# Password
pass_var = tk.StringVar()
password = ""
passwordLabel = tk.Label(root, text="Password:").grid(row=1)
password_entry = tk.Entry(root, textvariable=pass_var).grid(row=1, column=1)

# Buttons
login_button = tk.Button(root, text="Login", command=lambda: log_in()).grid(row=2)
register_button = tk.Button(root, text="Register", command=lambda: reg()).grid(row=2, column=1)

root.bind('Return', log_in)

tk.mainloop()

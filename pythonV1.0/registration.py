import tkinter as tk
import sqlite3
import smtplib


def reg():
    root = tk.Tk()

    emailReg_var = tk.StringVar()
    emailReg = ""
    usernameReg_var = tk.StringVar()
    usernameReg = ""
    passwordReg_var = tk.StringVar()

    def add_cred():
        global emailReg
        global usernameReg
        global passwordReg
        emailReg = emailReg_var.get()
        usernameReg = usernameReg_var.get()
        passwordReg = passwordReg_var.get()

        conn = sqlite3.connect('logins.db')
        cursor = conn.cursor()
        with sqlite3.connect('logins.db') as conn:
            cursor.execute("INSERT INTO logins (email, username, password) VALUES (?,?,?,)", (emailReg, usernameReg, passwordReg))
            conn.commit()


    def send_email():
        email = "dmorozkin26@gmail.com"
        account = "dmorozkin26@gmail.com"
        reciever = emailReg
        subject = ("Email confirmation")
        message = ("This is an automatic email to confirm creation of your account with Forshung Solutions, and your access to the Forshung Terminal.")
        text = f"Subject: {subject}\n\n{message}"
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls
        server.login(email, "owioktiteagbyklx")
        server.sendmail(account, reciever, text)

    def close_reg():
        root.destroy()

    emailReg_label = tk.Label(root, text="Email:").grid(row=0)
    emailReg_entry = tk.Entry(root, textvariable=emailReg_var).grid(row=0, column=1)

    usernameReg_label = tk.Label(root, text="Username:").grid(row=1)
    usernameReg_entry = tk.Entry(root, textvariable=usernameReg_var).grid(row=1,column=1)

    passwordReg_label = tk.Label(root, text="Password").grid(row=2)
    passwordReg_entry = tk.Entry(root, textvariable=passwordReg_var).grid(row=2,column=1)

    register_button = tk.Button(root, text="Register", command=lambda: [add_cred(), send_email(), close_reg()]).grid(row=3, column=0, columnspan=2)

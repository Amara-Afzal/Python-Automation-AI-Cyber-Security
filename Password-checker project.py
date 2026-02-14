import re
import tkinter as tk
from tkinter import messagebox
def validate_username(username):
    if not username:
        return "Username cannot be empty"
    if len(username) < 4:
        return "Username too short (min 4 characters)"
    if not username.isalnum():
        return "Only letters and numbers allowed"
    return "Valid"

def validate_email(email):
    if not email:
        return "Email cannot be empty"
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return "Valid"
    return "Invalid email format"

def validate_password(password):
    if not password:
        return "Password cannot be empty"
    if len(password) < 8:
        return "Password too short (min 8 characters)"
    if not re.search(r"[A-Z]", password):
        return "Must contain uppercase letter"
    if not re.search(r"[a-z]", password):
        return "Must contain lowercase letter"
    if not re.search(r"[0-9]", password):
        return "Must contain a digit"
    if not re.search(r"[!@#$%^&*()_+]", password):
        return "Must contain special character"
    return "Strong"
def submit_form():
    username = entry_username.get().strip()
    email = entry_email.get().strip()
    password = entry_password.get().strip()

    user_result = validate_username(username)
    email_result = validate_email(email)
    pass_result = validate_password(password)

    if user_result != "Valid":
        messagebox.showerror("Username Error", user_result)
        return
    
    if email_result != "Valid":
        messagebox.showerror("Email Error", email_result)
        return
    
    if pass_result != "Strong":
        messagebox.showerror("Password Error", pass_result)
        return

    messagebox.showinfo("Success", "All inputs validated successfully!")
    clear_fields()

def clear_fields():
    entry_username.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_password.delete(0, tk.END)

root = tk.Tk()
root.title("User Input Validation Tool")
root.geometry("450x400")
root.config(bg="#1e1e2f")
title = tk.Label(root, text="User Registration Form",
                 font=("Arial", 18, "bold"),
                 bg="#1e1e2f", fg="white")
title.pack(pady=20)
tk.Label(root, text="Username",
         font=("Arial", 12),
         bg="#1e1e2f", fg="white").pack()
entry_username = tk.Entry(root, font=("Arial", 12), width=30)
entry_username.pack(pady=5)

tk.Label(root, text="Email",
         font=("Arial", 12),
         bg="#1e1e2f", fg="white").pack()
entry_email = tk.Entry(root, font=("Arial", 12), width=30)
entry_email.pack(pady=5)
tk.Label(root, text="Password",
         font=("Arial", 12),
         bg="#1e1e2f", fg="white").pack()
entry_password = tk.Entry(root, font=("Arial", 12), width=30, show="*")
entry_password.pack(pady=5)
submit_btn = tk.Button(root, text="Submit",
                       font=("Arial", 12, "bold"),
                       bg="#4CAF50", fg="white",
                       width=15, command=submit_form)
submit_btn.pack(pady=15)

clear_btn = tk.Button(root, text="Clear",
                      font=("Arial", 12),
                      bg="#f44336", fg="white",
                      width=15, command=clear_fields)
clear_btn.pack()

root.mainloop()

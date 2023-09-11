import tkinter as tk
from tkinter import ttk
import secrets
import string

def generate_password():
    password_length = int(password_length_entry.get())
    if password_length < 1:
        password_result.set("Invalid length")
        return

    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase
    digit_chars = string.digits
    special_chars = string.punctuation

    pool = ""
    if include_lower.get():
        pool += lower_chars
    if include_upper.get():
        pool += upper_chars
    if include_digits.get():
        pool += digit_chars
    if include_special.get():
        pool += special_chars

    if not pool:
        password_result.set("Select at least one character type")
        return

    password = ''.join(secrets.choice(pool) for _ in range(password_length))
    password_result.set(password)

window = tk.Tk()
window.title("Password Generator")

ttk.Label(window, text="Password Length:").grid(row=0, column=0)
password_length_entry = ttk.Entry(window)
password_length_entry.grid(row=0, column=1)

include_lower = tk.BooleanVar()
include_upper = tk.BooleanVar()
include_digits = tk.BooleanVar()
include_special = tk.BooleanVar()

ttk.Checkbutton(window, text="Lowercase", variable=include_lower).grid(row=1, column=0, sticky="w")
ttk.Checkbutton(window, text="Uppercase", variable=include_upper).grid(row=2, column=0, sticky="w")
ttk.Checkbutton(window, text="Digits", variable=include_digits).grid(row=3, column=0, sticky="w")
ttk.Checkbutton(window, text="Special Characters", variable=include_special).grid(row=4, column=0, sticky="w")

generate_button = ttk.Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=5, columnspan=2)

password_result = tk.StringVar()
ttk.Label(window, text="Generated Password:").grid(row=6, column=0, columnspan=2)
ttk.Label(window, textvariable=password_result).grid(row=7, column=0, columnspan=2)

window.mainloop()

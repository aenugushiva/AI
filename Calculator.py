
import tkinter as tk
from math import sin, cos, tan, radians, log, sqrt

def press(key):
    if key == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif key == "C":
        entry.delete(0, tk.END)
    elif key in ["sin", "cos", "tan", "log", "√"]:
        try:
            value = eval(entry.get())
            if key == "sin":
                result = sin(radians(value))
            elif key == "cos":
                result = cos(radians(value))
            elif key == "tan":
                result = tan(radians(value))
            elif key == "log":
                result = log(value)
            elif key == "√":
                result = sqrt(value)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, key)

root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.configure(bg="#20232a")

entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right", bg="#282c34", fg="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("sin", 5, 1), ("cos", 5, 2), ("tan", 5, 3),
    ("log", 6, 0), ("√", 6, 1), ("(", 6, 2), (")", 6, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text: press(t), bg="#61dafb", fg="black", relief="raised", bd=2)
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()

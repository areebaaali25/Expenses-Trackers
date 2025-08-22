import tkinter as tk
from tkinter import messagebox

# Expense list
expenses = []

# Functions
def add_expense():
    name = entry_name.get()
    try:
        amount = float(entry_amount.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Amount must be a number")
        return

    if not name:
        messagebox.showerror("Invalid Input", "Name cannot be empty")
        return

    expenses.append({"name": name, "amount": amount})
    listbox.insert(tk.END, f"{name} - ${amount:.2f}")
    update_total()

    # clear input fields
    entry_name.delete(0, tk.END)
    entry_amount.delete(0, tk.END)


def update_total():
    total = sum(exp["amount"] for exp in expenses)
    label_total.config(text=f"Total: ${total:.2f}")


# GUI setup
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x400")

# Name input
label_name = tk.Label(root, text="Expense Name:")
label_name.pack(pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.pack(pady=5)

# Amount input
label_amount = tk.Label(root, text="Amount:")
label_amount.pack(pady=5)
entry_amount = tk.Entry(root, width=30)
entry_amount.pack(pady=5)

# Add button
btn_add = tk.Button(root, text="Add Expense", command=add_expense)
btn_add.pack(pady=10)

# Expense list
listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

# Total label
label_total = tk.Label(root, text="Total: $0.00", font=("Arial", 12, "bold"))
label_total.pack(pady=10)

root.mainloop()

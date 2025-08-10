expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    expenses.append({"name": name, "amount": amount})
    print(f"✅ Added: {name} - ${amount:.2f}")

def show_expenses():
    if not expenses:
        print("No expenses yet.")
        return
    print("\n--- Expense List ---")
    total = 0
    for idx, expense in enumerate(expenses, 1):
        print(f"{idx}. {expense['name']} - ${expense['amount']:.2f}")
        total += expense['amount']
    print(f"Total: ${total:.2f}\n")

while True:
    print("\n1. Add Expense")
    print("2. Show Expenses")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        print("Goodbye! 💰")
        break





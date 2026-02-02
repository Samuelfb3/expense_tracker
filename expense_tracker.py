import csv
from datetime import date
FILE_NAME = "expenses.csv"

#Func add expense
def add_expense(category, amount, description):
    today = date.today().isoformat()

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, category, amount, description])

    print("Expense added successfully.")


#Get the expenses from file
def load_expenses():
    expenses = []
    try:
        with open(FILE_NAME, mode="r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 4:
                    continue

                d, cat, amt, desc = row

                try:
                    amt = float(amt)
                except ValueError:
                    continue

                expenses.append(
                    {"date": d, "category": cat, "amount": amt, "description": desc}
                )
    except FileNotFoundError:
        return []

    return expenses



#func search expense
def view_expenses():
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No expenses found yet.")

#Main program
while True:
    print("\nPersonal Budget Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        category = input("Category: ")
        amount = float(input("Amount: "))
        description = input("Description: ")
        add_expense(category, amount, description)

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        print("Goodbye.")
        break

    else:
        print("Invalid option.")

import csv
from datetime import date
FILE_NAME = "expenses.csv"

#Func add expense
def add_expense(category, amount, description):
    today = date.today().isoformat()

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, category, amount, description])

    print("Expense added successfully.")



#Get the expenses from file, helpful to sort categories or amount.
def load_expenses():
    expenses = []
    try:
        with open(FILE_NAME, mode="r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 4:
                    continue

                d, cat, amt, desc = row

                try:
                    amt = float(amt)
                except ValueError:
                    continue

                expenses.append(
                    {"date": d, "category": cat, "amount": amt, "description": desc}
                )
    except FileNotFoundError:
        return []

    return expenses

#Func to calculate total by category.
def show_category_totals():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found yet.")
        return

    totals = {}
    for e in expenses:
        cat = e["category"].strip()
        totals[cat] = totals.get(cat, 0.0) + e["amount"]

    print("\nCATEGORY TOTALS")
    print("-" * 25)
    for cat in sorted(totals.keys()):
        print(f"{cat:<15} ${totals[cat]:.2f}")


#func search expense
def view_expenses():
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No expenses found yet.")

#Main program
while True:
    print("\nPersonal Budget Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show totals by category")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        category = input("Category: ")
        amount = float(input("Amount: "))
        description = input("Description: ")
        add_expense(category, amount, description)

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        show_category_totals()

            
    elif choice == "4":
        print("Goodbye.")
        break

    else:
        print("Invalid option.")


#This is a Github test

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

#func to calculate expenses by month
def monthly_expenses(month):
    expenses = load_expenses()
    total_month = 0

    
    month = month.zfill(2)
    for e in expenses:
        date_str = e["date"]
        part = date_str.split("-")
        expense_month = part[1]

        if expense_month == month:
            total_month += e["amount"]
            
    
    print(f"\nTOTAL SPENT ON MONTH {month}")
    print("Matched Expenses: ", total_month)


#Main program
while True:
    print("\nPersonal Budget Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show totals by category")
    print("4. Show monthly expenses")
    print("5. Exit")
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
        month = input("What month would you like to calculate? (enter the number): ")
        monthly_expenses(month)

    elif choice == "5":
        print("Goodbye.")
        break

    else:
        print("Invalid option.")


#This is a Github test

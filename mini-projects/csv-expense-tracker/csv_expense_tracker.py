# CSV expense tracker
import csv
import datetime
def load_file():
    try:
        with open("expense tracker.csv", "r") as file:
            csv.DictReader(file)
    except FileNotFoundError:
        with open("expense tracker.csv", "w", newline= "") as file:
                fieldnames = ["Amount", "Category", "Description", "Date"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

def add_expense():
    with open("expense tracker.csv", "a", newline= "") as file:
        fieldnames = ["Amount", "Category", "Description", "Date"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        first = input("Enter amount: ")
        try:
            amount = float(first)
            category_option = ["Personal", "Purchase"]
            second = input("Enter category(Personal or Purchase): ").title()
            if second in category_option:
                category = second
                description = input("Enter description: ")
                date = datetime.date.today()
                writer.writerow({"Amount": amount, "Category": category, "Description": description, "Date": date})
            else:
                print("Invalid: Enter either 'Personal' or 'Purchase'")
        except ValueError:
            print("Must be a number or decimal")

def view():
    with open("expense tracker.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row["Amount"]}, {row["Category"]}, {row["Description"]}, {row["Date"]}")

def summary():
    with open("expense tracker.csv", "r") as file:
        reader = csv.DictReader(file)
        total_expense = 0
        category_totals = {}
        for row in reader:
            total_expense += float(row["Amount"])
            category_totals[row["Category"]] = category_totals.get(row["Category"], 0 ) + float(row["Amount"])
        print(f"Total expense: {total_expense}")
        for category, total in category_totals.items():
            print(f"{category}: {total}")


def running():
    options = ["add", "view", "summary", "quit"]
    choice = input("Choose an Option (Add, View, Summary, Quit): ").lower()
    if choice in options:
        if choice == "add":
            add_expense()
            return True
        elif choice == "view":
            view()
            return True
        elif choice == "summary":
            summary()
            return True
        elif choice == "quit":
            exit()
    else:
        print("Invalid!")
    return True

def begin():
    load_file()
    begin = True
    while begin == True:
        begin = running()

begin()
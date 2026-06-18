import csv
import os

FILE_NAME = "expenses.csv"

expenses = []

# Load expenses from CSV
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['Amount'] = float(row['Amount'])
                expenses.append(row)

# Save expenses to CSV
def save_expenses():
    with open(FILE_NAME, mode='w', newline='') as file:
        fieldnames = ['Date', 'Category', 'Description', 'Amount']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(expenses)

# Add expense
def add_expense():
    date = input("Enter Date (DD-MM-YYYY): ")
    category = input("Enter Category: ")
    description = input("Enter Description: ")
    amount = float(input("Enter Amount: ₹"))

    expenses.append({
        'Date': date,
        'Category': category,
        'Description': description,
        'Amount': amount
    })

    save_expenses()
    print("Expense Added Successfully!")

# View expenses
def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n{:<5} {:<12} {:<15} {:<25} {:<10}".format(
        "ID", "Date", "Category", "Description", "Amount"))

    print("-" * 70)

    for i, expense in enumerate(expenses):
        print("{:<5} {:<12} {:<15} {:<25} ₹{:<10}".format(
            i + 1,
            expense['Date'],
            expense['Category'],
            expense['Description'],
            expense['Amount']
        ))

# Total expenses
def total_expense():
    total = sum(expense['Amount'] for expense in expenses)
    print(f"\nTotal Expense: ₹{total:.2f}")

# Category summary
def category_summary():
    summary = {}

    for expense in expenses:
        category = expense['Category']
        amount = expense['Amount']

        summary[category] = summary.get(category, 0) + amount

    print("\nCategory Wise Report")
    print("-" * 30)

    for category, amount in summary.items():
        print(f"{category:<15} ₹{amount:.2f}")

# Monthly report
def monthly_report():
    month = input("Enter Month (MM): ")

    total = 0

    for expense in expenses:
        if expense['Date'][3:5] == month:
            total += expense['Amount']

    print(f"Total Spending in Month {month}: ₹{total:.2f}")

# Delete expense
def delete_expense():
    view_expenses()

    try:
        index = int(input("\nEnter Expense ID to Delete: ")) - 1

        if 0 <= index < len(expenses):
            deleted = expenses.pop(index)
            save_expenses()
            print(f"Deleted: {deleted['Description']}")
        else:
            print("Invalid ID")

    except ValueError:
        print("Please enter a valid number")

# Main Menu
def main():
    load_expenses()

    while True:
        print("\n" + "=" * 40)
        print("      PERSONAL EXPENSE TRACKER")
        print("=" * 40)
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category Summary")
        print("5. Monthly Report")
        print("6. Delete Expense")
        print("7. Exit")

        choice = input("\nEnter Choice: ")

        if choice == '1':
            add_expense()

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            total_expense()

        elif choice == '4':
            category_summary()

        elif choice == '5':
            monthly_report()

        elif choice == '6':
            delete_expense()

        elif choice == '7':
            print("Thank You!")
            break

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
import json
import os

# Define file to store data
DATA_FILE = 'budget_tracker_data.json'

def load_data():
    """Load data from JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {'income': [], 'expenses': []}

def save_data(data):
    """Save data to JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_transaction(transaction_type):
    """Add an income or expense transaction."""
    category = input(f"Enter {transaction_type} category: ").strip()
    amount = float(input(f"Enter {transaction_type} amount: ").strip())
    
    data = load_data()
    
    transaction = {'category': category, 'amount': amount}
    if transaction_type == 'income':
        data['income'].append(transaction)
    elif transaction_type == 'expense':
        data['expenses'].append(transaction)
    
    save_data(data)
    print(f"{transaction_type.capitalize()} added successfully.")

def calculate_budget():
    """Calculate the remaining budget."""
    data = load_data()
    total_income = sum(item['amount'] for item in data['income'])
    total_expenses = sum(item['amount'] for item in data['expenses'])
    remaining_budget = total_income - total_expenses
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Budget: ${remaining_budget:.2f}")

def analyze_expenses():
    """Provide insights on expenses."""
    data = load_data()
    expense_categories = {}
    
    for expense in data['expenses']:
        category = expense['category']
        amount = expense['amount']
        if category in expense_categories:
            expense_categories[category] += amount
        else:
            expense_categories[category] = amount
    
    print("Expense Analysis:")
    for category, total in expense_categories.items():
        print(f"Category: {category}, Total Spent: ${total:.2f}")

def menu():
    """Display the menu and handle user choices."""
    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Budget")
        print("4. Analyze Expenses")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_transaction('income')
        elif choice == '2':
            add_transaction('expense')
        elif choice == '3':
            calculate_budget()
        elif choice == '4':
            analyze_expenses()
        elif choice == '5':
            print("Exiting Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
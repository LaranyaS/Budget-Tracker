import json
import os

# File where budget data will be stored
BUDGET_FILE = "budget.json"

def load_budget():
    """
    Loads budget data from the budget.json file if it exists.
    If the file doesn't exist, return a default budget with 0 income and empty expenses.
    """
    if os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, "r") as f:
            return json.load(f)  # Load data from JSON file
    return {"income": 0, "expenses": []}  # Default structure if file not found

def save_budget(data):
    """
    Saves the budget data to budget.json file.
    """
    with open(BUDGET_FILE, "w") as f:
        json.dump(data, f, indent=2)  # Write JSON with indentation for readability

def display_budget(data):
    """
    Displays the current budget summary:
    - Income
    - Total expenses
    - Balance
    - Expense breakdown by category
    """
    print(f"\n💵 Monthly Income: ${data['income']}")
    total_expense = sum(item["amount"] for item in data["expenses"])  # Calculate total expenses
    print(f"💸 Total Expenses: ${total_expense}")
    print(f"💰 Balance: ${data['income'] - total_expense}")  # Remaining balance

    # Show breakdown of expenses if there are any
    if data["expenses"]:
        print("\n📂 Expense Breakdown:")
        for i, item in enumerate(data["expenses"], 1):
            print(f"{i}. {item['category']} - ${item['amount']}")

def set_income(data):
    """
    Allows the user to set/update their monthly income.
    """
    try:
        data["income"] = float(input("Enter your monthly income: $"))  # Convert input to number
        print("Income updated.")
    except ValueError:
        print("Invalid amount.")  # Handle non-numeric input

def add_expense(data):
    """
    Allows the user to add an expense with category and amount.
    """
    try:
        category = input("Enter expense category: ").strip()
        amount = float(input("Enter amount: $"))  # Convert input to number
        data["expenses"].append({"category": category, "amount": amount})  # Add expense to list
        print("Expense added.")
    except ValueError:
        print("Invalid amount.")

def delete_expense(data):
    """
    Allows the user to delete an expense by selecting its number from the list.
    """
    display_budget(data)  # Show expenses before deleting
    try:
        i = int(input("Enter expense number to delete: ")) - 1  # Get index (1-based input)
        if 0 <= i < len(data["expenses"]):  # Ensure input is valid
            deleted = data["expenses"].pop(i)  # Remove expense
            print(f"Deleted expense: {deleted['category']} - ${deleted['amount']}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Invalid input.")

def main():
    """
    Main program loop:
    - Load budget
    - Show menu
    - Let user view, add, delete expenses or set income
    - Save data before exiting
    """
    data = load_budget()  # Load existing data or create new

    while True:
        # Show menu options
        print("\n📊 Budget Overview Menu:")
        print("1. View budget summary")
        print("2. Set monthly income")
        print("3. Add an expense")
        print("4. Delete an expense")
        print("5. Exit")

        try:
            choice = input("Choose an option: ").strip()
            if choice == "1":
                display_budget(data)
            elif choice == "2":
                set_income(data)
            elif choice == "3":
                add_expense(data)
            elif choice == "4":
                delete_expense(data)
            elif choice == "5":
                save_budget(data)  # Save before exiting
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
        except KeyboardInterrupt:
            # If user presses Ctrl+C, save data and exit gracefully
            print("\nInterrupted. Saving and exiting...")
            save_budget(data)
            break

# Entry point: only runs if the file is executed directly
if __name__ == "__main__":
    main()

import json
import os

BUDGET_FILE = "budget.json"

def load_budget():
    if os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, "r") as f:
            return json.load(f)
    return {"income": 0, "expenses": []}

def save_budget(data):
    with open(BUDGET_FILE, "w") as f:
        json.dump(data, f, indent=2)

def display_budget(data):
    print(f"\n💵 Monthly Income: ${data['income']}")
    total_expense = sum(item["amount"] for item in data["expenses"])
    print(f"💸 Total Expenses: ${total_expense}")
    print(f"💰 Balance: ${data['income'] - total_expense}")

    if data["expenses"]:
        print("\n📂 Expense Breakdown:")
        for i, item in enumerate(data["expenses"], 1):
            print(f"{i}. {item['category']} - ${item['amount']}")

def set_income(data):
    try:
        data["income"] = float(input("Enter your monthly income: $"))
        print("Income updated.")
    except ValueError:
        print("Invalid amount.")

def add_expense(data):
    try:
        category = input("Enter expense category: ").strip()
        amount = float(input("Enter amount: $"))
        data["expenses"].append({"category": category, "amount": amount})
        print("Expense added.")
    except ValueError:
        print("Invalid amount.")

def delete_expense(data):
    display_budget(data)
    try:
        i = int(input("Enter expense number to delete: ")) - 1
        if 0 <= i < len(data["expenses"]):
            deleted = data["expenses"].pop(i)
            print(f"Deleted expense: {deleted['category']} - ${deleted['amount']}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Invalid input.")

def main():
    data = load_budget()

    while True:
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
                save_budget(data)
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
        except KeyboardInterrupt:
            print("\nInterrupted. Saving and exiting...")
            save_budget(data)
            break

if __name__ == "__main__":
    main()

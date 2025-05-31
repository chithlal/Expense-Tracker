import csv

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.budget = None
        self.load_expenses()
        

    def load_expenses(self, filename="expenses.csv"):
        try: 
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                self.expenses = []
                for row in reader:
                # Convert amount back to float
                    expense = {
                    'amount': float(row['amount']),
                    'category': row['category'],
                    'description': row['description']
                    }
                    self.expenses.append(expense)
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with empty expenses.")
            self.expenses = []
        except ValueError as e:
            print(f"Error converting amount to number: {e}")
            self.expenses = []

    def add_expense(self, amount, category, description=""):
        if self.budget is not None:
            if amount > (self.budget - sum(exp['amount'] for exp in self.expenses)):
                print(f"Warning: Expense (${amount:.2f}) exceeds remaining budget (${self.budget:.2f}).")
    
        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }
        self.expenses.append(expense)
        if self.budget is not None:
            self.set_budget(amount)

    def set_budget(self, budget):
        self.budget = budget

    def track_budget(self):
        total_expense = sum(exp['amount'] for exp in self.expenses)
        if self.budget is not None:
            remaining_budget = self.budget - total_expense
            return f"Total expenses: {total_expense}, Remaining budget: {remaining_budget}"
        else:
            return f"Total expenses: {total_expense}, No budget set."

    def save_expenses(self, filename="expenses.csv"):
        with open(filename, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=['amount', 'category', 'description'])
            writer.writeheader()  # Write column headers
            writer.writerows(self.expenses)

    def print_expenses(self):
        print("===========================")
        for expense in self.expenses:
            amount = expense.get('amount')
            category = expense.get('category')
            description = expense.get('description', '')
            if description:
                print(f"Amount: ${amount:.2f}, Category: {category}, Description: {description}")
            else:
                print(f"Amount: ${amount:.2f}, Category: {category}")
        print("===========================")



def print_expenses(amount, category, description=None):
    print("===========================\n")
    if description:
        print(f"Amount: ${amount:.2f}\nCategory: {category}\nDescription: {description}\n")
    else:
        print(f"Amount: ${amount:.2f}\nCategory: {category}\n")
    print("===========================\n")
    
    
def print_expense(expense):
    amount = expense.get('amount')
    category = expense.get('category')
    description = expense.get('description')
    if description:
        print(f"Amount: ${amount:.2f}\nCategory: {category}\nDescription: {description}")
    else:
        print(f"Amount: ${amount:.2f}\nCategory: {category}")
    
def main():
    tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Track budget")
        print("4. Save expenses")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                description = input("Enter description (optional): ")
                tracker.add_expense(amount, category, description)
                print_expenses(amount, category, description)
                print("Expense added.")
            except ValueError:
                print("Invalid amount.")
        elif choice == "2":
            tracker.print_expenses()
            if not tracker.expenses:
                print("No expenses recorded.")
        elif choice == "3":
            if tracker.budget is None:
                try:
                    budget = float(input("Set your budget: "))
                    tracker.set_budget(budget)
                except ValueError:
                    print("Invalid budget.")
            print(tracker.track_budget())
        elif choice == "4":
            tracker.save_expenses()
            print("Expenses saved.")
        elif choice == "5":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
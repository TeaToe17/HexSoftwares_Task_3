class Expense:

    def __init__(self, item: str, amount: int, category: str):
        self.item = item
        self.amount = amount
        self.category = category

    def __str__(self):
        return f"{self.item}"


class ExpenseTracker:

    def __init__(self):
        self.expenses = []
    
    def display_expenses(self):
        print("Item  Amount  Category")
        amount_sum = 0
        for expense in self.expenses:
            amount_sum += expense.amount
            print(f"{expense.item}  {expense.amount}  {expense.category}")
        print(f"Total: {amount_sum}")

    def add_expense(self, expense):
        self.expenses.append(expense)
    
    def track_category(self, category):
        category = category.lower()
        selected_category = [expense for expense in self.expenses if category == expense.category.lower()]
        amount_sum = 0
        for expense in selected_category:
            amount_sum += expense.amount
            print(f"{expense.item}  {expense.amount}  {expense.category}")
        print(f"Total: {amount_sum}\n")


def track_expense():
    categories = ["food","jewelry","clothes","transport","communication"]
    more_expenses = ""
    more_expenses = more_expenses.lower()
    Tracker = ExpenseTracker()
    while more_expenses != "no":
        for index,cat in enumerate(categories):
            print(f"category_number:{index+1} for {cat}\n")
        print("Type your expenses in this format: item, amount, catagory_number \n e.g tesla, 3000, 4\n")
        expense = input("what did you buy? ")
        more_expenses = input("Did you anything else? (yes/no) ").lower().strip()
        print("\n")
        if expense:
            item, amount, category = expense.split(",")
            amount = int(amount)
            category = categories[int(category)-1]
            expense = Expense(item, amount, category)
            Tracker.add_expense(expense)

    print("ALL EXPENSES")    
    Tracker.display_expenses()
    print("\n")

    for cat in categories:
        print(f"EXPENSE ACCORDING  TO CATEGORY:{cat}")
        Tracker.track_category(cat)


if __name__ == "__main__":
    track_expense()


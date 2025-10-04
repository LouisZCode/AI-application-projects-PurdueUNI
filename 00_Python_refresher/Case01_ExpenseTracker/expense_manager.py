class ExpenseTracker:
    def __init__(self, csv_path='expenses.csv'):
        self.csv_path = csv_path
        self.df = self.load_or_create_csv()
        self.budget = self.load_budget()

    def add_expense(self, ...):
        # Method 1
        pass

    def view_expenses(self):
        # Method 2
        pass

    # ... all 7 core methods ...

    def save(self):
        # Explicit save
        self.df.to_csv(self.csv_path, index=False)
# STEPS
# TO-DO 1: Function to ask the user for the Expense Details
#Input: Year of Expense, Category, amount, description
#Output: save into a list of dictionaries,
#use datetime to save the time and date.
# example: {'date': '2024-09-18', 'category': 'Food', 'amount': 15.50,
# 'description': 'Lunch with friends'}

import pandas as pd

class Expensetracker:

    def __init__(self) -> None:
        pass

    def add_expense(self, date_input, category_input, amount_input, description_input):
        pd.read_csv('expenses.csv')

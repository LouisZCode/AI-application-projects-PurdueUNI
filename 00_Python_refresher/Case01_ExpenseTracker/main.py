import gradio as gr
from datetime import datetime
import pandas as pd
import os
import time


MONTHLY_BUDGET = 0
CSV_NAME = "expenses.csv"



#Make an Expense Tracker that can:
# -Categorize the Expense
# -Set Monthly Budgets
# -Save and Load Expense Data
# -Menu driven Interface


# TO-DO 2: Function to retrieve and display all stored expenses
#Input: Click!
#Output: Display all expenses, if incomplete, skip it.
#Notes:   If no entries, elif entries - missing part, skip or notify!

# TO-DO 3: Function that sets and tracks a monthly budget
#Input: Total ammount they want; make the ammount a unified number (float)
#Input: Click!
#Output, sum all the expenses so far, warn if above or below budget.

# TO-DO 4: Save and Load Expenses on CSV     Pandas*
#Input: program starts
#Output, loads the CSV into the program.
#If no CSV, create an empty one.
#Input: click "Save the expenses"
#Output: updates CSV file.

# TO-DO 5: Create an interactive Menu.
# Step 1: Create the function that will handle saving the expense


#When starting, we need to check if the .csv even exists:
if os.path.exists(CSV_NAME):
    print('csv with expenses exists, loading...\n')
else:
    #We create a new empty DataFrame withthe columns we want:
    expenses_df = pd.DataFrame(columns=['date', 'category', 'amount', 'description'])
    print('No DataFrame, creating a new one..!')
    time.sleep(1)
    #and we save it in a new created .csv document
    expenses_df.to_csv(CSV_NAME, index=False)
    print('created a new .csv document')

print("Welcome to your Expense tracker!!")
print('--------------------------------------------\n')
print('Actions:\n01: Add an Expense\n')

user_decision = input("Please select the action you want to take: ")

# TO-DO 1: Function to ask the user for the Expense Details
#Input: Year of Expense, Category, amount, description
#Output: save into a list of dictionaries,
#use datetime to save the time and date.
# example: {'date': '2024-09-18', 'category': 'Food', 'amount': 15.50,
# 'description': 'Lunch with friends'}

def add_expense(date, category, ammount, description):
    #we load the cvs as a DataFrame into memory
    df = pd.read_csv(CSV_NAME)
    #We add the new row as a list in a dictionary, first by saving the row as a dictionary in a lit
    new_row = pd.DataFrame([{'date': date, 'category': category, 'ammount': ammount, 'description': description}])
    #... then we add it to the dataframe we loaded:
    df = pd.concat([df, new_row], ignore_index=True)  #the Ignore Index is important, as it 'continues' the indexes, not restart them from 0 in a weird place

    #lastly, we save is as a new .csv
    df.to_csv(CSV_NAME)



if user_decision == '01':
    #We get the Date row information:
    date = datetime.today().strftime('%Y-%m-%d')
    print(f"this will be added with thedate: {date}")
    category = input('choose your category:\n')
    ammount = input('choose your ammount:\n')
    description = input('choose your description:\n')
    add_expense(date, category, ammount, description)
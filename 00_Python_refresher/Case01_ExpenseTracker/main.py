import gradio as gr
from datetime import datetime
import pandas as pd
import os
import time

CSV_NAME = "expenses.csv"

# TO-DO 5: Create an interactive Menu.

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
    print('created a new .csv document\n')
    time.sleep(1)


#Same for the budget data:
if os.path.exists('budget.txt'):
    print('Budget data exists, loading...\n')
else:
    print('No budget, creating a new one..!')
    time.sleep(1)
    #We create a new empty TXT with the budget as 0:
    with open('budget.txt', 'w') as budget:
        budget.write('0')

    print('created a new budget document\n')
    time.sleep(1)



with gr.Blocks() as demo:
    gr.Markdown("#Welcome to Luis Expense Tracker")

    with gr.Column():
        add_button = gr.Button("Add an Expense")
        show_button = gr.Button("Show Expenses")
        set_button = gr.Button("Set a monthly Budge")
        track_button = gr.Button("Track the Budget")

demo.launch()


print('\n\nActions:\n01: Add an Expense\n02: Show Expenses\n03: Set a NEW Budget\n04: Track current Budget\n05: Exit')

user_decision = input("\nPlease select the action you want to take: ")

# TO-DO 1: Function to ask the user for the Expense Details
#Input: Year of Expense, Category, amount, description
#Output: save into a list of dictionaries,
#use datetime to save the time and date.
# example: {'date': '2024-09-18', 'category': 'Food', 'amount': 15.50,
# 'description': 'Lunch with friends'}

def add_expense(date, category, amount, description):
    #we load the cvs as a DataFrame into memory
    df = pd.read_csv(CSV_NAME)
    #We add the new row as a list in a dictionary, first by saving the row as a dictionary in a lit
    new_row = pd.DataFrame([{'date': date, 'category': category, 'amount': amount, 'description': description}])
    #... then we add it to the dataframe we loaded:
    df = pd.concat([df, new_row], ignore_index=True)  #the Ignore Index is important, as it 'continues' the indexes, not restart them from 0 in a weird place

    #lastly, we save is as a new .csv
    df.to_csv(CSV_NAME, index=False)

def show_data():
    #we get the csv and print it to see
    df = pd.read_csv(CSV_NAME)
    print(df)

#03
def set_budget(new_budget):
    with open('budget.txt', 'w') as budget:
        budget.write(str(new_budget))
    print(f'your new budget is now: ${new_budget}!')
        

#04
def track_budget():
    #We get a hold of the value in the Budget Tracker:
    with open('budget.txt', 'r') as budget_value:
        budget = int(budget_value.read())

    #We get a sum of the total expensed in the csv:
    df = pd.read_csv(CSV_NAME)
    amounts = df['amount'].sum()
    costs = amounts


    #We compare both!
    if budget == 0:
        print('You have not set a budget yet! all is ok')
    
    elif budget > costs:
        print(f"You have a budget of: {budget}\nYou have a cost so far of {costs}\n\nAll safe still, keep enjoying!")
    
    elif budget < costs:
        print(f"You had a budget of: {budget}\nYou have a cost so far of {costs}\n\nDANGER, stop enjoying!")
    else:
        print('Both have the same value, stop spending now')


if user_decision == '01':
    #We get the Date row information:
    date = datetime.today().strftime('%Y-%m-%d')
    print(f"this will be added with thedate: {date}")
    category = input('choose your category:\n')
    amount = input('choose your ammount:\n')
    description = input('choose your description:\n')
    add_expense(date, category, amount, description)


# TO-DO 2: Function to retrieve and display all stored expenses
#Input: Click!
#Output: Display all expenses, if incomplete, skip it.
#Notes:   If no entries, elif entries - missing part, skip or notify!

elif user_decision == "02":
    show_data()

# TO-DO 3: Function that sets and tracks a monthly budget
#Input: Total ammount they want; make the ammount a unified number (float)
#Input: Click!
#Output, sum all the expenses so far, warn if above or below budget.

elif user_decision == "03":
    budget = input('What is the new budget you want to have?\n')
    new_budget = str(budget)
    set_budget(new_budget)

elif user_decision == "04":
    track_budget()

elif user_decision == '05':
    play = False
    print("Perfect, thanks for using the tracker!")
    exit()

else:
    print('Sorry I did not understand that one, please try again')
import gradio as gr
from datetime import datetime
import pandas as pd


MONTHLY_BUDGET = 0
expense_list = []

def main():




#Make an Expense Tracker that can:
# -Categorize the Expense
# -Set Monthly Budgets
# -Save and Load Expense Data
# -Menu driven Interface

# STEPS
# TO-DO 1: Function to ask the user for the Expense Details
#Input: Year of Expense, Category, amount, description
#Output: save into a list of dictionaries,
#use datetime to save the time and date.
# example: {'date': '2024-09-18', 'category': 'Food', 'amount': 15.50,
# 'description': 'Lunch with friends'}

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

    expenses_list = []

        expense = {
            'date': date_str,
            'category': category,
            'amount': float(amount),
            'description': description
        }

        expenses_list.append(expense)

        return f"✅ Expense added!\n📅 Date: {date_str}\n📊 Total expenses: {len(expenses_list)}"


    with gr.Blocks() as demo:
        gr.Markdown("# 💰 Personal Expense Tracker")
        gr.Markdown("### Main Menu")

        with gr.Row():
            btn_add = gr.Button("➕ Add Expense", variant="primary")

        with gr.Column(visible=False) as panel_add:
            gr.Markdown("### Enter Expense Details")

            date_input = gr.DateTime(
                label="Date",
                value=datetime.now(),
                include_time=False
            )

            category_input = gr.Dropdown(
                choices=["Food", "Transportation", "Entertainment", "Utilities", "Healthcare", "Other"],
                label="Category"
            )

            amount_input = gr.Number(label="Amount ($)", value=0.0)
            description_input = gr.Textbox(label="Description", lines=2)

            with gr.Row():
                submit_btn = gr.Button("💾 Save Expense", variant="primary")
                back_btn = gr.Button("⬅️ Back to Menu")

            output_msg = gr.Textbox(label="Status", interactive=False)

        btn_add.click(lambda: gr.Column(visible=True), outputs=panel_add)
        submit_btn.click(add_expense, [date_input, category_input, amount_input, description_input], output_msg)
        back_btn.click(lambda: gr.Column(visible=False), outputs=panel_add)

    demo.launch()


if __name__ == "__main__":
    main()

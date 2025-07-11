import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from .transaction import Transaction


class FinanceTracker():
    def __init__(self):
        self.transactions = [] # To hold all the transactions
        
    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)
        
    def view_transactions(self):
        if not self.transactions:
            print('No Transactions To Display')
        else:
            print('-' * 13, "All Transactions", '-' * 14)
            for transaction in self.transactions:
                transaction.showtransaction()
            print('-' * 10, "End of All Transactions", '-' * 10, '\n')
                
    def total_income(self):
        income = sum([transaction.amount for transaction in self.transactions if transaction.amount > 0])
        return income
    
    def total_expenses(self):
        expenses = sum([transaction.amount for transaction in self.transactions if transaction.amount < 0])
        return expenses
    
    def total_savings(self):
        return self.total_income() + self.total_expenses()
    
    def filter_by_category(self, category):
        if category not in Transaction.categories:
            category = 'Miscellaneous'
            
        filtered_transactions = [transaction for transaction in self.transactions if category==transaction.category]
        return filtered_transactions
    
    def get_transaction_details(self):
        user_date = input("Enter transaction date (DD-MM-YYYY): ")
        while True:
            try:
                user_amount = int(input("Enter transaction amount (positive for income, negative for expenses): "))
                break
            except ValueError:
                print("Please enter a valid numeric amount.")
                
        user_description = str(input("Enter transaction description: "))
        user_category = str(input(f'Enter transaction category (Choose only from the predefined categories) {Transaction.categories}: '))
        user_description = user_description if user_description else 'No Description'
        user_category = user_category if user_category else 'Miscellaneous'
        t = Transaction(user_date, user_amount, user_description, user_category)
        self.add_transaction(t)
        print('Transaction Added Succesfully!')
        
    def monthly_summary(self):
        monthly_data = {}
        
        for transaction in self.transactions:
            month = transaction.date.strftime('%m-%y')
            
            if month not in monthly_data:
                monthly_data[month] = {'income': 0, 'expenses': 0, 'savings': 0}
                
            if transaction.amount > 0:
                monthly_data[month]['income'] += transaction.amount
                
            if transaction.amount < 0:
                monthly_data[month]['expenses'] += transaction.amount
                
        for month in monthly_data:
            monthly_data[month]['savings'] = monthly_data[month]['income'] + monthly_data[month]['expenses']
            
        summary_df = pd.DataFrame.from_dict(monthly_data, orient='index')
        return summary_df
    
    def visualize_monthly_summary(self):
        monthly_df = self.monthly_summary()
        
        monthly_df[['income', 'expenses']].plot(kind='bar', figsize=(10, 6), stacked=True)
        
        plt.title('Income Vs Expenses By Month')
        plt.xlabel('Month')
        plt.ylabel('Amount')
        plt.show()
        
    def visualize_categorical_spendings(self):
        category_expenses = {}
        
        for transaction in self.transactions:
            if transaction.amount < 0:
                if transaction.category not in category_expenses:
                    category_expenses[transaction.category] = 0
                    
                category_expenses[transaction.category] += abs(transaction.amount)
        labels = category_expenses.keys()
        values = category_expenses.values()
        
        plt.figure(figsize=(10, 6))
        plt.title("Categorical Expenses")
        plt.pie(values, labels=labels, autopct='%1.f%%',startangle=140)
        plt.show()
        
    def export_csv(self):
        transactions_data = []
        for transaction in self.transactions:
            transactions_data.append([transaction.date.strftime('%d-%m-%y'), transaction.amount, transaction.description, transaction.category])
        df = pd.DataFrame(transactions_data, columns=['Date', 'Amount', 'Description', 'Category'])
        df.to_csv('data/transactions.csv', index=False)
        print('transactions.csv created succesfully!')
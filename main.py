from app.financetracker import FinanceTracker 
from app.transaction import Transaction

def main():
    tracker = FinanceTracker()
    
    while True:
        print("\n1. Add Transaction")
        print("2. View Transactions")
        print("3. View Summary")
        print("4. Monthly Data Report")
        print("5. Monthly Visualized Data")
        print("6. Export Data to CSV")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            tracker.get_transaction_details()
        elif choice == '2':
            tracker.view_transactions()
        elif choice == '3':
            print(f"Total Income: {tracker.total_income()}")
            print(f"Total Expenses: {tracker.total_expenses()}")
            print(f"Total Savings: {tracker.total_savings()}")
        elif choice== '4':
            print("Monthly Data Report: \n", tracker.monthly_summary())
        elif choice == '5':
            tracker.visualize_monthly_summary()
            tracker.visualize_categorical_spendings()
        elif choice == '6':
            tracker.export_csv()
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")     
main()


import pandas as pd

class Transaction():
    rupee_symbol = '\u20B9'
    categories = ['Food', 'Rent', 'Entertainment', 'Clothing', 'Travel', 'Health', 'Miscellaneous']
    def __init__(self, date, amount, description='No Description', category='Miscellaneous'):
        try:
            if isinstance(amount, (int, float)):
                self.date = pd.to_datetime(date, format='%d-%m-%Y')
                self.amount = amount
                self.description = description
                # Validate category
                if category not in Transaction.categories:
                    print(f"Warning: Invalid category '{category}'. Defaulting to 'Miscellaneous'.")
                    self.category = 'Miscellaneous'
                else:
                    self.category = category
            else:
                raise ValueError("Amount should be a Float or Integer type only.")
        except ValueError as ex:
            print(ex)

    def __repr__(self):
        return f"Transaction(date={self.date.strftime('%d-%m-%y')}, amount={self.amount}{Transaction.rupee_symbol}, description={self.description}, category={self.category})"
        
    def showtransaction(self):
        print(f"{self.date.strftime('%d-%m-%y')}: {self.amount }{Transaction.rupee_symbol} - {self.description} - {self.category}")
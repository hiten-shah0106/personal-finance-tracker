import datetime

class Transaction():
    rupee_symbol = '\u20B9'
    categories = ['Food', 'Rent', 'Entertainment', 'Clothing', 'Travel', 'Health', 'Miscellaneous']
    
    def __init__(self, date, amount, description='No Description', category='Miscellaneous'):
        try:
            if isinstance(amount, (int, float)):
                if isinstance(date, str):
                    self.date = datetime.datetime.strptime(date, '%d-%m-%Y').date()
                elif isinstance(date, datetime.date):
                    self.date = date 
                else:
                    raise ValueError("Date must be a string or datetime object.")
                
                self.amount = amount
                self.description = description
                
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
        return f"Transaction(date={self.date.strftime('%d-%m-%Y')}, amount={self.amount}{Transaction.rupee_symbol}, description={self.description}, category={self.category})"

    def showtransaction(self):
        print(f"{self.date.strftime('%d-%m-%Y')}: {self.amount}{Transaction.rupee_symbol} - {self.description} - {self.category}")

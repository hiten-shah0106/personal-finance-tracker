import sqlite3
import datetime
from .transaction import Transaction

class Database:
    def __init__(self):
        self.create_table()
    
    def create_connection(self):
        try:
            self.connection = sqlite3.connect('./data/transactions.db')
        except Exception as ex:
            print(f"Error creating connection: {ex}")
        return self.connection
    
    def create_cursor(self):
        try:
            self.cursor = self.connection.cursor()
        except Exception as ex:
            print(f"Error creating cursor: {ex}")
        return self.cursor
    
    def create_table(self):
        conn = self.create_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT, 
                amount REAL NOT NULL,
                description TEXT,
                category TEXT
            )
        ''')
        
        conn.commit()
        cursor.close()
        conn.close()

    def add_transaction(self, transaction: Transaction):
        conn = self.create_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO transactions (date, amount, description, category) 
                VALUES (?, ?, ?, ?)
            ''', (transaction.date.strftime('%Y-%m-%d'), transaction.amount, transaction.description, transaction.category))
            
            conn.commit()
        except Exception as ex:
            print(f"Error adding transaction: {ex}")
        finally:
            cursor.close()
            conn.close()

    def get_transactions(self):
        conn = self.create_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM transactions')
        rows = cursor.fetchall()

        transactions = []
        for row in rows:
            transaction_id, date, amount, description, category = row
            date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            t = Transaction(date, amount, description, category)  
            transactions.append(t)

        return transactions

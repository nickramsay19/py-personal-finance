from flask import Flask, render_template, url_for, session, request, redirect, flash
from datetime import datetime

app = Flask(__name__)

class Transaction:
    def __init__(self, amount, date, name, category):
        self.amount = amount;
        self.date = date
        self.name = name
        self.category = category

transactions = []
transactions.append(Transaction(56, datetime(2015,5,17), 'Club Penguin Membership', 'NonEssential'))
transactions.append(Transaction(-330, datetime(2015,6,1), 'Rent', 'Essential'))
transactions.append(Transaction(-330, datetime(2015,6,8), 'Rent', 'Essential'))
transactions.append(Transaction(-330, datetime(2015,6,15), 'Rent', 'Essential'))

@app.route("/")
def dashboard():
    return render_template('dashboard.html', transactions=transactions, datetime=datetime)

@app.route("/transactions")
def viewTransactions():
    return render_template('transactions.html', transactions=transactions)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
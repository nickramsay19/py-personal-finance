from flask import Flask, render_template, url_for, session, request, redirect, flash
from datetime import datetime
import pandas as pd

from model import Model, Transaction
model = Model()

from collections import OrderedDict

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template('dashboard.html', transactions=model.GetTransactions(), current=model.GetCurrentBalance())

@app.route("/transactions")
def viewTransactions():   
    return render_template('transactions.html', transactions=model.GetTransactions(), current=model.GetCurrentBalance())

@app.route("/spendingtracker")
def viewSpendingTracker():   
    return render_template('transactions.html', transactions=model.GetTransactions(), current=model.GetCurrentBalance())

@app.route("/upload", methods=['POST', 'GET'])
def viewUpload():   
    if request.method == 'GET':
        return render_template('upload.html')

    elif request.method == 'POST':
        # get file
        file = request.files['transactions_file']
        content = file.read()

        for line in content.splitlines():
            transaction = Transaction()
            for index, item in enumerate(str(line)[2:].split(',')):

                # Date
                if index == 0:
                    transaction.date = item
                elif index == 1:
                    transaction.amount = float(item[1:-1])
                elif index == 2:
                    transaction.name = item[:-1]
            
            # add transaction
            model.AddTransaction(transaction)

        # complete redirect to upload page
        return render_template('upload.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
from flask import Flask, render_template, url_for, session, request, redirect, flash
from datetime import datetime
import csv
from collections import OrderedDict

app = Flask(__name__)

class Transaction:
    def __init__(self, amount, date, name, category):
        self.amount = amount;
        self.date = date
        self.name = name
        self.category = category

def getTransactions():

    transactions = []

    reader = csv.DictReader(open('static/ANZ.csv'))

    for raw in reader:
        items = list(OrderedDict(raw).items())

        transactions.append(Transaction(float(items[1][1]), items[0][1], items[2][1], ''))

    return transactions

def getCurrent():

    reader = csv.DictReader(open('static/ANZ.csv'))

    for raw in reader:
        items = list(OrderedDict(raw).items())

        return Transaction(float(items[1][0]), items[0][0], '', '')

@app.route("/")
def dashboard():
    return render_template('dashboard.html', transactions=getTransactions(), current=getCurrent())

@app.route("/transactions")
def viewTransactions():   
    return render_template('transactions.html', transactions=getTransactions(), current=getCurrent())

@app.route("/spendingtracker")
def viewSpendingTracker():   
    return render_template('transactions.html', transactions=getTransactions(), current=getCurrent())

@app.route("/upload")
def viewUpload():   
    return render_template('upload.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
import mysql.connector
from datetime import datetime
from collections import OrderedDict
import csv

'''
# Setup DB Connection
db = mysql.connector.connect(
  host="remotemysql.com",
  user="pxHpXYXX51",
  passwd="ASlM7zdZoV",
  database="pxHpXYXX51"
)
cursor = db.cursor()


cursor.execute("SELECT id, amount, date, name FROM Transaction;")
Users = []
for user in list(cursor.fetchall()):
    Users.append(User(str(user[0]), str(user[1])))
    
'''
class Transaction:
    def __init__(self, id=0, amount=0.0, date='', name='', category=''):
        self.id = id
        self.amount = amount;
        self.date = date
        self.name = name
        self.category = category


class Model:
    def __init__(self):
        self.Transactions = []

        # Setup DB Connection
        self.db = mysql.connector.connect(
          host="remotemysql.com",
          user="CrepRHXvS9",
          passwd="ASlM7zdZoV",
          database="CrepRHXvS9"
        )
        self.cursor = self.db.cursor()

    def __updateTransactions(self):

        # read db
        self.cursor.execute("SELECT amount, date, name FROM Transaction;")
        for transaction in list(self.cursor.fetchall()):
            print(transaction[0])
            self.Transactions.append(Transaction(amount=transaction[0], date=transaction[1], name=transaction[2]))
            


        # update transactions
        
        '''
        reader = csv.DictReader(open('static/ANZ.csv'))

        for raw in reader:
            items = list(OrderedDict(raw).items())

            transactions.append(Transaction(0, float(items[1][1]), items[0][1], items[2][1], ''))

        self.Transactions = transactions
        '''
            

    def GetTransactions(self):
        self.__updateTransactions()
        return self.Transactions
        

    def AddTransaction(self, transaction):
          
        # INSERT INTO `Transaction` (`id`, `amount`, `date`, `name`) VALUES (NULL, '-50', '2019-09-01', 'my purchase');
        # add to db
        self.cursor.execute("INSERT INTO `Transaction` (`id`, `amount`, `name`) VALUES (NULL, \'" + str(transaction.amount) + "\', \'" + str(transaction.name) + "\');")

        self.__updateTransactions

    def getTransactions(self):
        pass
    

    def GetCurrentBalance(self):

        reader = csv.DictReader(open('static/ANZ.csv'))

        for raw in reader:
            items = list(OrderedDict(raw).items())

        return Transaction(0, float(items[1][0]), items[0][0], '', '')

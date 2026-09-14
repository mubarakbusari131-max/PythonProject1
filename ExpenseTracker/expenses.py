import json
import os
USER_FILE = 'users.json'
EXPENSES_FILE = 'expenses.json'

def save_user(user_list, filename: str =USER_FILE):
    with open(filename,'w') as f:
        json.dump([u.to_dict() for u in user_list ],f, indent=2)

def load_user(filename=USER_FILE):
    if not os.path.exists(filename):
        return []
    with open(filename,'r') as f:
        data = json.load(f)
    return [User.from_dict(d) for d in data]

def save_expense(expense_list, filename: str =EXPENSES_FILE):
    with open(filename,'w') as f:
        json.dump([e.to_dict() for e in expense_list ],f, indent=2)

def load_expense(filename=EXPENSES_FILE):
    if not os.path.exists(filename):
        return []
    with open(filename,'r') as f:
        data = json.load(f)
    return [Expenses.from_dict(d) for d in data]

class Expenses:
    def __init__(self,name,amount,category,dete,description):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = dete
        self.description = description

    def __str__(self):
        return f'{self.name}  {self.amount}  {self.category}  {self.date}  {self.description}\n'

    def to_dict(self):
        return {"name": self.name,"amount": self.amount,"category": self.category,"date": self.date,"description": self.description}

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'],data['amount'],data['category'],data['date'],data['description'])

class User:
    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password = password

    def __str__(self):
        return f'{self.email} {self.username} {self.password}'

    def to_dict(self):
        return {"email": self.email,"username": self.username,"password": self.password}

    @classmethod
    def from_dict(cls, data):
        return cls(data["email"],data["username"],data["password"])


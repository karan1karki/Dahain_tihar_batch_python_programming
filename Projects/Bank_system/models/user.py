class User:

    def __init__(self, username, balance=0):
        self.username = username
        self.balance = balance

    def __str__(self):
        return f"{self.username} - Balance: {self.balance}"
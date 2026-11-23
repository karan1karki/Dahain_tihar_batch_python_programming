from datetime import datetime

class Transaction:

    def __init__(self, sender, receiver, amount):

        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.date = str(datetime.now())

    def to_dict(self):

        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount,
            "date": self.date
        }
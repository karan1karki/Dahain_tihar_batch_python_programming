from utils.file_handler import read_json, write_json
import random

def tranaction_code ():
    words = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
    word_random = random.choices(words, k=8)

    result = "".join(word_random)

    return result
class Account:

    def deposit(self, username, amount):

        users = read_json("Bank_system/auth/users.json")

        users[username]["balance"] += amount

        write_json("Bank_system/auth/users.json", users)

        transactions =  read_json("Bank_system/account/transactions.json")

        transactions.append ({
            "username": username,
            "type" : "Credit",
            "code" : tranaction_code(),
            "amount" : amount
        })

        write_json("Bank_system/account/transactions.json", transactions)
    def withdraw(self, username, amount):

        users = read_json("Bank_system/auth/users.json")

        if users[username]["balance"] >= amount:

            users[username]["balance"] -= amount

            write_json("Bank_system/auth/users.json", users)

            transactions =  read_json("Bank_system/account/transactions.json")

            transactions.append ({
                "username": username,
                "type" : "Debit",
                "Code" : tranaction_code(),
                "amount" : amount
            })

            write_json("Bank_system/account/transactions.json", transactions)

            return True

        return False
    
    def transfer(self ,sender, receiver, amount):

        users = read_json("Bank_system/auth/users.json")

        if users[sender]["balance"] >= amount:

            users[sender]["balance"] -= amount
            users[receiver]["balance"] += amount

            write_json("Bank_system/auth/users.json", users)

            return "Transfer Successful"

        return "Insufficient Balance"
    
    def get_balance(self, username):

        users = read_json("Bank_system/auth/users.json")
        
        return users[username]["balance"]
    
    def transaction_history(self, username):
       
       transactions = read_json("Bank_system/account/transactions.json")

       user_transactiions = []

       for transaction in transactions :
        if transaction["username"] == username :
            user_transactiions.append(transaction)
        
        return user_transactiions


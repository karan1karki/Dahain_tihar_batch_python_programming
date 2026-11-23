from auth.auth import Auth
from account.accunt import Account
from loan.loan import Loan
from utils.helpers import show_bank_menu

auth = Auth()
account = Account()
loan = Loan()


current_user = None

def main_menu():
    print("\n===== BANK SYSTEM =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

def user_menu():
    show_bank_menu()

while True:

    if current_user is None:

        main_menu()
        choice = input("Choose option: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")

            print(auth.register(username, password))

        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")

            if auth.login(username, password):
                current_user = username
                print("Login Successful")
            else:
                print("Invalid Credentials")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

    else:

        user_menu()
        choice = input("Choose option: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            account.deposit(current_user, amount)
            print("Deposited successfully")

        elif choice == "2":
            amount = float(input("Enter amount: "))

            if account.withdraw(current_user, amount):
                print("Withdraw successful")
            else:
                print("Insufficient balance")

        elif choice == "3":
            receiver = input("Receiver username: ")
            amount = float(input("Enter amount: "))

            result = account.transfer(current_user, receiver, amount)
            print(result)

        elif choice == "4":
            balance = account.get_balance(current_user)
            history = account.transaction_history(current_user)
            print("Your Balance:", balance)
            print("History : ", history)

        elif choice == "5":
            amount = float(input("Loan amount: "))
            rate = float(input("Interest rate: "))
            months = int(input("Months: "))

            result = loan.apply_loan(current_user, amount, rate, months)
            print(result)

        elif choice == "6":
            amount = float(input("Loan amount: "))
            rate = float(input("Interest rate: "))
            months = int(input("Months: "))

            emi = loan.calculate_emi(amount, rate, months)
            print("Monthly EMI:", emi)

        elif choice == "7":
            current_user = None
            print("Logged out successfully")

        else:
            print("Invalid choice")
            
            
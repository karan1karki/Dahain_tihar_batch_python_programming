from datetime import datetime
# utils/helper.py

def is_valid_amount(amount):
    return amount > 0


def generate_transaction_id():
    return datetime.now().strftime("%Y%m%d%H%M%S")


def calculate_interest(principal, rate):
    return principal * rate / 100


def format_currency(amount):
    return f"NPR {amount:.2f}"

def show_bank_menu():
    print("\n===== BANK MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    print("4. Transaction History")
    print("5. Loan")
    print('6. EMI Loan')
    print("7. Logout")
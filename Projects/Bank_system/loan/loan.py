class Loan:

    def __init__(self):
        pass

    def apply_loan(self, username, principal, rate, months):
        return {
            "username": username,
            "loan": principal,
            "rate": rate,
            "months": months
        }

    def calculate_emi(self, principal, rate, months):

        r = rate / (12 * 100)

        emi = (
            principal * r * ((1 + r) ** months)
        ) / (((1 + r) ** months) - 1)

        return round(emi, 2)
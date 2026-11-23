class EMI:

    def __init__(self, loan_amount, interest_rate, months):
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.months = months

    def calculate(self):

        r = self.interest_rate / (12 * 100)

        emi = (
            self.loan_amount * r * ((1 + r) ** self.months)
        ) / (
            ((1 + r) ** self.months) - 1
        )

        return round(emi, 2)
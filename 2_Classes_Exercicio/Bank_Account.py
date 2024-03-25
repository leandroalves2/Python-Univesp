class Bank_Account():
    def __init__(self, number, owner, balance):
        self.Number = number
        self.Owner = owner
        self.Balance = balance

    def Deposit(self, deposit):
        self.Balance = self.Balance + deposit

    def Cashout(self, cashout):
        self.Balance = self.Balance - (cashout + 5.00)

    def __str__(self):
        return f"Cont: {self.Number}, Owner: {self.Owner}, accont amount: {self.Balance}"


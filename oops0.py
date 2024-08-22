class Account:
    def __init__(self,acc,bal):
        self.balance=bal
        self.account_no=acc
    def debit(self,amount):
        self.balance=self.balance-amount
    def credit(self,amount):
        self.balance+=amount
    def get_balance(self):
        return self.balance
acc1=Account(12345,100000)
print(acc1.balance,acc1.account_no)
acc1.debit(500)
print(acc1.balance,acc1.account_no)
acc1.debit(200)
print(acc1.get_balance())
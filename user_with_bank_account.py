
class BankAccount:
    bank_name = "Bank of Traci"
    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            self.balance = self.balance
        return self

    @classmethod
    def all_account_info(cls):
        for account in cls.all_accounts:
            account.display_account_info()


class User:
    def __init__(self, first_name, last_name, account_balance):
        self.first_name = first_name
        self.last_name = last_name
        # self.account_balance = account_balance
        self.account = BankAccount(int_rate=0.02, balance=account_balance)

    def make_withdrawal(self, amount):
        self.account.balance -= amount

    def display_user_balance(self):
        print(f"User:{self.first_name},Balance:{self.account.balance}")

    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount
        
        
bob = User("Bob", "Smith", 500)
print(bob.account.balance)

guido = User("Guido", "Parma", 1000)
print(guido.account.balance)


guido.make_withdrawal(100)
print(guido.account.balance)

guido.display_user_balance()

bob.transfer_money(guido, 100)
print(guido.account.balance)

bob.display_user_balance()









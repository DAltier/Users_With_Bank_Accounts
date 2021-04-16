class BankAccount:
    def __init__(self, name, int_rate, balance) :
        self.name = name
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount) :
        self.balance += amount
        return self

    def withdraw(self, amount) :
        self.balance -= amount
        return self
    
    def display_account_info(self) :
        print("Account balance", self.balance)
        return self

    def yield_interest(self) :
        self.balance += self.balance * self.int_rate
        return self

class User:
    def __init__(self, name, email) :
        self.name = name
        self.email = email
        self.accounts = []

    def add(self, account) :
        self.accounts.append(account)
        return self
    
    def make_deposit(self, account, amount) :
        for acc in self.accounts :
            if (acc.name == account) :
                self.accounts[self.accounts.index(acc)].deposit(amount)
        return self

    def make_withdrawal(self, account, amount) :
        for acc in self.accounts :
            if (acc.name == account) :
                self.accounts[self.accounts.index(acc)].withdraw(amount)
        return self

    def display_user_balance(self) :
        print(f"{self.name}'s accounts")
        for acc in self.accounts :
            print(f"Balance in {acc.name} account: {self.accounts[self.accounts.index(acc)].balance}")   
        return self

    def transfer_money(self, account_user, other_user, account_other_user, amount) :
        for acc in self.accounts :
            if (acc.name == account_user) :
                self.make_withdrawal(account_user, amount)
        for acc in other_user.accounts :
            if (acc.name == account_other_user) :
                other_user.make_deposit(account_other_user, amount)
        return self


alex = User("Alex", "alex@python.com").add(BankAccount("checking",0.4,0)).add(BankAccount("savings",0.2,0))
amy = User("Amy", "amy@python.com").add(BankAccount("checking",0.4,0)).add(BankAccount("savings",0.2,0))
james = User("James", "james@python.com").add(BankAccount("checking",0.4,900))

alex.make_deposit("checking", 200).make_deposit("checking", 500).make_deposit("savings", 50).make_withdrawal("checking", 100).display_user_balance()

amy.make_deposit("checking", 300).make_deposit("savings", 150).make_withdrawal("checking", 100).make_withdrawal("checking", 75).display_user_balance()

alex.transfer_money("checking", amy, "savings", 200)
alex.display_user_balance()
amy.display_user_balance()

james.transfer_money("checking", alex, "savings", 200)
alex.display_user_balance()
james.display_user_balance()

from abc import ABC ,abstractmethod
class BankAccount(ABC):
    def checkbalance(self):
        print("You can checkout your balance..")
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass

class SavingsAccount(BankAccount):
    def deposit(self):
        print("2 lakhs per day")
    def withdraw(self):
        print("1 lakh you can withdraw")

class ZeroAccount(BankAccount):
    def deposit(self):
        print("1 lakhs per day")
    def withdraw(self):
        print("50K lakh you can withdraw")

class CurrentAccount(BankAccount):
    def deposit(self):
        print("No limit")
    def withdraw(self):
        print("1 lakh you can withdraw")

class PensionAccount(BankAccount):
    def deposit(self):
        print("No deposit")
    def withdraw(self):
        print("40K per day")

class JointAccount(BankAccount):
    def deposit(self):
        print("only those 2 people can deposit")
    def withdraw(self):
        print("1-2 lakhs you can withdraw per day")


class SalaryAccount(BankAccount):
    def deposit(self):
        print("No limit")
    def withdraw(self):
        print("1 lakh you can withdraw")

print("----------ACHYUTH----------")
achyuth=SalaryAccount()
achyuth.checkbalance()
achyuth.deposit()
achyuth.withdraw()

print("----------HARISH----------")
harish=SavingsAccount()
harish.checkbalance()
harish.deposit()
harish.withdraw()

print("----------KARTHIKEYA----------")
karthikeya=PensionAccount()
karthikeya.checkbalance()
karthikeya.deposit()
karthikeya.withdraw()

print("----------SANDEEP----------")
sandeep=CurrentAccount()
sandeep.checkbalance()
sandeep.deposit()
sandeep.withdraw()

print("----------KRISHNA----------")
krishna=ZeroAccount()
krishna.checkbalance()
krishna.deposit()
krishna.withdraw()

print("----------RAM_KRISHNA----------")
ram_krishna=JointAccount()
ram_krishna.checkbalance()
ram_krishna.deposit()
ram_krishna.withdraw()







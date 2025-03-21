class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def add(self, amount):
        self.balance += amount
        print(f"На счет {self.account_number} зачислено {amount}. Новый баланс: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств на счете!")
        else:
            self.balance -= amount
            print(f"Со счета {self.account_number} снято {amount}. Новый баланс: {self.balance}")

#определение обьектов
account1 = BankAccount("228", 1000)
account2 = BankAccount("1337", 500)

account1.add(200)
account1.withdraw(1500)
account1.withdraw(300)

account2.add(100)
account2.withdraw(400)

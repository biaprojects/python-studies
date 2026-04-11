class Account:

    TAX = 10
    def __init__(self, name, balance=0):
        self.__name = name
        self.__balance = int(balance)

    # getters and setters
    @property
    def name(self):
        return self.__name

    @property
    def balance(self):
        return self.__balance


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("The amount to deposit must be higher than 0!")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            self.__balance -= amount + Account.TAX
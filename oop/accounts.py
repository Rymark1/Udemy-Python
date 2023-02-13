import datetime
import pytz


class Account:
    """Simple account class with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self.transaction_list = [(Account._current_time(), balance)]
        print(f"Account created for {self.name}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if amount > self.__balance:
            print("You don't have enough money in your account!")
        elif amount > 0:
            self.__balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))
        self.show_balance()

    def show_balance(self):
        print(f"Balance is {self.__balance}")

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print(f"{amount} {tran_type} on {date} (local time was {date.astimezone()}")


if __name__ == "__main__":
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    tim.withdraw(500)
    tim.withdraw(1000)
    tim.show_transactions()
    ryan = Account("Ryan", 800)
    ryan.__balance = 200
    ryan.deposit(100)
    ryan.withdraw(200)
    ryan.show_transactions()
    print(ryan.__dict__)
    ryan._Account__balance = 40
    ryan.show_balance()
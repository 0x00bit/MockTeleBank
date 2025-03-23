import datetime


class Client():
    def __init__(self, userid, name, balance=0, last_deposit=None, last_withdraw=None):
        self.userid = userid
        self.name = name,
        self.balance = balance
        self.last_deposit = last_deposit
        self.last_withdraw = last_withdraw
        self.transaction_history = []

    def deposit(self, amount):
        """Deposit method"""
        if amount > 0:
            self.balance += amount
            self.last_deposit = datetime.datetime.now().replace(microsecond=0)
            self._track_transaction("deposit", amount, self.last_deposit)
        else:
            print("The amount must to be a valid value")
            return None

    def withdraw(self, amount):
        """Withdraw method"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.last_withdraw = datetime.datetime.now().replace(microsecond=0)
            self._track_transaction("withdraw", amount, self.last_withdraw)
            return self.balance, self.last_withdraw
        else:
            print("The amount must ot be a valid value")
            return None

    def check_balance(self):
        """Method responsible to check the balance and your last transactions"""
        message = f"Your balance is ${self.balance}"
        # Filtering the last transaction of each type
        deposits = [t for t in self.transaction_history if t["type"] == "deposit"]
        withdrawals = [t for t in self.transaction_history if t["type"] == "withdraw"]
        # Getting the last transaction of each type
        last_deposit = deposits[-1]["date"] if deposits else "You did not do any transactions yet"
        last_withdraw = withdrawals[-1]["date"] if withdrawals else "You did not do any transactions yet"

        message += f" \nYour last deposit was: {last_deposit}"
        print(self.transaction_history)
        message += f" \nYour last withdraw was: {last_withdraw}"

        print(message)

    def _track_transaction(self, type, amount, date):
        """This method tracks any transation and save it in a log"""
        # Creating a "log" to track each transaction of the clients
        transaction = {
            "type": type,
            "amount": amount,
            "date": date
        }
        self.transaction_history.append(transaction)

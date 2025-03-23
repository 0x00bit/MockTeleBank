import datetime


class Client():
    def __init__(self, userid, name, balance=0, last_deposit=None, last_withdraw=None, transaction_historic=None):
        self.userid = userid
        self.name = name,
        self.balance = balance
        self.last_deposit = last_deposit
        self.last_withdraw = last_withdraw
        self.transaction_history = transaction_historic or []

    def deposit(self, amount):
        """Deposit method"""
        if amount > 0:
            self.balance += amount
            self.last_deposit = datetime.datetime.now().replace(microsecond=0)
            self._track_transaction("deposit", amount, self.last_deposit)
            return self.balance, self.last_deposit
        else:
            print("The amount must to be a valid value")
            return None

    def withdraw(self, amount):
        """Withdraw method"""
        # Check if the amount is greater than 0 and if it's not greater than the whole balance
        if amount > 0 and amount <= self.balance:
            self.balance -= amount  # Discount from the account
            self.last_withdraw = datetime.datetime.now().replace(microsecond=0)  # Save the last transaction's time
            self._track_transaction("withdraw", amount, self.last_withdraw)
            return self.balance, self.last_withdraw
        else:
            print("The amount must ot be a valid value")
            return None

    def check_balance(self):
        """Method responsible to check the balance and your last transactions"""
        message = f"Your balance is ${self.balance}\n"
        return message


    def _track_transaction(self, type, amount, date):
        """This method tracks any transation and save it in a log"""
        # Creating a "log" to track each transaction of the clients
        transaction = {
            "type": type,
            "amount": amount,
            "date": date
        }
        self.transaction_history.append(transaction)



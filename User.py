import datetime
import uuid


class User:
    __accounts = []

    def __init__(self, name, email, address, account_type):
        self.__name = name
        self.__email = email
        self.__address = address
        self.__account_type = account_type

        ##########
        self.__balance = 0
        self.__account_number = uuid.uuid4()
        self.__transactions = []
        self.__loan_taken = 0

        ############
        self.__accounts.append(self.__account_number)

    def __make_transaction(self, type: str, amount: str):
        # tr_type = {
        #     "type": type,
        #     "amount": amount,
        #     "before": self.__balance,
        #     "after": self.__balance + amount
        #     if type == "deposit"
        #     else self.__balance - amount,
        #     "at": datetime.datetime.now(),
        # }
        return f"{type} {amount}TK at {datetime.datetime.now()}"
        return tr_type

    def deposit(self, amount: float | int) -> None:
        if amount > 0:
            self.__balance += amount

            self.__transactions.append(self.__make_transaction("deposit", amount))

    def withdraw(self, amount: float | int) -> None:
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(self.__make_transaction("withdraw", amount))
        else:
            raise Exception("Withdrawal amount exceeded")

    def request_for_loan(self, amount: float | int) -> None:
        if self.__loan_taken >= 2:
            if amount > 0 and amount <= self.__balance:
                self.__balance += amount
                self.__loan_taken += 1
                self.__transactions.append(self.__make_transaction("loan", amount))
            else:
                raise Exception("Loan amount exceeded")
        else:
            raise Exception("you already taked loan 2 times")

    def balance_transfer(self, amount: float | int) -> None:
        if amount > 0 and amount <= self.__balance:
            self.__balance += amount
            self.__transactions.append(self.__make_transaction("loan", amount))
        else:
            raise Exception("Loan amount exceeded")

    @property
    def balance(self) -> int:
        return self.__balance

    @property
    def transactions(self) -> int:
        return self.__transactions

    @property
    def accounts(self):
        return self.__accounts


u = User("aaa", "aaa", "aaa", "aaa")

u.deposit(1000)
u.deposit(1000)
u.withdraw(300)
u.request_for_loan(300)
u.request_for_loan(300)
u.request_for_loan(300)
u.request_for_loan(300)
print(u.balance)
print(u.transactions)

print(u.accounts)

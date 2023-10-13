import datetime


class User:
    __accounts = {}

    def __init__(self, name, email, address, account_type):
        self.__name = name
        self.__email = email
        self.__address = address
        self.__account_type = account_type

        ##########
        self.__balance = 0
        self.__account_number = name  # uuid.uuid4()
        self.__transactions = []
        self.__loan_taken = 0

        ############
        self.__accounts[name] = self

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
        print(self.__loan_taken)
        if self.__loan_taken <= 2:
            if amount > 0 and amount <= self.__balance:
                self.__balance += amount
                self.__loan_taken += 1
                self.__transactions.append(self.__make_transaction("loan", amount))
            else:
                raise Exception("Loan amount exceeded")
        else:
            raise Exception("you already taked loan 2 times")

    def balance_transfer(self, amount: float | int, acc_number: str) -> None:
        if acc_number in self.__accounts:
            acc = self.__accounts[acc_number]
            acc.__balance += amount
            self.__balance -= amount
            print(acc)

        else:
            raise Exception("Account not found")

    @property
    def balance(self) -> int:
        return self.__balance

    @property
    def transactions(self) -> int:
        return self.__transactions

    @property
    def accounts(self):
        return self.__accounts


aaa = User("aaa", "aaa", "aaa", "aaa")

aaa.deposit(1000)
aaa.deposit(1000)
aaa.withdraw(300)
aaa.request_for_loan(300)
# aaa.request_for_loan(300)
aaa.request_for_loan(300)
# aaa.balance_transfer(300, "aaa")
print(aaa.balance)
# print(aaa.transactions)

bbb = User("bbb", "bbb", "bbb", "bbb")

bbb.deposit(1000)
bbb.deposit(1000)
bbb.withdraw(300)
bbb.request_for_loan(300)
# bbb.request_for_loan(300)
bbb.request_for_loan(300)
bbb.balance_transfer(300, "aaa")
print(bbb.balance)
print(aaa.balance)
# print(bbb.transactions)

print(bbb.accounts)

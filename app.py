from Admin import Admin
from Bank import Bank


def account_list(users):
    if len(users) > 0:
        for acc_num in users:
            print(f"account {acc_num}")
    else:
        print("account not found")


def create_account(bank: Bank):
    name: str = input("Enter a name : ")
    email: str = input("Enter a email : ")
    address: str = input("Enter a address : ")
    account_type: str = input("Enter a account type : ")
    return bank.create_account(name, email, address, account_type)


def deposit(users):
    acc_num: str = input("Enter user account number : ")
    amount: str = int(input("Enter amount : "))
    if acc_num in users:
        users[acc_num].deposit(amount)
    else:
        print("account not found")


def withdraw(users, bank: Bank):
    acc_num: str = input("Enter user account number : ")
    amount: str = int(input("Enter amount : "))
    if bank.available_balance > amount:
        if acc_num in users:
            users[acc_num].withdraw(amount)
        else:
            print("account not found")
    else:
        print("the bank is bankrupt")


def request_for_loan(users):
    acc_num: str = input("Enter user account number : ")
    amount: str = int(input("Enter amount : "))
    if acc_num in users:
        users[acc_num].request_for_loan(amount)
    else:
        print("account not found")


def balance_transfer(users):
    acc_num: str = input("Enter user account number : ")
    rec_num: str = input("Enter recipient account number : ")
    amount: str = int(input("Enter amount : "))
    if acc_num in users and rec_num in users:
        users[acc_num].balance_transfer(amount, users[rec_num])
    else:
        print("account not found")


def delete_account(users, admin: Admin):
    acc_num: str = input("Enter user account number : ")

    if acc_num in users:
        admin.delete_account(acc_num)
        del users[acc_num]
    else:
        print("account not found")


def check_balance(users):
    acc_num: str = input("Enter user account number : ")

    if acc_num in users:
        print(users[acc_num].balance)
    else:
        print("account not found")


def check_transactions(users):
    acc_num: str = input("Enter user account number : ")

    if acc_num in users:
        print(users[acc_num].transactions)
    else:
        print("account not found")


def check_total_balance(admin: Admin):
    total_balance = admin.check_total_balance()
    print(f"Total Balance in the Bank: {total_balance}TK")


def check_total_loan_amount(admin: Admin):
    total_loan_amount = admin.check_total_loan_amount()
    print(f"Total Loan Amount in the Bank: {total_loan_amount}TK")


if __name__ == "__main__":
    bank = Bank(10000, True)
    admin = Admin(bank)
    users = {}
    # #######################
    user, account_number = bank.create_account(
        "name", "email", "address", "account_type"
    )
    users[account_number] = user
    users[account_number].deposit(1000)
    # #######################

    while True:
        txt = """
        ------------------------------
        1: account_list [admin]
        2: create_account [admin]
        3: delete_account [admin]
        4: check_total_balance [admin]
        5: check_total_loan_amount [admin]
        6: deposit [user]
        7: withdraw [user]
        8: check_balance [user]
        9: check_transactions [user]
        10: request_for_loan [user]
        11: balance_transfer [user]
        30: EXIT
        ------------------------------
        """

        op = int(input(txt + ": "))

        if op == 1:
            account_list(users)
        elif op == 2:
            user, account_number = create_account(bank)
            users[account_number] = user
        elif op == 3:
            delete_account(users, admin)
        elif op == 4:
            check_total_balance(admin)
        elif op == 5:
            check_total_loan_amount(admin)
        elif op == 6:
            deposit(users)
        elif op == 7:
            withdraw(users, bank)
        elif op == 8:
            check_balance(users)
        elif op == 9:
            check_transactions(users)
        elif op == 10:
            request_for_loan(users)
        elif op == 11:
            balance_transfer(users)
        elif op == 30:
            print("...EXIT...")
            break
        else:
            print("___invalid option___")

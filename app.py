from Admin import Admin
from Bank import Bank


def create_account(bank: Bank):
    name: str = input("Enter a name : ")
    email: str = input("Enter a email : ")
    address: str = input("Enter a address : ")
    account_type: str = input("Enter a account type : ")
    return bank.create_account(name, email, address, account_type)


def deposit(users):
    acc_num: str = input("Enter user account number : ")
    amount: str = input("Enter amount : ")
    if acc_num in users:
        users[acc_num].deposit(amount)
    else:
        print("account not found")


def request_for_loan(users):
    acc_num: str = input("Enter user account number : ")
    amount: str = input("Enter amount : ")
    if acc_num in users:
        users[acc_num].request_for_loan(amount)
    else:
        print("account not found")


def balance_transfer(users):
    acc_num: str = input("Enter user account number : ")
    rec_num: str = input("Enter recipient account number : ")
    amount: str = input("Enter amount : ")
    if acc_num in users and rec_num in users:
        users[acc_num].balance_transfer(amount, users[rec_num])
    else:
        print("account not found")


def delete_account(users, admin: Admin):
    acc_num: str = input("Enter user account number : ")

    if acc_num in users:
        admin.delete_account(acc_num)
    else:
        print("account not found")


def check_balance(users):
    acc_num: str = input("Enter user account number : ")

    if acc_num in users:
        print(users[acc_num].balance)
    else:
        print("account not found")


def check_total_balance(admin: Admin):
    total_balance = admin.check_total_balance()
    print(f"Total Balance in the Bank: ${total_balance}")


def check_total_loan_amount(admin: Admin):
    total_loan_amount = admin.check_total_loan_amount()
    print(f"Total Loan Amount in the Bank: ${total_loan_amount}")


if __name__ == "__main__":
    bank = Bank(10000, True)
    admin = Admin(bank)
    users = {}

    while True:
        txt = """------------------------------\n
        1: create_account(bank)    
        2: deposit(users)
        3: request_for_loan(users)
        4: balance_transfer(users)
        5: delete_account(users, admin)
        6: check_total_balance(admin)
        7:check_total_loan_amount
        8: EXIT
            
        ------------------------------\n:
        """

        op = int(input(txt))

        if op == 1:
            user, account_number = create_account(bank)
            users[account_number] = user
        elif op == 2:
            deposit(users)
        elif op == 3:
            request_for_loan(users)
        elif op == 4:
            balance_transfer(users)
        elif op == 5:
            delete_account(users, admin)
        elif op == 6:
            check_total_balance(admin)
        elif op == 7:
            check_total_loan_amount(admin)
        elif op == 8:
            print("...EXIT...")
            break
        else:
            print("___invalid option___")

from os import system, name
import sys
import time

accounts = []
options = ["to add new account", "to deposit money to an existing account", "to withdraw money from an existing account", "to move money from an account to another", "to check balance of account", "to delete account", "to quit the program"]

class Account:
    def __init__(self, name, id, balance = 0):
        self._id = id
        self._name = name
        self._balance = balance

    def __str__(self):
        return self._name

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

    @property
    def balance(self):
        return self._balance

def main():
    print("","Hello and welcome to Roem Central Bank, please follow the instructions below as in how to navigate the program", sep="\n")
    while True:
        get_command()

def get_command():
    print("","The commands that we offer are the following", sep="\n")
    for option_index in range(len(options)):
        print(str(option_index), options[option_index])
    print("Keep in mind that if you ever want to cancel an command simply press the enter button when prompted for input to cancel the command")
    try:
        index = int(input("Please choose an command: "))
        if index == 0:
            call_add()
        elif index == 1:
            call_deposit()
        elif index == 2:
            call_withdraw()
        elif index == 3:
            call_move()
        elif index == 4:
            check_balance()
        elif index == 5:
            call_delete()
        elif index == 6:
            quit()
    except ValueError:
        print(index)
        print("Invalid input, please try again")
        get_command()

def call_add():
    wait_and_clear()
    id = len(accounts)
    account_name = input("Please input name of the new account: ")
    if account_name == "":
        return
    print(add(accounts, account_name, id))
    time.sleep(1)
    wait_and_clear()

def add(account_list, account_name, id):
    new_account = Account(account_name, id)
    account_list.append(new_account)
    return ("Succesfully added new account named " + account_name)

def call_deposit():
    print(deposit(accounts))
    time.sleep(1)
    wait_and_clear()

def deposit(account_list = None, target_id = -1, set_amount = None):
    if len(account_list) == 0:
        return ("No valid account found")
    if target_id == -1:
        account = get_inputted_account(account_list, "Please input number of the account you want to deposit to: ")
        if not account:
            return ("Cancelled")
    else:
        if target_id >= len(account_list) or target_id < 0:
            return ("Target ID is not in account list")
        account = account_list[target_id]
    if not set_amount:
        amount = get_inputted_value("Please input the amount you want to deposit: ")
        if not amount:
            return("Cancelled")
    else:
        amount = set_amount
    account.deposit(amount)
    return ("Deposited " + str(amount) + " to " + str(account))

def call_withdraw():
    print(withdraw(accounts))
    time.sleep(1)
    wait_and_clear()

def withdraw(account_list = None, target_id = -1, set_amount = None):
    if len(account_list) == 0:
        return ("No valid account found")
    if target_id == -1:
        account = get_inputted_account(account_list, "Please input number of the account you want to withdraw from: ")
        if not account:
            return ("Cancelled")
    else:
        if target_id >= len(account_list) or target_id < 0:
            return ("Target ID is not in account list")
        account = account_list[target_id]
    if not set_amount:
        amount = -1
        while amount < 0 or amount >= account.balance:
            amount = get_inputted_value("Please input the amount you want to withdraw: ", "Balance: " + str(account.balance))
            if not amount:
                return("Cancelled")
    else:
        if set_amount < 0 or set_amount > account.balance:
            return("Amount to withdraw exceeds account balance")
        else:
            amount = set_amount
    account.withdraw(amount)
    return ("Succesfully withdrew " + str(amount) + " from " + str(account))

def call_move():
    print(move(accounts))
    time.sleep(1)
    wait_and_clear()

def move(account_list = None, from_id = -1, to_id = -1, set_amount = None):
    if len(account_list) == 0:
        return ("No valid account found")

    if from_id == -1:
        from_account = get_inputted_account(account_list, "Please input number of the account you want to move from: ")
        if not from_account:
            return ("Cancelled")
    else:
        if from_id >= len(account_list) or from_id < 0:
            return ("Target ID is not in account list")
        from_account = account_list[from_id]
    if not set_amount:
        amount = -1
        while amount < 0 or amount >= from_account.balance:
            amount = get_inputted_value("Please input the amount you want to withdraw: ", "Balance: " + str(from_account.balance))
            if not amount:
                return("Cancelled")
    else:
        if set_amount < 0 or set_amount > from_account.balance:
            return("Amount to withdraw exceeds account balance")
        else:
            amount = set_amount

    if to_id == -1:
        to_account = get_inputted_account(account_list, "Please input number of the account you want to move to: ")
        if not to_account:
            return ("Cancelled")
    else:
        if to_id >= len(account_list) or to_id < 0:
            return ("Target ID is not in account list")
        to_account = account_list[to_id]
    from_account.withdraw(amount)
    to_account.deposit(amount)
    return ("Succesfully moved " + str(amount) + " from " + str(from_account) + " to " + str(to_account))

def call_delete():
    if len(accounts) == 0:
        print("No valid account found")
        time.sleep(1)
        wait_and_clear()
        return
    for i in range(len(accounts)):
        print(i, "for account named:", accounts[i])

    while True:
        try:
            index = (input("Please input the number of the account that you want to delete: "))
            if index == "":
                return
            index = int(index)
            if index >= 0 and index < len(accounts):
                break
        except ValueError:
            print("Invalid input, please try again")
    print(delete(accounts, index))
    time.sleep(2)
    wait_and_clear()

def delete(account_list, index):
    print(index, len(account_list))
    if index >= 0 and index < len(account_list):
        target = account_list[index]
        account_list.remove(target)
        return ("Account named " + str(target) + " was removed from Roem Central Bank")
    else:
        return("No valid account found")

def check_balance(account_list = None, target_id = None):
    if len(account_list) == 0:
        print("No valid account found")
        time.sleep(1)
        wait_and_clear()
        return
    account = get_inputted_account(account_list)
    return("Balance:", account.balance)

#HELPERS

def wait_and_clear():
    for _ in range(3):
        time.sleep(0.15)
        sys.stdout.write('.')
        sys.stdout.flush()
    time.sleep(0.15)
    if name == 'nt':
        x = system('cls')
    else:
        x = system('clear')

def get_inputted_account(account_list, text):
    for i in range(len(account_list)):
        print("Input", i, "for account named:", account_list[i])
    while True:
        index = (input(text))
        if index == "":
            return
        index = int(index)
        try:
            if index >= 0 and index < len(account_list):
                break
        except ValueError:
            print("Invalid input, please try again")
    return account_list[index]

def get_inputted_value(input_text, printed_text = None):
    if printed_text:
        print(printed_text)
    value = input(input_text)
    if value == "":
        return
    value = int(value)
    return value

#----------------------------------------------------
def quit():
    sys.exit("Thank you for using Roem Central Bank")

if __name__ == "__main__":
    main()

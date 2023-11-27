from project import add, deposit, withdraw, move, delete
import pytest

testaccounts = []
emptyaccountlist = []
#This is a simulation of the program, thereby theres a list of testaccounts used in the pytest
def main():
    test_class_name()

def test_add():
    assert add(testaccounts, "Simon", 0) == "Succesfully added new account named Simon"
    assert add(testaccounts, "Anna", 1) == "Succesfully added new account named Anna"

def test_class_name():
    assert testaccounts[0]._name == "Simon"
    assert testaccounts[1]._name == "Anna"

def test_deposit():
    assert deposit(emptyaccountlist, 1, 50) == "No valid account found"
    assert deposit(testaccounts, 2, 50) == "Target ID is not in account list"
    assert deposit(testaccounts, 1, 50) == "Deposited 50 to Anna"
    assert deposit(testaccounts, 0, 50) == "Deposited 50 to Simon"

def test_withdraw():
    assert withdraw(emptyaccountlist, 0, 0) == "No valid account found"
    assert withdraw(testaccounts, 1, 1000) == "Amount to withdraw exceeds account balance"
    assert withdraw(testaccounts, 0, 10) == "Succesfully withdrew 10 from Simon"
    assert withdraw(testaccounts, 100, 10) == "Target ID is not in account list"

def test_move():
    assert move(emptyaccountlist, 0, 0, 0) == "No valid account found"
    assert move(testaccounts, 0, 1, 10) == "Succesfully moved 10 from Simon to Anna"

def test_delete():
    assert testaccounts[1]._name == "Anna"
    assert delete(testaccounts, 1) == "Account named Anna was removed from Roem Central Bank"
    assert delete(testaccounts, 1) == "No valid account found"

if __name__ == "__main__":
    main()

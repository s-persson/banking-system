# Banking System
## [Video Demo](https://youtu.be/PiSLwHjbQMQ)
### Description:
This program is a simulative banking program which lets the user create accounts and manage the accounts' money.

### How to use the program
When first entering the program the user is welcomed and displayed the different commands offered to navigate the program.
The user inputs where they want to navigate, the options are as following:
#### Add
When calling the add function the user is prompted to input the name of the account that they intend to create
The function then creates a new instance of the Account class which takes in the inputted name as name of the instance and the id is set to the current length of the list of all accounts created
The added account event is added to the accounts' "changehistory" which is a list of strings that gives the user the ability so see all the changes that has been made to that account.
#### Deposit
When calling the deposit function all the avaliable accounts to deposit too are printed, if none are avaliable then the function will return with the text "No valid account found", this is repeated throughout all the programs functions. The user is prompted to input the index of the account they want to deposit money to, if the input is valid then the programs prompts the user to input the amount of money to deposit. If all these steps are completed then the program will update the balance of the given account in the account list.
The accounts' "changehistory" is updated with the deposit information.
#### Withdraw
When calling the withdraw function all the avaliable accounts to withdraw from are printed,
if the input is valid then the program will prompt for the amount to withdraw, if the amount inputted is not valid then it will reprompt. If the steps are completed then the program will update the balance of the given account in the account list.
The accounts' "changehistory" is updated with the withdraw information.
#### Move
When calling the move function the user is prompted to enter the account to move money from, if the input is valid then the user is prompted to enter the amount of money to move, if the input is valid then the user is prompted to enter the account to move the money to.
Both of the accounts' "changehistory" is updated with the move information.
#### Check Changehistory
When calling the check changehistory function the user is prompted to input the account that the user wants to get the changehistory data for. If the input is valid then the program will output all the transactions and updates that it has recorded.
#### Delete
When calling the delete function the user is prompted to enter the account that the user wants to delete. If the input is valid and the user confirms then the program will delete the account from the account list.
#### Quit
When calling the quit function the programs exits with a message.

## Installation & Usage
After you've downloaded the project files and navigated to it's folder directory use 'cmd' with the following commands to use the program
#### Install Requirements
To install the required libraries use [pip](https://pip.pypa.io/en/stable/)
```
$ pip install -r requirements.txt
```
#### Usage
Run the program by
```
$ python project.py through the 'cmd'
```
Test the program by
```
$ pytest test_project.py through the 'cmd'
```
>[!NOTE]
When prompted the user can always press 'Enter' without any text to cancel the current command

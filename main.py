import json
from const import *
from login_utils import *
from expense_utils import *

try:
    with open(LOGIN_JSON_PATH, 'r') as file:
        login_data = json.load(file)
        USERS = [list(user.keys())[0] for user in login_data]
except FileNotFoundError:
    log("login.json not found! Defaulting to no users, and creating a new file.", "warn")
    with open(LOGIN_JSON_PATH, 'w') as file:
        file.write()
        USERS = []
    
except json.JSONDecodeError:
    log("login.json had an error", "warn")

def menu(username):
    print("1. Add Expense\n2. View Expense Statistics\n3. Delete Expense\n4. Logout")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_expense(username)
        menu(username)
    elif choice == '2':
        view_expense_stats(username)
        menu(username)
    elif choice == '3':
        delete_expense(username)
        menu(username)
    elif choice == '4':
        start()
    else:
        print("Invalid choice! Please try again.")
        menu()

def start():
    print("\n1. Login\n2. Register\n3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        next_step, username = login()
        if next_step == True:
            print("Login successful!")
            menu(username)
        else:
            start()
    elif choice == '2':
        register()
        start()
    elif choice == '3':
        exit()
    else:
        print("Invalid choice! Please try again.")
        start()

if __name__ == '__main__':
    start()
import json
import time
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
    if username == 'admin':
        print("1. Add Expense\n2. View Expense Statistics\n3. Delete Expense\n4. Logout\n5. View All Users")
    else:
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
        print("Logging out...")
        time.sleep(1)
        start()
    elif choice == '5' and username == 'admin':
        admin_view_users()
        menu(username)
    else:
        print("Invalid choice! Please try again.")
        menu()

def start():
    print("\n1. Login\n2. Register\n3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        next_step, username = login()
        if next_step == True and username == 'admin':
            print("Admin login successful!")
            menu(username)
        elif next_step == True:
            print(f"Login successful! Welcome, {username}!")
            time.sleep(1)
            menu(username)
        else:
            start()
    elif choice == '2':
        register()
        start()
    elif choice == '3':
        print("Thank you for using the ExpenseTracker™. Have a pleasent rest of your day.")
        exit()
    else:
        print("Invalid choice! Please try again.")
        start()

if __name__ == '__main__':
    print("Welcome to the ExpenseTracker™!")
    start()
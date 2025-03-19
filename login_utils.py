from const import *
import json

def new_user(username, password, security_question, security_answer):
    # Load existing users or create empty list
    try:
        with open(LOGIN_JSON_PATH, 'r') as f:
            users = json.load(f)
            if isinstance(users, dict):
                users = [users]
    except (FileNotFoundError, json.JSONDecodeError):
        users = []
        log("While reading login.json, an error occured. Defaulting to no users.", "warn")
    
    if any(user['username'] == username for user in users):
        print('Username already exists! Please try a different username.')
        return
    
    # Add new user to list
    new_username = {
        'username': username,
        'password': password,
        'security_question': security_question,
        'security_answer': security_answer
    }
    users.append(new_username)
    
    # Write back to file with nice formatting
    with open(LOGIN_JSON_PATH, 'w') as f:
        json.dump(users, f, indent=4)
    log(f"User {username} created", "info")
    
    # Add their expenses file
    with open(f'{USERS_FOLDER}/{username}_expenses.json', 'w') as f:
        f.write('[]')
    log(f"User {username} expenses file created", "info")
    
    
def register():
    print("Register your account. Type 'back' to go back to login.")
    username = input("Enter username: ")
    password = input("Enter password: ")
    security_question = input("Enter security question: ")
    security_answer = input("Enter security answer: ")
    new_user(username, password, security_question, security_answer)
    
    
def login():
    print("Login to your account. Type 'back' to go back to main menu.")
    username = input("Enter username: ")
    if username == 'back':
                return False
    password = input("Enter password: ")
    if username == 'back':
                return False, username
    # Search in login.json for user, and see if password matches.
    with open(LOGIN_JSON_PATH, 'r') as f:
        users = json.load(f)
        if isinstance(users, dict):
            users = [users]
    for user in users:
        if user['username'] == username and user['password'] == password:
            return True, username
        else:
            print("Username or password incorrect! Please try again.")
            user_choice = input("Enter 'back' to go back to main menu, 'forgot' to reset your password, or 'retry' to try again: ")
            if user_choice == 'back':
                return False, username
            elif user_choice == 'forgot':
                reset_password(username)
                login()
            elif user_choice == 'retry':
                login()
            else:
                print("Invalid input! Please try again.")
                login()

def reset_password(username):
    # Ask the user to answer the security question, and see if they get it right. If they do, ask for a new password. If they don't, keep asking until they get it right.
    with open(LOGIN_JSON_PATH, 'r') as f:
        users = json.load(f)
        if isinstance(users, dict):
            users = [users]
    for user in users:
        if user['username'] == username:
            security_answer = input(f"Please correctly answer your security question. All answers are case-sensitive.\n {user['security_question']}\nAnswer: ")
            while True:    
                if security_answer == user['security_answer']:
                    new_password = input("Enter your new password: ")
                    user['password'] = new_password
                    with open(LOGIN_JSON_PATH, 'w') as f:
                        json.dump(users, f, indent=4)
                    log(f"User {username} reset their password", "info")
                    print("Password reset successful!")
                    break
                else:
                    print("Incorrect answer! Please try again.")
                    continue
import json
from datetime import datetime

# Json to store account credentials
LOGIN_JSON_PATH = 'Users/login.json'

# Folder to store users data
USERS_FOLDER = 'Users/ExpenseDatabase'

USERS = []

def log(message, type):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('app.log', 'a') as log_file:
        log_file.write(f"[{timestamp}] [{type.upper()}] {message}\n")
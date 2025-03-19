from const import *

def add_expense(username):
    # Get the Category, Amount, and description of the expense, and store it in the user's file.
    category = input("Enter category of expense: ")
    amount = input("Enter amount of expense: ")
    description = input("Enter description of expense: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(f'{USERS_FOLDER}/{username}_expenses.json', 'r') as f:
        user_data = json.load(f)
    user_data.append({
        'category': category,
        'amount': amount,
        'description': description,
        'timestamp': timestamp
    })
    with open(f'{USERS_FOLDER}/{username}_expenses.json', 'w') as f:
        json.dump(user_data, f, indent=4)
        
def view_expense_stats(username):
    # Get the user's expenses, and calculate the total, average, and category wise expenses.
    with open(f'{USERS_FOLDER}/{username}_expenses.json', 'r') as f:
        user_data = json.load(f)
    
    total = sum([int(expense['amount']) for expense in user_data])
    average = total / len(user_data) if user_data else 0

    # Sort expenses by category and date
    category_wise = {}
    for expense in user_data:
        cat = expense['category']
        if cat not in category_wise:
            category_wise[cat] = {'total': 0, 'dates': []}
        category_wise[cat]['total'] += int(expense['amount'])
        category_wise[cat]['dates'].append(expense['timestamp'][:10])  # Get just the date part

    # Print summary
    print("\n=== Expense Summary ===")
    print(f"Total expenses: ${total:,.2f}")
    print(f"Average expense: ${average:,.2f}\n")

    # Print category table
    print("Category Breakdown:")
    print("-" * 50)
    print(f"{'Category':<20} {'Amount':>10} {'Latest Date':>18}")
    print("-" * 50)
    
    for category, data in sorted(category_wise.items()):
        latest_date = max(data['dates'])
        print(f"{category:<20} ${data['total']:>9,.2f} {latest_date:>18}")
    
    print("-" * 50)

def delete_expense(username):
    # Get the user's expenses, and show them the expenses. Ask them to enter the index of the expense they want to delete, and remove that expense from the user's file.
    with open(f'{USERS_FOLDER}/{username}_expenses.json', 'r') as f:
        user_data = json.load(f)
    for i, expense in enumerate(user_data):
        print(f"{i+1}. {expense['category']} - {expense['amount']} - {expense['description']} - {expense['timestamp']}")
    index = int(input("Enter the index of the expense you want to delete: ")) - 1
    user_data.pop(index)
    with open(f'{USERS_FOLDER}/{username}_expenses.json', 'w') as f:
        json.dump(user_data, f, indent=4)
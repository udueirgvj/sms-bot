users = {}
balances = {}

numbers_sold = 0
total_profit = 0


def add_user(user_id):

    if user_id not in users:
        users[user_id] = True
        balances[user_id] = 0


def add_balance(user_id, amount):

    balances[user_id] += amount


def remove_balance(user_id, amount):

    balances[user_id] -= amount

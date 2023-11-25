import uuid
from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime, timedelta

class User:
    def __init__(self, user_id, name, email, mobile):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.mobile = mobile
        self.expenses = []
        self.balances = {}

class Expense:
    def __init__(self, expense_id, payer, amount, expense_type, participants, shares=None):
        self.expense_id = expense_id
        self.payer = payer
        self.amount = amount
        self.expense_type = expense_type
        self.participants = participants
        self.shares = shares if shares else [1] * len(participants)

def round_decimal(value):
    return Decimal(value).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)


class ExpenseManager:
    def __init__(self):
        self.users = {}
        self.expenses = []

    def add_user(self, name, email, mobile):
        user_id = str(uuid.uuid4())
        user = User(user_id, name, email, mobile)
        self.users[user_id] = user
        return user

    def add_expense(self, payer, amount, expense_type, participants, shares=None):
        expense_id = str(uuid.uuid4())
        expense = Expense(expense_id, payer, amount, expense_type, participants, shares)
        self.expenses.append(expense)

        if shares is None:
            shares = [1] * len(participants)

        for participant, share in zip(participants, shares):
            share_amount = round_decimal(amount * share / sum(shares))
            if participant != payer:
                if participant.user_id not in self.users[payer.user_id].balances:
                    self.users[payer.user_id].balances[participant.user_id] = 0
                self.users[payer.user_id].balances[participant.user_id] += share_amount

                if payer.user_id not in self.users[participant.user_id].balances:
                    self.users[participant.user_id].balances[payer.user_id] = 0
                self.users[participant.user_id].balances[payer.user_id] -= share_amount

        return expense

    
    def simplify_balances(self, user_id):
        for creditor, amount in list(self.users[user_id].balances.items()):
            for debtor, debtor_amount in list(self.users[creditor].balances.items()):
                if debtor_amount < 0:
                    transfer_amount = min(amount, abs(debtor_amount))

                    # Update creditor's balance
                    self.users[creditor].balances[creditor] = max(0, self.users[creditor].balances.get(creditor, 0) - transfer_amount)
                    
                    # Update debtor's balance
                    self.users[debtor].balances[creditor] = max(0, self.users[debtor].balances.get(creditor, 0) + transfer_amount)

                    if self.users[creditor].balances[creditor] == 0:
                        del self.users[creditor].balances[creditor]

                    if self.users[debtor].balances[creditor] == 0:
                        del self.users[debtor].balances[creditor]

    def show_user_balances(self, user_id):
        self.simplify_balances(user_id)
        return {creditor: round_decimal(amount) for creditor, amount in self.users[user_id].balances.items()}

    

# Example usage:
expense_manager = ExpenseManager()
user1 = expense_manager.add_user("User1", "user1@example.com", "1234567890")
user2 = expense_manager.add_user("User2", "user2@example.com", "9876543210")
user3 = expense_manager.add_user("User3", "user3@example.com", "4567890123")
user4 = expense_manager.add_user("User4", "user4@example.com", "7890123456")

# Example 1
expense_manager.add_expense(user1, 1000, "EQUAL", [user1, user2, user3, user4])

# Example 2
expense_manager.add_expense(user1, 1250, "EXACT", [user1, user2, user3], [0, 370, 880])

# Example 3
expense_manager.add_expense(user4, 1200, "PERCENT", [user1, user2, user3, user4], [40, 20, 20, 20])

# Show balances
print(expense_manager.show_user_balances(user1.user_id))
print(expense_manager.show_user_balances(user2.user_id))
print(expense_manager.show_user_balances(user3.user_id))
print(expense_manager.show_user_balances(user4.user_id))

Expense Sharing Application
Overview
The Expense Sharing Application is a backend system designed to facilitate the sharing of expenses among users. The system allows users to add expenses, split them among different participants, and keeps track of balances between users. The goal is to efficiently manage shared expenses, ensure accurate balances, and provide optional features such as simplifying expenses and sending reminders.

Architecture
Expense Sharing App Architecture

Components:

User Management: Manages user information.
Expense Management: Handles the creation and management of expenses.
Balances and Notifications: Manages balances and sends notifications.
API Endpoints: Handles HTTP requests and responses.
Database: Stores user information, expenses, and balances.
Communication:

Users interact with the system through API endpoints.
The system communicates with the database to store and retrieve information.
The Balances and Notifications component sends notifications based on user actions.
Optional Components:

Passbook: Manages and displays user transactions.
Reminder Scheduler: Schedules and sends reminders.
Database Schema
User Table:

userId (Primary Key)
name
email
mobile
Expense Table:

expenseId (Primary Key)
payerId (Foreign Key referencing User)
amount
type (EQUAL, EXACT, PERCENT)
splitDetails (JSON or separate table for split details)
created_at
Balance Table:

balanceId (Primary Key)
userId (Foreign Key referencing User)
debtorId (Foreign Key referencing User)
amount
expenseId (Foreign Key referencing Expense)
settled (Boolean)
Class Structure
python
Copy code
class User:
    def __init__(self, userId, name, email, mobile):
        pass

class Expense:
    def __init__(self, expenseId, payer, amount, expenseType, splitDetails):
        pass

class Balance:
    def __init__(self, userId, debtorId, amount, expenseId, settled):
        pass

class ExpenseManager:
    def add_user(self, name, email, mobile):
        pass

    def create_expense(self, payer, amount, expenseType, participants, splitDetails):
        pass

    def get_user_balances(self, userId):
        pass

    def simplify_expenses(self, userId):
        pass

    def send_expense_notifications(self, expenseId):
        pass
API Contracts
User Management
Create User:

POST /users
Creates a new user.
Example Request:

json
Copy code
{
  "name": "John Doe",
  "email": "john@example.com",
  "mobile": "1234567890"
}
Example Response:

json
Copy code
{
  "userId": "unique_user_id",
  "name": "John Doe",
  "email": "john@example.com",
  "mobile": "1234567890"
}
Get User Information:

GET /users/:userId
Retrieves information about a specific user.
Example Response:

json
Copy code
{
  "userId": "unique_user_id",
  "name": "John Doe",
  "email": "john@example.com",
  "mobile": "1234567890"
}
Update User Information:

PUT /users/:userId
Updates information about a specific user.
Example Request:

json
Copy code
{
  "name": "Updated Name",
  "email": "updated@example.com",
  "mobile": "9876543210"
}
Example Response:

json
Copy code
{
  "userId": "unique_user_id",
  "name": "Updated Name",
  "email": "updated@example.com",
  "mobile": "9876543210"
}
Expense Management
Create Expense:

POST /expenses
Creates a new expense.
Example Request:

json
Copy code
{
  "payerId": "payer_user_id",
  "amount": 1000,
  "expenseType": "EQUAL",
  "participants": ["u1", "u2", "u3", "u4"],
  "splitDetails": null
}
Example Response:

json
Copy code
{
  "expenseId": "unique_expense_id",
  "payerId": "payer_user_id",
  "amount": 1000,
  "expenseType": "EQUAL",
  "participants": ["u1", "u2", "u3", "u4"],
  "splitDetails": null,
  "created_at": "timestamp"
}
Get Expense Details:

GET /expenses/:expenseId
Retrieves details about a specific expense.
Example Response:

json
Copy code
{
  "expenseId": "unique_expense_id",
  "payerId": "payer_user_id",
  "amount": 1000,
  "expenseType": "EQUAL",
  "participants": ["u1", "u2", "u3", "u4"],
  "splitDetails": null,
  "created_at": "timestamp"
}
Get User Expenses:

GET /users/:userId/expenses
Retrieves all expenses for a specific user.
Example Response:

json
Copy code
[
  {
    "expenseId": "unique_expense_id",
    "payerId": "payer_user_id",
    "amount": 1000,
    "expenseType": "EQUAL",
    "participants": ["u1", "u2", "u3", "u4"],
    "splitDetails": null,
    "created_at": "timestamp"
  },
  // ... (more expenses)
]
Balances and Notifications
Get User Balances:

GET /users/:userId/balances
Retrieves balances for a specific user.
Example Response:

json
Copy code
{
  "u2": -250,
  "u3": -250,
  "u4": -250
}
Simplify Expenses:

POST /expenses/:expenseId/simplify
Simplifies balances for a specific expense.
Example Response:

json
Copy code
{
  "u2": -250,
  "u3": -250,
  "u4": -250
}
Optional Components
Passbook:

GET /users/:userId/passbook
Retrieves the user's passbook showing all transactions.
Example Response:

json
Copy code
[
  {
    "type": "Expense",
    "description": "Electricity Bill",
    "amount": 1000,
    "date": "timestamp"
  },
  // ... (more entries)
]
Reminder Scheduler:

Automatically sends reminders at the end of each week.


# Install dependencies using your package manager
Database Setup:

Set up your preferred database (e.g., PostgreSQL, MongoDB).
Update the database connection details in the configuration file.
Environment Variables:

Create an environment file (e.g., .env) and configure necessary variables.
Example .env file:
env
Copy code
DATABASE_URL=your_database_url
PORT=5000
Run the Application:

bash
Copy code
# Run the application
Access API Endpoints:

Open your browser or use a tool like curl or Postman to access the defined API endpoints.
Testing:

Implement and run tests to ensure the system's functionality.
Notes
All API responses should take less than 50 milliseconds.
Optional features can be enabled or disabled based on user preferences.
Security measures (e.g., authentication, authorization) should be implemented based on your application's needs.

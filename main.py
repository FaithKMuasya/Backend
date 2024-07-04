from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from models import db, Income, Savings, Expenses, Categories, User
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
migrate=Migrate(app, db)
db.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/incomes', methods=['GET'])
def get_all_income():
    incomes = Income.query.all()
    income_list = [income.to_dict() for income in incomes]
    return jsonify(income_list)

@app.route('/incomes/<int:income_id>', methods=['GET'])
def get_income(income_id):
    income = Income.query.get(income_id)
    if income:
        return jsonify(income.to_dict()), 200
    else:
        return jsonify({"error": "Income not found"}), 404
    
@app.route('/savings/', methods=['GET'])
def get_all_savings():
    savings = Savings.query.all()
    savings_list = [saving.to_dict() for saving in savings]
    return jsonify(savings_list)

@app.route('/savings/<int:saving_id>', methods=['GET'])
def get_saving(saving_id):
    saving = Savings.query.get(saving_id)
    if saving:
        return jsonify(saving.to_dict()), 200
    else:
        return jsonify({"error": "Saving not found"}), 404
    
@app.route('/expenses', methods=['GET'])
def get_all_expenses():
    expenses= Expenses.query.all()
    expenses_list = [expense.to_dict() for expense in expenses]
    return jsonify(expenses_list)

@app.route('/expenses/<int:expense_id>', methods=['GET'])
def get_expense(expense_id):
    expense=Expenses.query.get(expense_id)
    if expense:
        return jsonify(expense.to_dict()), 200
    else:
        return jsonify({"error": "Expense not found"}), 404
    

@app.route('/categories', methods=['GET'])
def get_all_categories():
    categories = Categories.query.all()
    categories_list = [category.to_dict() for category in categories]
    return jsonify(categories_list)

@app.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    category = Categories.query.get(category_id)
    if category:
        return jsonify(category.to_dict()), 200
    else:
        return jsonify({"error": "Category not found"}), 404
    

@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    users_list = [user.to_dict() for user in users]
    return jsonify(users_list)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    else:
        return jsonify({"error": "User not found"}), 404
    

if __name__ == '__main__':
    app.run(port=5555)
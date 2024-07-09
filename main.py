from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate
from models import db, Income, Savings, Expenses, Categories, User
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
migrate=Migrate(app, db)
db.init_app(app)

@app.route('/')
def hello_world():
    return 'Hey Loshy!'

#INCOME ROUTES

#Route for Querying all the incomes from the database
@app.route('/incomes', methods=['GET'])
def get_all_income():
    incomes = Income.query.all()
    income_list = [income.to_dict() for income in incomes]
    return jsonify(income_list)


#Route for Querying a specific income by id from the database
@app.route('/incomes/<int:income_id>', methods=['GET'])
def get_income(income_id):
    income = Income.query.get(income_id)
    if income:
        return jsonify(income.to_dict()), 200
    else:
        return jsonify({"error": "Income not found"}), 404
    
#Route for creating/adding a new income in the database
@app.route('/incomes', methods=['POST'])
def create_income():
    data = request.json
    description = data.get('description')
    amount = data.get('amount')
    date_str = data.get('date')
    user_id = data.get('user_id')
    date = datetime.strptime(date_str, '%Y-%m-%d').date()
    new_income = Income(description=description, amount=amount, date=date, user_id=user_id)
    db.session.add(new_income)
    db.session.commit()
    return jsonify(new_income.to_dict()), 201

#Route for changing values in all of your income attributes 
@app.route('/incomes/<int:income_id>', methods=['PUT'])
def update_income(income_id):
    updating_income = Income.query.get(income_id)
    if not updating_income:
        return jsonify({"error": "Income not found"}), 404

    updates = request.json
    updating_income.description = updates['description']
    updating_income.amount = updates['amount']
    

    updating_income.date = datetime.strptime(updates['date'], '%Y-%m-%d').date()
    
    updating_income.user_id = updates['user_id']

    db.session.commit()
    return jsonify(updating_income.to_dict())



#SAVINGS ROUTES

#Route for querying all savings from the database    
@app.route('/savings/', methods=['GET'])
def get_all_savings():
    savings = Savings.query.all()
    savings_list = [saving.to_dict() for saving in savings]
    return jsonify(savings_list)


#Route for querying a specific savings by id from the database
@app.route('/savings/<int:saving_id>', methods=['GET'])
def get_saving(saving_id):
    saving = Savings.query.get(saving_id)
    if saving:
        return jsonify(saving.to_dict()), 200
    else:
        return jsonify({"error": "Saving not found"}), 404
    

#Route for creating/adding a new savings in the database
@app.route('/savings', methods=['POST'])
def create_saving():
    data = request.json
    description = data.get('description')
    amount = data.get('amount')
    date_str = data.get('date')
    user_id = data.get('user_id')
    category_id = data.get('category_id')
    date = datetime.strptime(date_str, '%Y-%m-%d').date()
    new_saving = Savings(description=description, amount=amount, date=date, user_id=user_id, category_id=category_id)
    db.session.add(new_saving)
    db.session.commit()
    return jsonify(new_saving.to_dict()), 201

#Route for changing values in all of your savings attributes
@app.route('/savings/<int:saving_id>', methods=['PUT'])
def update_saving(saving_id):
    updating_saving = Savings.query.get(saving_id)
    if not updating_saving:
        return jsonify({"error": "Saving not found"}), 404

    updates = request.json
    updating_saving.description = updates['description']
    updating_saving.amount = updates['amount']
    updating_saving.date = datetime.strptime(updates['date'], '%Y-%m-%d').date()
    updating_saving.user_id = updates['user_id']
    updating_saving.category_id = updates['category_id']

    db.session.commit()
    return jsonify(updating_saving.to_dict())



#EXPENSE ROUTES
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
    

@app.route('/expenses', methods=['POST'])
def create_expense():
    data = request.json
    description = data.get('description')
    amount = data.get('amount')
    date_str = data.get('date')
    user_id = data.get('user_id')
    category_id = data.get('category_id')
    date = datetime.strptime(date_str, '%Y-%m-%d').date()
    new_expense = Expenses(description=description, amount=amount, date=date, user_id=user_id, category_id=category_id)
    db.session.add(new_expense)
    db.session.commit()
    return jsonify(new_expense.to_dict()), 201

#Route for updating an expense 
@app.route('/expenses/<int:expense_id>', methods=['PUT'])
def update_expense(expense_id):
    updating_expense = Expenses.query.get(expense_id)
    if not updating_expense:
        return jsonify({"error": "Expense not found"}), 404

    updates = request.json
    updating_expense.description = updates['description']
    updating_expense.amount = updates['amount']
    updating_expense.date = datetime.strptime(updates['date'], '%Y-%m-%d').date()
    updating_expense.user_id = updates['user_id']
    updating_expense.category_id = updates['category_id']

    db.session.commit()
    return jsonify(updating_expense.to_dict())
    

#CATEGORY ROUTES
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
    


@app.route('/categories', methods=['POST'])
def create_category():
    data = request.json
    name = data.get('name')
    new_category = Categories(name=name)
    db.session.add(new_category)
    db.session.commit()
    return jsonify(new_category.to_dict()), 201

#Route for updating a category
@app.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    updating_category = Categories.query.get(category_id)
    if not updating_category:
        return jsonify({"error": "Category not found"}), 404

    updates = request.json
    updating_category.name = updates['name']

    db.session.commit()
    return jsonify(updating_category.to_dict())
    

#USER ROUTES
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
    

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

#Route for updating a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    updating_user = User.query.get(user_id)
    if not updating_user:
        return jsonify({"error": "User not found"}), 404

    updates = request.json
    updating_user.username = updates['username']
    updating_user.email = updates['email']
    updating_user.password = updates['password']

    db.session.commit()
    return jsonify(updating_user.to_dict())
    

if __name__ == '__main__':
    app.run(port=5555)
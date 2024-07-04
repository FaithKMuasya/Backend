from faker import Faker
from werkzeug.security import generate_password_hash
from models import db, Income, User, Savings, Expenses, Categories
from main import app

fake = Faker()

def tracker():
    with app.app_context():
        # Create a new user with a hashed password
        user_1 = User(username=fake.user_name(), email=fake.email(), password=generate_password_hash(fake.password()))
        db.session.add(user_1)
        db.session.commit()  # Commit to get the user id

        # Create a new category
        category_1 = Categories(name=fake.word())
        db.session.add(category_1)
        db.session.commit()  # Commit to get the category id

        # Create records for income, savings, and expenses using the new user's id and category's id
        income_1 = Income(description=fake.job(), amount=fake.random_number(digits=5), date=fake.date_this_year(), user_id=user_1.id)
        savings_1 = Savings(description=fake.word(), amount=fake.random_number(digits=5), date=fake.date_this_year(), user_id=user_1.id, category_id=category_1.id)
        expense_1 = Expenses(description=fake.word(), amount=fake.random_number(digits=4), date=fake.date_this_year(), user_id=user_1.id, category_id=category_1.id)

        db.session.add_all([income_1, savings_1, expense_1, category_1])
        db.session.commit()

        print("All data has been added successfully")

if __name__ == "__main__":
    tracker()


from run import app, db  # Import the Flask app and SQLAlchemy instance
from models import Restaurant, Pizza, RestaurantPizza  # Import your SQLAlchemy models

def create_sample_data():
    with app.app_context():
        # Create and add sample restaurants
        restaurant1 = Restaurant(name="Dominion Pizza", address="Good Italian, Ngong Road, 5th Avenue")
        restaurant2 = Restaurant(name="Pizza Hut", address="Westgate Mall, Mwanzi Road, Nrb 100")

        # Create and add sample pizzas
        pizza1 = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
        pizza2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

        # Add sample restaurants and pizzas to the session
        db.session.add(restaurant1)
        db.session.add(restaurant2)
        db.session.add(pizza1)
        db.session.add(pizza2)

        # Commit the changes to the database
        db.session.commit()

if __name__ == '__main__':
    create_sample_data()
    print("Sample data created successfully.")

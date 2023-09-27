# Pizza Restaurant Management System
Restaurant flask api code challenge

This is a Python Flask application for managing a pizza restaurant. The application allows you to create, read, update, and delete restaurants and pizzas. It also allows you to associate pizzas with restaurants and specify their prices. Below, you'll find instructions on how to set up and use this application.

## Table of Contents
- [Setup](#setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)

## Setup

1. **Clone the Repository**: Clone this repository to your local machine.

    ```
    git clone <repository_url>
    ```

2. **Install Dependencies**: Navigate to the project directory and install the required dependencies using pip.

    ```
    cd Flaskuno
    pip install -r requirements.txt
    ```

3. **Database Configuration**: By default, the application is configured to use SQLite as the database. You can modify the database configuration in `run.py` by changing the `SQLALCHEMY_DATABASE_URI` variable to use a different database system if needed.

4. **Initialize the Database**: Initialize the database by running the following command:

    ```
    python3 run.py
    ```

    This will create the SQLite database file `pizza_restaurant.db` and set up the necessary tables.

## Running the Application

To run the application, use the following command in the project directory:

```
python3 run.py
```

The application will start on `http://localhost:5000`.

## API Endpoints

The application provides the following API endpoints for managing restaurants and pizzas:

### Get a List of All Restaurants

- **URL**: `/restaurants`
- **Method**: `GET`
- **Description**: Retrieves a list of all restaurants.

### Get a Restaurant by ID

- **URL**: `/restaurants/<int:restaurant_id>`
- **Method**: `GET`
- **Description**: Retrieves details of a specific restaurant by its ID.

### Delete a Restaurant by ID

- **URL**: `/restaurants/<int:restaurant_id>`
- **Method**: `DELETE`
- **Description**: Deletes a restaurant and its associated pizzas by its ID.

### Get a List of All Pizzas

- **URL**: `/pizzas`
- **Method**: `GET`
- **Description**: Retrieves a list of all available pizzas.

### Create a New Restaurant

- **URL**: `/restaurants`
- **Method**: `POST`
- **Description**: Creates a new restaurant. Provide the restaurant's name and address in the request JSON.

### Create a New Pizza

- **URL**: `/pizzas`
- **Method**: `POST`
- **Description**: Creates a new pizza. Provide the pizza's name and ingredients in the request JSON.

### Create a New RestaurantPizza

- **URL**: `/restaurant_pizzas`
- **Method**: `POST`
- **Description**: Associates a pizza with a restaurant and specifies its price. Provide the `restaurant_id`, `pizza_id`, and `price` in the request JSON.

Make API requests using your preferred tool (e.g., Postman or curl) or integrate these endpoints into your own application.

**Note**: This README provides a basic overview of the application. You can extend it by adding more features, such as authentication and error handling, to suit your specific requirements.
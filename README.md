# Pizza Restaurant API

A RESTful API for managing pizza restaurants, their pizzas, and the relationship between them.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pizza-api-challenge.git
   cd pizza-api-challenge

2.  Set up virtual environment and install
    dependencies:
    '''bash
    pipenv install
    pipenv shell

3. Initialize the database:
    '''bash
    export FLASK_APP=server/app.py
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade head

4. Seed the database
    '''bash
    python server/seed.py


5. Run the application
    ''bash
    flask run

 API Endpoints
Restaurants
GET /restaurants

Returns all restaurants

Example response:

json
[
  {
    "id": 1,
    "name": "Pizza Palace",
    "address": "123 Main St"
  },
  ...
]
GET /restaurants/<int:id>

Returns a single restaurant with its pizzas

Example response:

json
{
  "id": 1,
  "name": "Pizza Palace",
  "address": "123 Main St",
  "pizzas": [
    {
      "id": 1,
      "name": "Margherita",
      "ingredients": "Tomato sauce, mozzarella, basil"
    },
    ...
  ]
}
If restaurant not found:

json
{
  "error": "Restaurant not found"
}
DELETE /restaurants/<int:id>

Deletes a restaurant and its associated restaurant_pizzas

Returns 204 No Content on success

If restaurant not found:

json
{
  "error": "Restaurant not found"
}
Pizzas
GET /pizzas

Returns all pizzas

Example response:

json
[
  {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Tomato sauce, mozzarella, basil"
  },
  ...
]
Restaurant Pizzas
POST /restaurant_pizzas

Creates a new restaurant_pizza

Request body:

json
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
Success response:

json
{
  "id": 4,
  "price": 5,
  "pizza": {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Tomato sauce, mozzarella, basil"
  },
  "restaurant": {
    "id": 3,
    "name": "Luigi's Pizza",
    "address": "789 Pine Rd"
  }
}
Error response (if validation fails):

json
{
  "errors": ["Price must be between 1 and 30"]
}
Validation Rules
Restaurant:

Name must be unique and ≤ 50 characters

Address is required

Pizza:

Name is required

Ingredients is required

RestaurantPizza:

Price must be between 1 and 30 (inclusive)

pizza_id and restaurant_id are required

Testing with Postman
Import the Postman collection from challenge-1-pizzas.postman_collection.json

Start the Flask server

Run each request in the collection to test the API   

  
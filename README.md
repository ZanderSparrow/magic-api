# Magic Gathering API

A RESTful API for gathering a collection of Magic: The Gathering cards.

## Endpoints

### GET /cards/

Returns a list of all magic cards in the collection.

### GET /cards/?name=

Returns the card with the specified name.

### GET /cards/?colors=&colors=

Returns cards whose mana cost contains any of the specified colors.

### POST /cards/

Creates a new magic card.

Request Body:
```json
{
    "name": "Card Name",
    "current_value": 10.99,
    "description": "Card description",
    "image_url": "https://example.com/card-image.jpg",
    "mana_cost": "2UU"
}
```

### PUT /cards/<id>/

Updates the card with the specified ID.

Request Body:
```json
{
    "name": "New Card Name",
    "current_value": 11.99,
    "description": "New card description",
    "image_url": "https://example.com/new-card-image.jpg",
    "mana_cost": "3UU"
}
```

### DELETE /cards/<id>/

Deletes the card with the specified ID.

## Running the API

1. Install the required dependencies using pip:
```
pip install -r requirements.txt
```
2. Run the migrations to create the database tables:
```
python manage.py migrate
```
3. Start the development server:
```
python manage.py runserver
```
4. Use a tool like curl or Postman to test the API endpoints.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

This is just a basic example, and you can add more information as needed. You may also want to include information about authentication, error handling, and any other features of your API.
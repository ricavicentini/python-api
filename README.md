# Simple FastAPI Application

A basic FastAPI application with CRUD (in memory) operations for items.

## Setup

1. Install dependencies:
```bash
poetry install
```

2. Run the application:
```bash
poetry run uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Available Endpoints

- `GET /`: Welcome message
- `GET /items`: Get all items
- `GET /items/{item_id}`: Get a specific item
- `POST /items`: Create a new item
- `PUT /items/{item_id}`: Update an item
- `DELETE /items/{item_id}`: Delete an item

## Example Usage

```bash
# Create an item
curl -X POST "http://localhost:8000/items" -H "Content-Type: application/json" -d '{"name": "Test Item", "description": "This is a test item"}'

# Get all items
curl "http://localhost:8000/items"

# Get a specific item
curl "http://localhost:8000/items/0"

# Update an item
curl -X PUT "http://localhost:8000/items/0" -H "Content-Type: application/json" -d '{"name": "Updated Item", "description": "This is an updated item"}'

# Delete an item
curl -X DELETE "http://localhost:8000/items/0"
``` 
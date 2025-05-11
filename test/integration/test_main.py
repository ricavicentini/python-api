import os
import sys
from fastapi.testclient import TestClient
from uuid import UUID, uuid4

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def is_valid_uuid(uuid_str: str):
    """Check if the given string is a valid UUID."""
    try:
        UUID(uuid_str)
        return True
    except (ValueError, AttributeError, TypeError):
        return False

from src.main import app, Item

client = TestClient(app)

"""
Test suite for the main API endpoints.
This module contains integration tests for all CRUD operations
and edge cases of the API.
"""

def test_read_root():
    """
    Test the root endpoint.
    
    Expected behavior:
    - Status code: 200
    - Response: Welcome message
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Simple API"}

def test_create_item():
    """
    Test item creation endpoint.
    
    Expected behavior:
    - Status code: 200
    - Response: Created item with all fields matching input
    """
    # Test data for item creation
    item_data = {
        "name": "Test Item",
        "description": "This is a test item",
        "price": 10.99,
        "on_offer": False
    }
    response = client.post("/items", json=item_data)
    assert response.status_code == 200
    item_id = response.json()
    assert is_valid_uuid(item_id)
    
    

def test_read_items():
    """
    Test getting all items.
    
    Expected behavior:
    - Status code: 200
    - Response: List of items
    """
    response = client.get("/items")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_read_item():
    """
    Test getting a specific item by ID.
    
    Expected behavior:
    - Status code: 200
    - Response: Item matching the created item
    """
    # Create test item first
    item_data = {
        "name": "Test Item",
        "description": "This is a test item",
        "price": 10.99,
        "on_offer": False
    }
    create_response = client.post("/items", json=item_data)
    item_id = create_response.json()
    # Retrieve the created item
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == item_data["name"]
    assert data["description"] == item_data["description"]

def test_read_nonexistent_item():
    """
    Test getting a non-existent item.
    
    Expected behavior:
    - Status code: 404
    - Response: Error message about item not found
    """
    random_uuid = uuid4()  # Generate a random UUID that doesn't exist
    response = client.get(f"/items/{random_uuid}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"

def test_update_item():
    """
    Test updating an existing item.
    
    Expected behavior:
    - Status code: 200
    - Response: Updated item with new values
    """
    # Create initial item
    item_data = {
        "name": "Original Item",
        "description": "Original description",
        "price": 10.99,
        "on_offer": False
    }
    create_response = client.post("/items", json=item_data)
    item_id = create_response.json()
    
    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 200
    get_data = get_response.json()
    assert get_data["name"] == item_data["name"]
    assert get_data["description"] == item_data["description"]
    assert get_data["price"] == item_data["price"]
    assert get_data["on_offer"] == item_data["on_offer"]
    
    # Update the item
    updated_data = {
        "name": "Updated Item",
        "description": "Updated description",
        "price": 20.99,
        "on_offer": True
    }
    response = client.put(f"/items/{item_id}", json=updated_data)
    assert response.status_code == 200
    
    response = client.get(f"/items/{item_id}")
    data = response.json()
    # Verify all fields were updated
    assert data["name"] == updated_data["name"]
    assert data["description"] == updated_data["description"]
    assert data["price"] == updated_data["price"]
    assert data["on_offer"] == updated_data["on_offer"]

def test_update_nonexistent_item():
    """
    Test updating a non-existent item.
    
    Expected behavior:
    - Status code: 404
    - Response: Error message about item not found
    """
    random_uuid = uuid4()  # Generate a random UUID that doesn't exist
    item_data = {
        "name": "Test Item",
        "description": "Test description",
        "price": 10.99,
        "on_offer": False
    }
    response = client.put(f"/items/{random_uuid}", json=item_data)
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"

def test_delete_item():
    """
    Test deleting an item.
    
    Expected behavior:
    - Status code: 200
    - Response: Success message
    - Item should no longer exist
    """
    # Create item to delete
    item_data = {
        "name": "Test Item",
        "description": "Test description",
        "price": 10.99,
        "on_offer": False
    }
    create_response = client.post("/items", json=item_data)
    item_id = create_response.json()
    
    # Delete the item
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    
    # Verify item is gone
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 404

def test_delete_nonexistent_item():
    """
    Test deleting a non-existent item.
    
    Expected behavior:
    - Status code: 404
    - Response: Error message about item not found
    """
    random_uuid = uuid4()  # Generate a random UUID that doesn't exist
    response = client.delete(f"/items/{random_uuid}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"

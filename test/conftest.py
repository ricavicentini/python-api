import os
import sys
from uuid import UUID
import pytest
from fastapi.testclient import TestClient

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import app

@pytest.fixture
def client():
    """Create a test client for the FastAPI application."""
    return TestClient(app)

@pytest.fixture
def sample_item():
    """Create a sample item for testing."""
    return {
        "name": "Test Item",
        "description": "This is a test item",
        "price": 10.99,
        "tax": 1.99
    } 
    

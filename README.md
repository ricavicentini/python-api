# ⚠️ Warning
This is part of my Python learning path. The code and implementations here are for educational purposes.

## Project Description
This is a simple FastAPI application that demonstrates basic CRUD operations with a REST API.

## Features
- FastAPI framework
- Pydantic models for data validation
- Basic CRUD operations
- Type hints and documentation

## Setup
1. Create a virtual environment:
```bash
python -m venv .venv
```

2. Activate the virtual environment:
```bash
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the server:
```bash
uvicorn main:app --reload
```

The API will be available at http://127.0.0.1:8000
API documentation will be available at http://127.0.0.1:8000/docs

## API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `
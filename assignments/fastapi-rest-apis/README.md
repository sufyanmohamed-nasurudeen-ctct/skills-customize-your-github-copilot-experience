# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Students will build a REST API using the FastAPI framework. They will create endpoints, validate request data, and return clear HTTP responses for common CRUD actions.

## 📝 Tasks

### 🛠️ Create the FastAPI App and First Endpoint

#### Description
Set up a FastAPI project and create a basic API route to confirm the server is running correctly.

#### Requirements
Completed program should:

- Create a FastAPI app in `starter-code.py`
- Implement a GET endpoint at `/` that returns a JSON welcome message
- Run successfully with Uvicorn and respond at `http://127.0.0.1:8000/`


### 🛠️ Build Item CRUD Endpoints

#### Description
Add routes that let users create, read, update, and delete items from an in-memory store.

#### Requirements
Completed program should:

- Implement `POST /items`, `GET /items`, `GET /items/{item_id}`, `PUT /items/{item_id}`, and `DELETE /items/{item_id}`
- Use proper status codes (for example: 201 for create, 404 for missing items)
- Return JSON responses for each operation


### 🛠️ Add Validation and Error Handling

#### Description
Use Pydantic models to validate request data and provide helpful errors for invalid requests.

#### Requirements
Completed program should:

- Define a request model with fields for item name, price, and in_stock
- Reject invalid data types or missing required fields automatically
- Return a clear 404 error message when an item ID does not exist

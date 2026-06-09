# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using the FastAPI framework. You will define endpoints, add request and response models, and test your API locally.

## 📝 Tasks

### 🛠️ Create the FastAPI application

#### Description
Build a FastAPI app that manages a collection of items. The application should accept requests, return JSON responses, and handle missing items gracefully.

#### Requirements
Completed program should:

- Define a `FastAPI()` app instance.
- Add a `GET /` endpoint that returns a welcome message.
- Add a `GET /items/{item_id}` endpoint that returns item data by its ID.
- Return a `404` error when an item is not found.

### 🛠️ Define request and response models

#### Description
Use Pydantic models to validate request data and serialize responses.

#### Requirements
Completed program should:

- Define an `Item` model with `name`, `description`, and `price` fields.
- Use the model as the request body for creating or updating items.
- Return item data in JSON format for successful responses.

### 🛠️ Implement CRUD operations

#### Description
Add endpoints to create, update, and delete items in memory.

#### Requirements
Completed program should:

- Add a `POST /items` endpoint to create a new item.
- Add a `PUT /items/{item_id}` endpoint to update an existing item.
- Add a `DELETE /items/{item_id}` endpoint to remove an item.
- Use an in-memory dictionary to store items while the app is running.

### 💡 Run and test the API

#### Description
Start the FastAPI app and verify it works using example requests.

#### Requirements
Completed program should:

- Run with `uvicorn` and expose the API locally.
- Include sample request examples in comments or README.
- Confirm that FastAPI docs are available at `/docs`.

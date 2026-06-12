# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a RESTful API using the FastAPI framework that handles HTTP requests, manages data with different endpoints, and demonstrates proper request/response handling. You'll learn how to structure API endpoints, work with parameters, and return structured data.

## 📝 Tasks

### 🛠️ Create a Basic API with Multiple Endpoints

#### Description
Set up a FastAPI application with multiple GET endpoints that return different types of data. Start with a simple welcome endpoint, then add endpoints that return JSON data and demonstrate basic request handling.

#### Requirements
Completed program should:

- Run a FastAPI server (using `uvicorn` or similar)
- Have a GET `/` endpoint that returns a welcome message
- Have a GET `/items` endpoint that returns a list of items as JSON
- Have a GET `/items/{item_id}` endpoint that returns a specific item based on the ID
- Return proper JSON responses for all endpoints
- Include appropriate HTTP status codes

### 🛠️ Add Query Parameters and Data Validation

#### Description
Extend the API to accept query parameters and demonstrate input validation. Create endpoints that filter or process data based on optional query parameters passed by the client.

#### Requirements
Completed program should:

- Accept optional query parameters (e.g., `?skip=0&limit=10` for pagination)
- Filter or limit results based on query parameters
- Return different responses based on parameter values
- Demonstrate at least one optional and one required parameter
- Handle edge cases gracefully (missing parameters, invalid values)

### 🛠️ Implement POST/PUT Endpoints and Request Bodies

#### Description
Create endpoints that accept data from the client using request bodies. Implement both POST (create) and PUT (update) endpoints to manage data, demonstrating proper HTTP methods and data handling.

#### Requirements
Completed program should:

- Accept JSON request bodies in POST endpoints
- Create or store new data based on POST requests
- Update existing data with PUT endpoints
- Validate incoming data (check required fields, data types)
- Return appropriate responses (created item, confirmation, etc.)
- Use Python data classes or Pydantic models for request/response structures

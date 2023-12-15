# Django User Management API

Welcome to our Django User Management API!

## API Endpoints

To interact with user data, you can use the following API endpoints:

- **POST a New User:**
  Use the HTTP POST method to add a new user.
  Example: Send a POST request to `http://localhost:8000/home/user` with user details in the request body.

- **GET User Information:**
  Use the HTTP GET method to retrieve user information.
  Example: Send a GET request to `http://localhost:8000/home/user` to get user details.

Please use Postman or any HTTP client tool to make requests.

## API Usage Example

### POST Request Example

```http
POST http://localhost:8000/home/user
Content-Type: application/json

{
    "name": "John Doe",
    "age": 30,
    "email": "john@example.com",
    "address": "123 Street, City"
}

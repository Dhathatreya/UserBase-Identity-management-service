# Flask API with REST Endpoints

A Flask-based REST API application with user and product management functionality, connected to a MySQL database.

## Project Structure

```
.
├── app.py                    # Main Flask application
├── controller/
│   ├── __init__.py
│   ├── user_controller.py    # User-related endpoints
│   ├── product_controller.py # Product-related endpoints
│   └── product_categories.py
└── model/
    └── user_model.py         # Database models and queries
```

## Features

- **User Management**: Signup and retrieve user information
- **Product Management**: Add and manage products
- **MySQL Database Integration**: Connected to `flask_tutorial` database
- **RESTful API Endpoints**: Well-organized controller-model architecture

## Prerequisites

- Python 3.x
- Flask
- mysql-connector-python
- MySQL Server

## Installation

1. Clone or download this project
2. Install required dependencies:
   ```bash
   pip install flask mysql-connector-python
   ```

3. Configure the database connection in [model/user_model.py](model/user_model.py):
   - Update `host`, `user`, `password`, and `database` credentials

## API Endpoints

### User Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/user/signup` | Retrieve all users |
| POST | `/user/addone` | Add a new user |

**User Payload Example:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "1234567890",
  "roleid": 1,
  "password": "securepassword"
}
```

### Product Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/product/add` | Add a new product |

### General Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/home` | Home page |

## Running the Application

```bash
python app.py
```

The API will be available at `http://localhost:5000`

## Database Setup

Ensure your MySQL database has the following structure:

```sql
CREATE DATABASE flask_tutorial;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  phone VARCHAR(20),
  roleid INT,
  password VARCHAR(255)
);
```

## Important Notes

- Currently, user input validation and SQL injection prevention measures should be implemented
- Consider using parameterized queries instead of f-strings for database operations
- Store passwords securely (e.g., using bcrypt hashing)
- Add proper error handling and logging

## Future Improvements

- Add authentication and authorization
- Implement comprehensive error handling
- Add input validation
- Create database migration scripts
- Add unit tests
- Implement API documentation (Swagger/OpenAPI)

## License

This project is open source and available under the MIT License.

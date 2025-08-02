# Registration API - Postman Testing Guide

This directory contains a comprehensive Postman collection for testing the User Registration API.

## Collection Overview

The `Registration_API_Collection.json` file contains the following API tests:

### 1. API Root
- **Method:** GET
- **Endpoint:** `/api/`
- **Description:** Get API root information and available endpoints

### 2. User Registration Tests

#### Success Case
- **Method:** POST
- **Endpoint:** `/api/users/`
- **Description:** Register a new user with valid data
- **Sample Payload:**
```json
{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "mobile": "+1234567890",
    "location": "New York, NY"
}
```

#### Validation Tests
- **Duplicate Email:** Test email uniqueness validation
- **Invalid Email:** Test email format validation
- **Invalid Mobile:** Test mobile number format validation
- **Missing Fields:** Test required field validation

### 3. User Retrieval Tests
- **Get All Users:** Retrieve all registered users
- **Get User by ID:** Retrieve a specific user by ID
- **Get User by Email:** Retrieve a user by email address

### 4. User Management Tests
- **Update User:** Update an existing user's information
- **Delete User:** Delete a user by ID

## Setup Instructions

### 1. Import Collection to Postman
1. Open Postman
2. Click "Import" button
3. Select `Registration_API_Collection.json` file
4. The collection will be imported with all requests and environment variable

### 2. Environment Variables
The collection uses the following environment variable:
- `base_url`: Set to `http://localhost:8000` (Django backend URL)

### 3. Prerequisites
Make sure the following services are running:
- Django backend server on `http://localhost:8000`
- Database is properly configured and migrated

## Testing Workflow

### Basic Testing Sequence:
1. **API Root** - Verify the API is accessible
2. **Register User - Success** - Create a test user
3. **Get All Users** - Verify user was created
4. **Get User by ID** - Test individual user retrieval
5. **Get User by Email** - Test email-based lookup
6. **Update User** - Test user modification
7. **Delete User** - Test user deletion

### Validation Testing Sequence:
1. **Register User - Success** - Create a valid user first
2. **Register User - Duplicate Email** - Should return error
3. **Register User - Invalid Email** - Should return validation error
4. **Register User - Invalid Mobile** - Should return validation error
5. **Register User - Missing Fields** - Should return required field errors

## Expected Responses

### Successful Registration (201 Created):
```json
{
    "message": "User registered successfully!",
    "user": {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "mobile": "+1234567890",
        "location": "New York, NY",
        "created_at": "2024-01-01T12:00:00Z",
        "updated_at": "2024-01-01T12:00:00Z"
    }
}
```

### Validation Error (400 Bad Request):
```json
{
    "message": "Registration failed",
    "errors": {
        "email": ["A user with this email already exists."]
    }
}
```

### User List (200 OK):
```json
[
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "mobile": "+1234567890",
        "location": "New York, NY",
        "created_at": "2024-01-01T12:00:00Z",
        "updated_at": "2024-01-01T12:00:00Z"
    }
]
```

## Manual Testing with cURL

If you prefer command-line testing, here are some cURL examples:

### Register a new user:
```bash
curl -X POST http://localhost:8000/api/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test User",
    "email": "test@example.com",
    "mobile": "+1234567890",
    "location": "Test Location"
  }'
```

### Get all users:
```bash
curl -X GET http://localhost:8000/api/users/
```

### Get user by ID:
```bash
curl -X GET http://localhost:8000/api/users/1/
```

## Troubleshooting

### Common Issues:
1. **Connection refused:** Make sure Django server is running on port 8000
2. **CORS errors:** Verify CORS settings in Django settings.py
3. **Database errors:** Ensure database migrations are applied
4. **Validation errors:** Check request payload format and required fields

### Debug Steps:
1. Check Django server logs for detailed error messages
2. Verify API endpoints are correctly configured
3. Test with simple GET requests first
4. Ensure all required fields are included in POST requests
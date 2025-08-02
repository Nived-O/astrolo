# User Registration Full-Stack Application

A complete user registration system built with Next.js frontend, Django REST API backend, and comprehensive API testing.

## 🏗️ Architecture

```
Frontend (Next.js) ← HTTP API → Backend (Django REST API) ← ORM → Database (SQLite/MySQL)
    Port 3000                        Port 8000                      Local DB
```

## 🚀 Features

### Frontend (Next.js)
- ✅ Modern, responsive registration form
- ✅ Real-time form validation with Zod
- ✅ React Hook Form for efficient form handling
- ✅ Tailwind CSS for beautiful UI
- ✅ TypeScript for type safety
- ✅ Axios for API communication
- ✅ Success/error message handling

### Backend (Django REST API)
- ✅ RESTful API endpoints
- ✅ User model with Name, Email, Mobile, Location
- ✅ Comprehensive validation (email uniqueness, mobile format)
- ✅ CORS configuration for frontend integration
- ✅ Django REST Framework serializers
- ✅ SQLite database (MySQL ready)

### API Testing
- ✅ Complete Postman collection
- ✅ cURL examples
- ✅ Validation testing scenarios
- ✅ CRUD operations testing

## 📋 Requirements Met

✅ **Frontend**: Next.js with HTML forms  
✅ **Backend**: Django REST API with Python  
✅ **Database**: SQLite (MySQL configuration included)  
✅ **API Testing**: Postman collection provided  
✅ **Form Fields**: Name, Email, Mobile, Location  

## 🛠️ Setup Instructions

### Prerequisites
- Node.js 18+ and npm
- Python 3.8+
- (Optional) MySQL server

### 1. Backend Setup

```bash
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start Django server
python manage.py runserver 0.0.0.0:8000
```

The backend will be available at: `http://localhost:8000`

### 2. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start Next.js development server
npm run dev
```

The frontend will be available at: `http://localhost:3000`

### 3. API Testing Setup

#### Using Postman:
1. Import `postman/Registration_API_Collection.json` into Postman
2. The collection includes all endpoints with test data
3. Base URL is set to `http://localhost:8000`

#### Using cURL:
```bash
# Test API root
curl -X GET http://localhost:8000/api/

# Register a user
curl -X POST http://localhost:8000/api/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "mobile": "+1234567890",
    "location": "New York, NY"
  }'

# Get all users
curl -X GET http://localhost:8000/api/users/
```

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/` | API root information |
| POST | `/api/users/` | Register new user |
| GET | `/api/users/` | Get all users |
| GET | `/api/users/{id}/` | Get user by ID |
| GET | `/api/users/email/{email}/` | Get user by email |
| PUT | `/api/users/{id}/` | Update user |
| DELETE | `/api/users/{id}/` | Delete user |

## 📝 Form Validation

### Frontend Validation (Zod)
- **Name**: Minimum 2 characters
- **Email**: Valid email format
- **Mobile**: Phone number format (+1234567890)
- **Location**: Minimum 2 characters

### Backend Validation (Django)
- **Email**: Uniqueness validation
- **Mobile**: Regex pattern validation
- **All fields**: Required field validation

## 🧪 Testing Scenarios

### Successful Registration
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "mobile": "+1234567890",
  "location": "New York, NY"
}
```

### Validation Errors
- Duplicate email
- Invalid email format
- Invalid mobile number
- Missing required fields

## 📁 Project Structure

```
.
├── backend/                 # Django REST API
│   ├── registration_backend/
│   │   ├── settings.py     # Django configuration
│   │   └── urls.py         # Main URL routing
│   ├── users/              # Users app
│   │   ├── models.py       # User model
│   │   ├── serializers.py  # API serializers
│   │   ├── views.py        # API views
│   │   └── urls.py         # Users URL routing
│   ├── requirements.txt    # Python dependencies
│   └── manage.py           # Django management
├── frontend/               # Next.js frontend
│   ├── src/
│   │   └── app/
│   │       ├── page.tsx    # Registration form
│   │       └── layout.tsx  # App layout
│   ├── package.json        # Node dependencies
│   └── tailwind.config.js  # Tailwind configuration
├── postman/                # API testing
│   ├── Registration_API_Collection.json
│   └── README.md           # Testing guide
└── README.md               # This file
```

## 🚀 Deployment Notes

### Database Migration to MySQL
Update `backend/registration_backend/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'registration_db',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Production Considerations
1. **Security**: Update SECRET_KEY and disable DEBUG
2. **CORS**: Configure specific allowed origins
3. **Database**: Use PostgreSQL or MySQL in production
4. **Static Files**: Configure static file serving
5. **Environment Variables**: Use environment-specific configs

## 🛠️ Technologies Used

### Frontend
- **Next.js 14**: React framework with App Router
- **TypeScript**: Static type checking
- **Tailwind CSS**: Utility-first CSS framework
- **React Hook Form**: Efficient form handling
- **Zod**: Schema validation
- **Axios**: HTTP client

### Backend
- **Django 4.2**: Python web framework
- **Django REST Framework**: API development
- **django-cors-headers**: CORS handling
- **SQLite**: Development database
- **mysqlclient**: MySQL connector (optional)

### Development Tools
- **Postman**: API testing
- **cURL**: Command-line API testing
- **ESLint**: JavaScript linting
- **Python virtual environment**: Dependency isolation

## 🐛 Troubleshooting

### Common Issues
1. **Port conflicts**: Ensure ports 3000 and 8000 are available
2. **CORS errors**: Check Django CORS settings
3. **Database errors**: Run migrations after model changes
4. **Import errors**: Verify virtual environment activation

### Debug Commands
```bash
# Check if servers are running
curl http://localhost:8000/api/
curl http://localhost:3000/

# View Django logs
cd backend && python manage.py runserver --verbosity=2

# View Next.js logs
cd frontend && npm run dev
```

## 📄 License

This project is created for demonstration purposes.
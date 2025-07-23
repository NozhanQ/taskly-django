# Django To-Do List Application

A full-featured task management web application built with Django, featuring user authentication, CRUD operations, and persistent data storage.

## 🏗️ Backend Architecture

### Framework & Technologies
- **Django 4.x** - Python web framework
- **PostgreSQL** - Production-grade relational database
- **psycopg2** - PostgreSQL adapter for Python
- **Django ORM** - Object-Relational Mapping
- **Django Forms** - Form handling and validation
- **Django Authentication** - Built-in user management

## 📊 Database Schema

### Models

#### User Model
Uses Django's built-in `User` model with the following key fields:
- `username` - Unique user identifier
- `password` - Hashed password storage
- `email` - User email address
- `date_joined` - Account creation timestamp

#### Task Model
```python
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```

**Field Descriptions:**
- `title` - Task description (max 200 characters)
- `completed` - Boolean flag for task status
- `created_at` - Automatic timestamp on creation
- `updated_at` - Automatic timestamp on modification
- `user` - Foreign key relationship to User model

**Relationships:**
- One-to-Many: User → Tasks (One user can have multiple tasks)
- CASCADE deletion: When user is deleted, all their tasks are deleted

## 🔐 Authentication System

### User Registration
- **Endpoint:** `/register/`
- **Method:** GET/POST
- **Features:**
  - Username uniqueness validation
  - Password strength requirements
  - Automatic login after registration
  - CSRF protection

### User Login
- **Endpoint:** `/login/`
- **Method:** GET/POST
- **Features:**
  - Session-based authentication
  - "Remember me" functionality
  - Redirect after successful login
  - Invalid credentials handling

### User Logout
- **Endpoint:** `/logout/`
- **Method:** POST
- **Features:**
  - Session termination
  - CSRF token validation
  - Redirect to login page

## 🛠️ API Endpoints

### Task Management

#### List & Create Tasks
```
GET/POST /tasks/
```
- **GET:** Display all user's tasks with create form
- **POST:** Create new task
- **Authentication:** Required
- **Permissions:** User can only see their own tasks

#### Toggle Task Status
```
POST /tasks/<int:task_id>/toggle/
```
- **Purpose:** Mark task as complete/incomplete
- **Method:** POST (form submission)
- **Validation:** User ownership verification
- **Redirect:** Back to task list

#### Edit Task
```
GET/POST /tasks/<int:task_id>/edit/
```
- **GET:** Display task list with inline edit form
- **POST:** Update task title
- **Validation:** 
  - User ownership
  - Title length limits
  - CSRF protection

#### Delete Task
```
POST /tasks/<int:task_id>/delete/
```
- **Purpose:** Permanently remove task
- **Method:** POST only (prevents accidental deletion)
- **Validation:** User ownership verification
- **Redirect:** Back to task list

## 🔒 Security Features

### CSRF Protection
- All forms include `{% csrf_token %}`
- POST requests validated against CSRF attacks
- Automatic token generation and validation

### User Authorization
- Login required decorators on all task views
- Task ownership validation on all operations
- Session-based authentication

### Data Validation
- Form field validation (max lengths, required fields)
- Model-level constraints
- SQL injection prevention through ORM

### Password Security
- Django's built-in password hashing (PBKDF2)
- Configurable password validators
- Secure session management

## 📁 Project Structure

```
todo_project/
├── manage.py
├── todo_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── todo_app/
│   ├── __init__.py
│   ├── models.py          # Task and User models
│   ├── views.py           # Business logic
│   ├── forms.py           # Form definitions
│   ├── urls.py            # URL routing
│   ├── admin.py           # Admin interface
│   └── migrations/        # Database migrations
└── templates/
    ├── registration/
    │   ├── login.html
    │   └── register.html
    └── tasks/
        └── task_list.html
```

## ⚙️ Configuration

### Settings.py Key Configurations

#### Database
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'todo_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

#### Authentication
```python
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/tasks/'
LOGOUT_REDIRECT_URL = '/login/'
```

#### Security
```python
SECRET_KEY = 'your-secret-key'
DEBUG = False  # For production
ALLOWED_HOSTS = ['your-domain.com']
CSRF_COOKIE_SECURE = True  # For HTTPS
SESSION_COOKIE_SECURE = True  # For HTTPS
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- PostgreSQL 12+ installed and running
- psycopg2 or psycopg2-binary
- pip (Python package manager)
- Virtual environment (recommended)

### Database Setup
```bash
# Install PostgreSQL (Ubuntu/Debian)
sudo apt update
sudo apt install postgresql postgresql-contrib

# Start PostgreSQL service
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Create database and user
sudo -u postgres psql
CREATE DATABASE todo_db;
CREATE USER your_db_user WITH PASSWORD 'your_db_password';
GRANT ALL PRIVILEGES ON DATABASE todo_db TO your_db_user;
ALTER USER your_db_user CREATEDB;
\q
```

### Installation Steps
```bash
# Clone repository
git clone <repository-url>
cd todo-app

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install django psycopg2-binary

# Configure database settings (see Configuration section)
# Update DATABASES in settings.py

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### Environment Variables
Create a `.env` file for sensitive configurations:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=todo_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

### Using Environment Variables in Settings
```python
import os
from pathlib import Path

# Database configuration using environment variables
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'todo_db'),
        'USER': os.getenv('DB_USER', 'your_db_user'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'your_db_password'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
```

## 🗄️ Database Operations

### Migrations
```bash
# Create new migration
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# View migration status
python manage.py showmigrations

# Reverse migration
python manage.py migrate app_name migration_name
```

### Admin Interface
- Access: `/admin/`
- Features: Task and User management
- Requires superuser account

## 🔍 Business Logic Flow

### Task Creation Flow
1. User submits task form via POST
2. Form validation (CSRF, field validation)
3. User authentication check
4. Task object creation with user association
5. Database commit
6. Redirect to task list

### Task Status Toggle Flow
1. User clicks checkbox (triggers form submission)
2. POST request to toggle endpoint
3. Task ownership verification
4. Boolean field update in database
5. Scroll position preservation
6. Page refresh with updated status

### Edit Task Flow
1. User clicks edit button (GET request with edit parameter)
2. Task list loads with inline edit form
3. User submits changes (POST request)
4. Form validation and ownership check
5. Database update
6. Redirect to clean task list URL

## 📊 Performance Considerations

### Database Optimization
- PostgreSQL-specific indexing strategies
- Connection pooling with pgbouncer
- Query optimization with EXPLAIN ANALYZE
- Efficient querysets with `select_related()` and `prefetch_related()`
- Pagination for large task lists
- Database-level constraints and triggers

### PostgreSQL Specific Features
- **JSONB fields** for future metadata storage
- **Full-text search** capabilities
- **Partial indexes** for completed/incomplete tasks
- **Database views** for complex queries
- **Stored procedures** for complex business logic

### Caching Strategy
- Session caching for user data
- Template fragment caching
- Static file caching
- Database query caching

## 🧪 Testing Strategy

### Unit Tests
- Model validation tests
- Form validation tests  
- View logic tests
- Authentication tests

### Integration Tests
- End-to-end user workflows
- Database transaction tests
- Security vulnerability tests

### Example Test Structure
```python
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Task

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
        
    def test_task_creation(self):
        task = Task.objects.create(title='Test Task', user=self.user)
        self.assertEqual(task.title, 'Test Task')
        self.assertFalse(task.completed)
```

## 🚀 Deployment

### Production Checklist
- [ ] Set `DEBUG = False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up production PostgreSQL database
- [ ] Configure database connection pooling
- [ ] Set up SSL/TLS for database connections
- [ ] Configure static file serving
- [ ] Set up HTTPS certificates
- [ ] Configure environment variables
- [ ] Set up automated PostgreSQL backups
- [ ] Configure logging
- [ ] Set up monitoring (PostgreSQL + Django)
- [ ] Configure PostgreSQL performance tuning

### Docker Deployment with PostgreSQL
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

```yaml
# docker-compose.yml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      - DB_NAME=todo_db
      - DB_USER=postgres
      - DB_PASSWORD=password
      - DB_HOST=db
      - DB_PORT=5432
  
  db:
    image: postgres:13
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    environment:
      - POSTGRES_DB=todo_db
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
    ports:
      - "5432:5432"

volumes:
  postgres_data:
```

## 📈 Monitoring & Maintenance

### Logging
- Django's built-in logging framework
- User action logging
- Error tracking and reporting
- Performance monitoring

### Database Maintenance
- PostgreSQL automated backup with pg_dump
- Database optimization with VACUUM and ANALYZE
- Connection monitoring and pooling
- Index maintenance and performance tuning
- Migration management
- Query performance monitoring with pg_stat_statements

### PostgreSQL Backup Strategy
```bash
# Daily backup script
#!/bin/bash
BACKUP_DIR="/path/to/backups"
DB_NAME="todo_db"
DATE=$(date +%Y%m%d_%H%M%S)

pg_dump -h localhost -U your_db_user -d $DB_NAME > $BACKUP_DIR/todo_backup_$DATE.sql

# Keep only last 7 days of backups
find $BACKUP_DIR -name "todo_backup_*.sql" -mtime +7 -delete
```

## 🤝 Contributing

### Development Workflow
1. Fork repository
2. Create feature branch
3. Write tests for new features
4. Implement changes
5. Run test suite
6. Submit pull request

### Code Standards
- PEP 8 Python style guide
- Django best practices
- Comprehensive docstrings
- Unit test coverage > 80%

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

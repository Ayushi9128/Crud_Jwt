# User Management REST API

A Flask-based REST API with JWT authentication, CRUD operations, and Pytest test suite.

# User Management REST API

A Flask-based REST API with JWT authentication, CRUD operations, and Pytest test suite.

## Tech Stack
- Python 3.11, Flask 3.x
- SQLite (via Flask-SQLAlchemy)
- Flask-JWT-Extended (JWT auth)
- Pytest (12 tests, 90%+ coverage)
- Docker + Docker Compose
- Gunicorn (production WSGI server)

## Endpoints
| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | /auth/register | No | Create account |
| POST | /auth/login | No | Get JWT token |
| GET | /users | Yes | List all users |
| GET | /users/:id | Yes | Get single user |
| PUT | /users/:id | Yes | Update profile |
| DELETE | /users/:id | Yes | Delete account |

## Run Locally

### Without Docker
```bash
pip install -r requirements.txt
python app.py    
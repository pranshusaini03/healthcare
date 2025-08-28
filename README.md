# Healthcare Backend (Django)

A modular Django backend for a healthcare application, organized into apps for users, patients, doctors, and general API endpoints. This README explains setup, development workflow, and how to contribute.

---

## Features

- **Modular Django project**: separate apps for `users`, `patients`, `doctors`, and `api`
- **SQLite by default**: easy local setup; can be swapped for PostgreSQL/MySQL
- **Django REST Framework-ready**: serializers and views organized for APIs
- **Admin interface**: manage models via Django Admin
- **Migrations included**: initial schema and patient-doctor mapping

---

## Tech Stack

- **Backend**: Django (Python)
- **API**: Django REST Framework (DRF)
- **Database**: SQLite (development), configurable for Postgres/MySQL
- **ASGI/WSGI**: Ready for `gunicorn`/`uvicorn` in production

---

## Project Structure

```
healthcare-main/
  ├─ healthcare-main/
  │  ├─ api/
  │  ├─ core/
  │  ├─ doctors/
  │  ├─ healthcare/
  │  ├─ patients/
  │  ├─ users/
  │  ├─ db.sqlite3
  │  └─ manage.py
  └─ README.md
```

Key folders/files:
- `healthcare/` – Django project settings, URLs, ASGI/WSGI
- `api/` – shared API endpoints and serializers
- `users/` – user models, serializers, views, and URLs
- `patients/` – patient domain logic
- `doctors/` – doctor domain logic
- `core/` – shared/core utilities (if any)
- `manage.py` – Django management entrypoint
- `db.sqlite3` – default development database

---

## Getting Started

These steps assume Windows PowerShell, but the commands are similar for macOS/Linux.

### 1) Prerequisites
- Python 3.10+
- pip
- (Optional) virtualenv or venv

Check versions:
```powershell
python --version
pip --version
```

### 2) Clone the Repository
```powershell
# If you haven’t already
git clone <YOUR_REPO_URL>.git
cd healthcare-main
```

### 3) Create and Activate a Virtual Environment
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

> On macOS/Linux:
> ```bash
> python3 -m venv .venv
> source .venv/bin/activate
> ```

### 4) Install Dependencies

If `requirements.txt` exists:
```powershell
pip install -r requirements.txt
```

If not, install core packages manually:
```powershell
pip install django djangorestframework
```

### 5) Database Setup

Navigate to the inner project folder that has `manage.py`:
```powershell
cd .\healthcare-main\
```

Run migrations:
```powershell
python manage.py migrate
```

Create a superuser (admin account):
```powershell
python manage.py createsuperuser
```

### 6) Run the Development Server
```powershell
python manage.py runserver
```

App will be available at `http://127.0.0.1:8000/`.

Django admin at `http://127.0.0.1:8000/admin/`.

---

## Configuration

### Environment Variables
This project works out-of-the-box with SQLite. For production, configure environment variables and a secure settings module. Common variables:

- `DJANGO_SETTINGS_MODULE` – defaults to `healthcare.settings`
- `SECRET_KEY` – ensure a strong key in production
- `DEBUG` – set to `False` in production
- `ALLOWED_HOSTS` – add your domains/IPs
- Database settings via `DATABASES` in `healthcare/settings.py`

### Switching to PostgreSQL (example)
In `healthcare/healthcare/settings.py`, update `DATABASES`:
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "healthcare",
        "USER": "postgres",
        "PASSWORD": "<password>",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```
Install the driver:
```powershell
pip install psycopg2-binary
```

---

## API Overview

This codebase is organized for REST APIs. Actual endpoints are defined in each app’s `urls.py` and wired through the project `healthcare/urls.py`.

- Project URLs: `healthcare/healthcare/urls.py`
- App URLs (examples):
  - `healthcare/users/urls.py`
  - `healthcare/api/urls.py`

To explore available endpoints during development, open the URLs files or visit the root route if DRF’s browsable API is enabled.

### Example: Listing Routes
If `api/urls.py` exposes routes under `/api/`, you can test with:
```bash
curl -X GET http://127.0.0.1:8000/api/
```

### Auth
If authentication is required (e.g., session auth or token/JWT), follow the endpoints documented in `users/urls.py` and `users/views.py`. Otherwise, use Django admin to create users and manage permissions.

---

## Running Tests

If tests are present:
```powershell
python manage.py test
```

Add tests in each app’s `tests.py`.

---

## Admin & Models

- Enable models in the admin by registering them in each app’s `admin.py`.
- Run `python manage.py makemigrations` after model changes.
- Apply changes with `python manage.py migrate`.

---

## Common Commands

```powershell
# Make new migrations for model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver

# Open Django shell
python manage.py shell
```

---

## Coding Standards

- Follow Django best practices and app separation
- Keep functions and classes small and purposeful
- Add/maintain docstrings for complex logic
- Write tests for critical logic and endpoints

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feat/my-feature`
3. Commit changes: `git commit -m "feat: add my feature"`
4. Push to branch: `git push origin feat/my-feature`
5. Open a Pull Request with a clear description

Please ensure:
- Code is formatted and linted
- Tests pass locally
- Migrations are included (if models changed)

---

## Deployment Notes

- Set `DEBUG=False` and configure `ALLOWED_HOSTS`
- Use a production-ready server (e.g., `gunicorn` with `nginx`)
- Configure a persistent database (PostgreSQL recommended)
- Collect static files if relevant: `python manage.py collectstatic`

---

## License

Add your license text here (e.g., MIT). If you’re unsure, MIT is a common choice for open-source projects.

---

## Maintainers

- Add your name(s) and contact info here.

---

## Troubleshooting

- "Module not found" or import errors: ensure you’re in the inner directory with `manage.py`
- Database locked or migration issues: remove `db.sqlite3` for a clean start (development only) and rerun migrations
- Static files not loading: check `STATIC_URL` and `STATIC_ROOT` in settings, and run `collectstatic` in production 

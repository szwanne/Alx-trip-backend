# 🧳 Trip Planner API

A backend API built with **Django** and **Django REST Framework (DRF)** for managing trips, destinations, activities, bookings, and users.

The API allows users to:

- Create, update, delete, and view trips.
- Manage destinations, activities, and bookings.
- Authenticate and manage user accounts.
- Search and filter trips by destination, activities, and dates.

---

## 🚀 Features

### ✅ Trip Management (CRUD)

- Create, Read, Update, and Delete trips.
- Each trip includes:
  - Title
  - Description
  - Destinations
  - Activities
  - Start Date / End Date
  - Trip Members
  - Bookings (flights, hotels, etc.)
  - Created Date

### 👤 User Management (CRUD)

- Register, login, and manage users.
- Each user has a unique username, email, and password.
- Only authenticated users can create, update, or delete their own trips.

### 🌍 Destination & Activity Management

- View and manage destinations and activities.
- Filter trips by destination (e.g., "Paris") or activity (e.g., "Hiking").

### 🔎 Search & Filtering

- Search trips by title, destination, activity, or dates.
- Optional filters for duration, number of travelers, etc.

### ⚡ Authentication & Permissions

- Authentication required for creating, updating, or deleting trips.
- Permission checks to ensure users can only edit or delete their own trips.
- Supports session-based or JWT authentication (optional).

### 📊 Pagination & Sorting

- Pagination support for large trip listings.
- Sort trips by start date, end date, or duration.

---

## 🛠️ Tech Stack

- **Backend Framework:** Django, Django REST Framework
- **Database:** SQLite (default), can switch to PostgreSQL/MySQL in production
- **Authentication:** Django auth system (with optional JWT support)
- **Deployment:** Heroku / PythonAnywhere

---

## 📂 Project Structure

backend/
│
├── trip/ # Trip management app
├── api/ # API endpoints
├── backend/ # Project settings & wsgi
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md

---

## ⚙️ Installation & Setup

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/trip-planner-api.git
cd trip-planner-api/backend
```

2. **Create and activate a virtual environment:**

```bash

python3 -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows

```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Configure environment variables by creating a .env file:**

```ini
SECRET_KEY=your-django-secret-key
DJANGO_ENV=development
DEBUG=True
DB_PASSWORD=your-db-password
DATABASE_URL=postgresql://postgres:your-db-password@host:port/database
ALLOWED_HOSTS=localhost,127.0.0.1
```

5. **Run migrations:**

```bash
python manage.py migrate
```

6. **Create a superuser:**

```bash
python manage.py createsuperuser
```

7. **Run the development server:**

```bash
python manage.py runserver
```

Server will be accessible at: http://127.0.0.1:8000/

### 📝 API Endpoints

| Endpoint              | Method | Description                       |
| --------------------- | ------ | --------------------------------- |
| `/api/trips/`         | GET    | List all trips                    |
| `/api/trips/`         | POST   | Create a new trip (auth required) |
| `/api/trips/<id>/`    | GET    | Retrieve a specific trip          |
| `/api/trips/<id>/`    | PUT    | Update a trip (auth required)     |
| `/api/trips/<id>/`    | DELETE | Delete a trip (auth required)     |
| `/api/destinations/`  | GET    | List all destinations             |
| `/api/activities/`    | GET    | List all activities               |
| `/api/bookings/`      | GET    | List all bookings                 |
| `/api/token/`         | POST   | Obtain JWT token                  |
| `/api/token/refresh/` | POST   | Refresh JWT token                 |

All endpoints support JSON requests and responses. Authenticated endpoints require the JWT token in the header:

```makefile
Authorization: Bearer <your-token>
```

### Deployment

1. Set environment variables on your hosting platform (Render, Heroku, etc.).

2. Use DATABASE_URL for your production database.

3. Ensure DEBUG=False and proper ALLOWED_HOSTS are configured.

4. Collect static files before deploying:

```bash
python manage.py collectstatic

```

### 📄 API Documentation

- DRF browsable API available at /api/ when running the server locally.

- Swagger / OpenAPI docs available if drf_yasg is enabled: /swagger/ or /redoc/.

### 🎯 Notes

- Use PostgreSQL in production (e.g., Supabase) for reliability.

- JWT authentication is recommended for API security.

- Make sure your database credentials are correct in .env or DATABASE_URL.

- Pagination is applied to all list endpoints (default 15 items per page).

### ✨ License

MIT License

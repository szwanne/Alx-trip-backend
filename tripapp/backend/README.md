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

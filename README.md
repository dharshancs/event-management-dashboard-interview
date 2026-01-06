# 🎟️ Event Management Dashboard

A full-stack **Event Management Dashboard** built with Flask, designed as a take-home interview assignment.

The application supports **role-based access** for organisers and users, real-time registration tracking, and notification logic for upcoming events. This repository is retained to demonstrate backend design decisions, time-bound implementation, and learning outcomes.

---

## 📌 Project Context

This project was implemented as part of a **time-constrained interview assignment**. The focus was on:

* Clean backend structure
* Correct data flow and integrity
* Feature completeness within limited time

The project is **functional**, but not production-hardened.

---

## ✨ Key Features

### 👤 User Features

* User registration and authentication
* Browse all available events
* Register for events
* View real-time attendee counts (via polling)
* Upcoming event notifications (within next 3 days)

### 🛠 Organiser Features

* Organiser-only dashboard
* Create and manage events
* View registration counts per event

---

## ⚡ Real-Time Updates

The User Dashboard displays **live registration counts** using:

* A lightweight API endpoint (`/user/api/stats`)
* JavaScript polling every 5 seconds

This avoids page reloads while keeping implementation simple and backend-focused.

---

## 🔔 Notification Logic

On user login, the system:

* Checks registered events
* Identifies events occurring within the next **3 days**
* Displays prominent reminder alerts

This demonstrates server-side date handling and user-specific logic.

---

## 🧱 Architecture Overview

The project follows a **modular Flask structure**:

```
controllers/   → Route handlers & business logic
models/        → Database schema & initialization
templates/     → Jinja2 HTML templates
main.py        → Application entry point
```

Key architectural choices:

* Flask Blueprints for role separation
* SQLite with foreign key constraints
* Custom decorators for access control

---

## 🛠 Tech Stack

| Layer    | Technologies                        |
| -------- | ----------------------------------- |
| Backend  | Python, Flask                       |
| Frontend | HTML, Bootstrap, Jinja2, JavaScript |
| Database | SQLite                              |
| Security | Werkzeug password hashing           |

---

## 🚀 Running the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/dharshancs/event-management-dashboard-interview.git
cd Event-Management-Dashboard
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
python main.py
```

The app will run at:

```
http://127.0.0.1:5000
```

---

## 📊 What This Project Demonstrates

* Role-based access control (RBAC)
* Backend-driven dashboards
* Real-time UI updates via polling
* Relational database modeling
* Time-bound implementation tradeoffs
* Clean separation of concerns

---

## 📌 Status

Completed as an **interview assignment**.

Maintained on GitHub for:

* Reference
* Learning review
* Demonstrating backend fundamentals

---

## 👨‍💻 Author

**Dharshan C S**
Aspiring Software Engineer

---

## 📄 License

For educational and portfolio use only.

# Event Management Dashboard

This project is a full-stack **Event Management Dashboard** built using **Flask**.  
It allows **organizers** to create and manage events, while **users** can browse events, register for them, and view real-time updates on event registrations.


## 🚀 Key Features

* **Role-Based Access Control (RBAC):**
    * **Organizers:** Dedicated dashboard to create and manage events.
    * **Users:** Separate dashboard to browse events, view details, and register.
* **⚡ Real-Time Updates:**
    * The User Dashboard tracks registration counts live. The application uses JavaScript polling to fetch updates from the backend every 5 seconds, ensuring the "Total Attendees" count is always accurate without needing a page refresh.
* **🔔 Smart Notifications (Bonus Requirement):**
    * Implemented a logic-based alert system. When a user logs in, the dashboard checks for any registered events happening in the **next 3 days** and displays a high-visibility alert at the top of the screen.
* **🔒 Security:**
    *The application uses `Werkzeug` security helpers to hash and salt passwords before storage.
    *Routes are protected by custom `@login_required` and `@admin_required` decorators.

## 🛠️ Tech Stack

* **Backend:** Python 3, Flask
* **Database:** SQLite3 (Native)
* **Frontend:** HTML5, Bootstrap 5, Jinja2, JavaScript (Fetch API)

## 📂 Project Structure

```text
Event_Management/
├── controllers/          # Modular Blueprints
│   ├── base_view.py      # Authentication (Login/Register/Logout)
│   ├── organiser_view.py # Event Creation Logic
│   └── user_view.py      # Booking Logic & Real-time Stats API
├── models/               # Database Logic
│   ├── config.py         # Admin User Setup
│   └── database.py       # SQL Schema & Table Creation
├── templates/            # Frontend Views
└── main.py               # Entry Point


```
## ⚙️ Setup & Installation

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/23f3004028/Event-Management-Dashboard.git](https://github.com/23f3004028/Event-Management-Dashboard.git)
    cd Event-Management-Dashboard
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application**
    ```bash
    python main.py
    ```
    *The application will run at `http://127.0.0.1:5000`*

### 📝 Note on Development

**Frontend Assets:** To prioritize functionality and ensure robust backend logic within the time constraints, the frontend templates (HTML/CSS structure) were adapted from my previous academic project: [Vehicle Parking App](https://github.com/23f3004028/23f3004028).

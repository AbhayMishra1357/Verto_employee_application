# 🚀 Employee Manager - Django CRUD Application

A **modern and full-featured CRUD (Create, Read, Update, Delete) application** to manage employees efficiently. Built with Django, Django REST Framework, and a clean frontend interface with HTML, CSS, and JavaScript.

---

## 🌟 Features

### Core Features

* **CRUD API for Employees**

  * Create, Read, Update, Delete employee records
  * Fields: `name`, `email`, `position`, `created_at`, `updated_at`
  * RESTful API endpoints at `/api/employees/`
* **Frontend**

  * View all employees in a responsive table
  * Add new employees using a form
  * Edit employees using modal or separate page
  * Delete employees with a single click

### Bonus Features ✨

* Search and filter employees by name
* Export employee data as **CSV**
* Send emails to employees
* Frontend **form validation**
* Backend **unit tests** for API and business logic


## 🏗️ Tech Stack

* **Backend:** Django, Django REST Framework, SQLite
* **Frontend:** HTML, CSS, JavaScript
* **Export:** CSV download

---

## ⚡ Project Structure

```
employee_project/
├── employee_project/
│   ├── settings.py
│   ├── urls.py
│   └── asgi.py
├── employees/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
│   └── templates/employees/
│       └── home.html
├── db.sqlite3
├── manage.py
└── README.md
```

---

## 🚀 Installation & Running

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/employee-manager.git
cd employee_project
```

### 2️⃣ Setup Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6️⃣ Run Server

```bash
python manage.py runserver
```

Visit:

* **Frontend:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **API:** [http://127.0.0.1:8000/api/employees/](http://127.0.0.1:8000/api/employees/)
* **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📱 Running on Other Devices

1. Make sure your device is on the **same network** as your server machine.
2. Find your local IP:

```bash
# Windows
ipconfig
# macOS/Linux
ifconfig
```

3. Run Django server on all interfaces:

```bash
python manage.py runserver 0.0.0.0:8000
```

4. Access from your device using:

```
http://<your-local-ip>:8000/
```


## ✉️ Email Integration

* Configure your SMTP credentials in `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'youremail@gmail.com'
EMAIL_HOST_PASSWORD = 'yourpassword'
```

* Use the frontend “Send Email” button to send emails to employees.

---

## 📄 CSV Export

* Click **“Download CSV”** on the frontend to export all employees.
* CSV includes: `ID, Name, Email, Position, Created At, Updated At, Mobile number, department, joining date, Salary `.

---

## 💡 Notes

* Make sure to **run migrations** after updating models.
* Use **virtual environment** to avoid dependency conflicts.
* For production, switch **DEBUG = False** in `settings.py` and configure proper SMTP and database.

---

## 📝 License

MIT License © 2025 - Abhay Mishra

---

## 🙌 Contribution

* Fork the repository
* Create a feature branch
* Commit your changes
* Open a pull request

---

## ❤️ Author

**Abhay Mishra**

* GitHub: [https://github.com/AbhayMishra1357](https://github.com/AbhayMishra1357)
* LinkedIn: [https://www.linkedin.com/in/abhay-mishra-38607b294](https://www.linkedin.com/in/abhay-mishra-38607b294)

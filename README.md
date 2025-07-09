# 🧑‍💼 Job Board API (Django + DRF)

A fully functional RESTful Job Board Backend API built with Django and Django REST Framework (DRF).  
It allows companies to post jobs, and job seekers to browse listings — featuring JWT authentication, filtering, pagination, and more.

---

## 🚀 Features

- ✅ User Registration & Login (JWT Auth)
- ✅ Admin Panel for Superuser
- ✅ Company & Job Models
- ✅ CRUD APIs for Jobs
- ✅ Filtering by Title, Company, etc.
- ✅ Pagination (Limit/Offset)
- ✅ Django Admin for Data Management
- ✅ DRF Browsable API & JSON Response
- ✅ API Schema/Docs with drf-spectacular

---

## 🛠️ Tech Stack

- Python 3.12
- Django 5.x
- Django REST Framework
- SimpleJWT (for token-based auth)
- drf-spectacular (for OpenAPI schema)
- SQLite (default DB for dev)

---

## ⚙️ Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/itsahnafarafat/Job-Board-API-With-Django-DRF.git
   cd Job-Board-API-With-Django-DRF
   ```


2. **Create Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Server:**

   ```bash
   python manage.py runserver
   ```

7. Visit: [http://localhost:8000/admin](http://localhost:8000/admin) to access the admin panel.

---

## 🔐 Authentication (JWT)

* Obtain Token: `POST /api/token/`
* Refresh Token: `POST /api/token/refresh/`

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

Use the access token in headers:

```
Authorization: Bearer <your_access_token>
```

---

## 🔗 API Endpoints

| Method | Endpoint        | Description             |
| ------ | --------------- | ----------------------- |
| GET    | /api/jobs/      | List all jobs           |
| POST   | /api/jobs/      | Create a new job        |
| GET    | /api/jobs/<id>/ | Retrieve a specific job |
| PUT    | /api/jobs/<id>/ | Update a job            |
| DELETE | /api/jobs/<id>/ | Delete a job            |

---

## 📄 API Documentation

Once the server is running, visit:

* Swagger/OpenAPI: [`/api/schema/swagger-ui/`](http://localhost:8000/api/schema/swagger-ui/)
* Redoc: [`/api/schema/redoc/`](http://localhost:8000/api/schema/redoc/)
* Raw OpenAPI JSON: [`/api/schema/`](http://localhost:8000/api/schema/)

---

## 🧪 Testing (Optional)

You can test endpoints using:

* [Postman](https://www.postman.com/)
* `curl`
* DRF’s built-in browsable API

---

## 📁 Project Structure

```
Job-Board-API-With-Django-DRF/
├── jobboard/            # Main project
│   ├── settings.py
│   └── urls.py
├── jobs/                # App for job postings
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── manage.py
└── requirements.txt
```

---

## 👨‍💻 Author

**Ahnaf Arafat**
Junior Python Backend Developer
🔗 [LinkedIn](https://www.linkedin.com/in/ahnaf-arafat-30189a357/) | 🌐 [Github](https://github.com/itsahnafarafat)

---

## 📃 License

This project is licensed under the MIT License.

````



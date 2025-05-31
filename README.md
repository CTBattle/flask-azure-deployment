# Flask Portfolio Project – Simple Blog API

This is a RESTful API built using **Flask** for a basic blogging platform. Users can register, log in, create posts, update them, and view posts from all users. The API uses **JWT authentication** and follows secure coding practices.

---

## 🚀 Features

- User registration and login with password hashing
- JWT token-based authentication
- Create, read, update, and delete posts (CRUD)
- Public and protected routes
- View user profiles and their posts
- SQLite backend (easy to swap with PostgreSQL)
- Ready for deployment with Docker

---

## 🧰 Tech Stack

- Python 3 / Flask
- Flask-JWT-Extended
- SQLAlchemy ORM
- SQLite (default)
- Docker (for deployment)
- Insomnia / curl for testing

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/your-flask-api.git
cd your-flask-api

```
python3 -m venv venv
source venv/bin/activate
```
```
pip install -r requirements.txt
```
```
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-key
```
```
flask --app main.py run --port 8000
```

```
Authorization: Bearer <your_token>
```
```
POST /login → returns access token
```

API Endpoints

Auth
Method	Endpoint	Description	Auth Required
POST	/register	Register new user	No
POST	/login	Login + return token	No
Posts
Method	Endpoint	Description	Auth Required
POST	/posts	Create post	Yes
GET	/posts	List all posts	No
GET	/posts/<id>	Get single post	No
PUT	/posts/<id>	Update post (if owner)	Yes
DELETE	/posts/<id>	Delete post (if owner)	Yes
Users
Method	Endpoint	Description	Auth Required
GET	/me	Get your own profile	Yes
GET	/users/<id>	Get any user profile	No
GET	/users/<id>/posts	Posts by specific user No
Testing the API

You can test endpoints using:

curl
Insomnia
Postman
Make sure to include your JWT token for protected routes.

☁️ Deployment

This project is Docker-ready and can be deployed using platforms like:

Railway
Render
Heroku (with workaround)
✍️ Author

Built by Charles Battle as part of a Nucamp coding portfolio project.

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

## 🧱 Tech Stack

- Python 3 / Flask
- Flask-JWT-Extended
- SQLAlchemy ORM
- SQLite (default)
- Docker (for deployment)
- Insomnia / curl for testing

---

## 📦 Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yourusername/your-flask-api.git
   cd your-flask-api

```
python3 -m venv venv
source venv/bin/activate

```
pip install -r requirements.txt

```
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-key

```
flask --app main.py run --port 5000


🔐 Authentication

Send JWT token in the header:
Authorization: Bearer <your_token>
Obtain token from:
POST /login (returns access token)
📘 API Endpoints

🔑 Auth
Method	Endpoint	Description	Auth
POST	/register	Register new user	❌
POST	/login	Login + return JWT	❌
📄 Posts
Method	Endpoint	Description	Auth
POST	/posts	Create post	✅
GET	/posts	List all posts	❌
GET	/posts/<id>	Get single post	❌
PUT	/posts/<id>	Update post (if owner)	✅
DELETE	/posts/<id>	Delete post (if owner)	✅
👤 Users
Method	Endpoint	Description	Auth
GET	/me	Get your own profile	✅
GET	/users/<id>	Get any user profile	❌
GET	/users/<id>/posts	Posts by specific user	❌
🧪 Testing the API

You can test endpoints using:

curl
Insomnia
Postman
Include your JWT token for protected routes.

☁️ Deployment

This project is Docker-ready and can be deployed using platforms like:

Railway
Render
Heroku (with workaround)
✍️ Author

Built by Charles Battle as part of a Nucamp coding portfolio project.


---

Let me know if you'd like me to:
- Add anything to the README (like ER diagram, Swagger link, etc.)
- Generate a real `requirements.txt`
- Help you upload this to GitHub and push live

Ready for deployment now, or want to do anything else first?

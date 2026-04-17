# FastAPI User Authentication System

## 🚀 Features

* User Registration
* User Login
* Password Hashing
* SQLite Database
* Modular Project Structure

## 🛠️ Tech Stack

* Python
* FastAPI
* SQLite
* Pydantic

## ▶️ How to Run

```bash
uvicorn main:app --reload
```

Open:
http://127.0.0.1:8000/docs

## 📌 API Endpoints

* POST /register → Register user
* POST /login → Login user
* GET /users → View users

## 📂 Project Structure

```
project/
│
├── main.py
├── database.py
├── models.py
└── routes/
    ├── auth.py
    └── user.py
```

## 🔐 Note

Passwords are hashed using SHA256.


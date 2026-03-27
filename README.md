# 🚀 FastAPI Social Media App (Images & Videos Feed)

A full-stack Python project demonstrating a **modern backend + lightweight frontend architecture** using **FastAPI**, **Streamlit**, and **ImageKit**.

This application allows users to:

- 🔐 Register & authenticate securely
- 📤 Upload images/videos with captions
- 📰 View uploaded content as a real-time feed

Built with scalability, async processing, and clean architecture in mind.

---

## 🧠 Tech Stack

### Backend

- **FastAPI** – High-performance async API framework
- **FastAPI Users** – Authentication & user management
- **SQLAlchemy (Async)** – Database ORM
- **SQLite (aiosqlite)** – Lightweight async database
- **ImageKit.io** – Cloud-based media storage & optimization

### Frontend

- **Streamlit** – Fast UI for data apps

### Dev Tools

- **uv** – Fast Python package & environment manager
- **Uvicorn** – ASGI server

---

## ⚙️ Features

### ✅ Authentication

- JWT-based authentication
- User registration & login
- Protected routes

### 📤 Media Upload

- Upload **images & videos**
- Add captions
- Cloud storage via ImageKit
- Automatic file type detection

### 📰 Feed System

- Displays all uploaded posts
- Shows:
  - Caption
  - Media (image/video)
  - Upload timestamp

### 🗑️ Post Management

- Delete posts

---

## 📁 Project Structure

```
fastapi-social-app/
│
├── app/
│   ├── db.py              # Database setup & models
│   ├── schema.py          # Pydantic schemas
│   ├── users.py           # Auth setup (FastAPI Users)
│   ├── images.py          # ImageKit configuration
│
├── main.py                # FastAPI entry point
├── frontend.py            # Streamlit UI
├── README.md
└── pyproject.toml
```

---

## 📦 Dependencies

```toml
[project]
name = "fastapi-social-app"
version = "0.1.0"
requires-python = ">=3.12"

dependencies = [
    "aiosqlite>=0.22.1",
    "dotenv>=0.9.9",
    "fastapi>=0.135.1",
    "fastapi-users[sqlalchemy]>=15.0.4",
    "imagekitio>=5.2.0",
    "python-dotenv>=1.2.2",
    "streamlit>=1.55.0",
    "uvicorn[standard]>=0.42.0",
]
```

---

## 🚀 Getting Started

### 1️⃣ Install `uv`

```bash
pip install uv
```

### 2️⃣ Install Dependencies

```bash
uv sync
```

---

## ▶️ Running the Project

### 🔹 Start Backend (FastAPI)

```bash
uv run main.py
```

API will run on:

```
http://127.0.0.1:8000
```

---

### 🔹 Start Frontend (Streamlit)

```bash
uv run streamlit run frontend.py
```

Frontend will run on:

```
http://localhost:8501
```

---

## 🔐 Environment Variables

Create a `.env` file:

```env
IMAGEKIT_PUBLIC_KEY=your_public_key
IMAGEKIT_PRIVATE_KEY=your_private_key
IMAGEKIT_URL_ENDPOINT=your_url_endpoint
SECRET_KEY=your_secret_key
```

---

## 📸 API Endpoints Overview

| Method | Endpoint         | Description        |
| ------ | ---------------- | ------------------ |
| POST   | `/auth/jwt`      | Login              |
| POST   | `/auth/register` | Register user      |
| POST   | `/upload`        | Upload image/video |
| GET    | `/feed`          | Get all posts      |
| DELETE | `/posts/{id}`    | Delete a post      |

---

## 🧪 Example Workflow

1. Register a new user
2. Login and get JWT token
3. Upload image/video with caption
4. View feed in Streamlit UI
5. Delete posts if needed

---

## 💡 Highlights (For Recruiters)

- ⚡ Built using **async-first architecture (FastAPI + Async DB)**
- ☁️ Integrated **cloud media storage (ImageKit)**
- 🔐 Production-ready **authentication system**
- 📦 Managed dependencies using **modern tool (uv)**
- 🧩 Clean modular structure (scalable & maintainable)
- 🖥️ Full-stack demo with minimal frontend using Streamlit

---

## 🔮 Future Improvements

- Likes & comments system
- Pagination / infinite scroll
- Role-based access control
- Docker deployment
- CI/CD pipeline
- S3 support (alternative to ImageKit)

---

## 👨‍💻 Author

**Muhammad Ahsan**
Senior Software Engineer (Full Stack)

- Python (FastAPI)
- Laravel / Node.js
- AWS & Serverless
- AI Integrations (OpenAI)

---

## ⭐ Final Note

This project demonstrates practical backend engineering skills including:

- API design
- Async programming
- Third-party integrations
- Authentication systems
- Full-stack thinking

---

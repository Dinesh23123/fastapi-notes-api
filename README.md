# 📝 FastAPI Notes App (MongoDB + Templates)

A full-stack Notes application built using **FastAPI**, **MongoDB Atlas**, and **Jinja2 Templates**.
This project allows users to create and view notes with a clean UI and backend API.

---

# 🚀 Features

* ✅ Create notes (title + description)
* 📄 View notes (API + UI)
* 🎨 Frontend using HTML + CSS (Jinja2 templates)
* ⚡ FastAPI backend with modular structure
* 🌐 MongoDB Atlas integration
* 🔐 Secure environment variables using `.env`

---

# 🛠 Tech Stack

| Technology      | Purpose              |
| --------------- | -------------------- |
| FastAPI         | Backend framework    |
| MongoDB Atlas   | Database             |
| PyMongo / Motor | Database connection  |
| Jinja2          | HTML templating      |
| Uvicorn         | ASGI server          |
| Python          | Programming language |

---

# 📂 Project Structure

```id="xtzplk"
FASTAPI-CH/
│
├── config/
│   └── db.py              # MongoDB connection
│
├── models/
│   └── note.py           # Database model
│
├── schemas/
│   └── note.py           # Pydantic schemas
│
├── routes/
│   └── note.py           # API routes
│
├── templates/
│   └── index.html        # Frontend UI
│
├── static/
│   └── style.css         # Styling
│
├── index.py              # Main FastAPI app
├── .env                  # Environment variables (not pushed)
├── .env.example          # Example env file
├── .gitignore
├── requirements.txt
```

---

# ⚙️ Setup Instructions

## 1️⃣ Clone Repository

```bash id="5s2zsa"
git clone https://github.com/Dinesh23123/fastapi-notes-app.git
cd fastapi-notes-app
```

---

## 2️⃣ Create Virtual Environment

```bash id="c34n8s"
python -m venv myenv
```

### Activate:

**Windows**

```bash id="nmp9qb"
myenv\Scripts\activate
```

**Mac/Linux**

```bash id="3s9gfw"
source myenv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash id="1u0mqi"
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a `.env` file:

```env id="33o1ny"
MONGO_URI=your_mongodb_connection_string
```

---

# ▶️ Run the Application

```bash id="wj2z7l"
uvicorn index:app --reload
```

App will run at:
👉 http://127.0.0.1:8000

---

# 🌐 Web Interface

* Home Page 👉 http://127.0.0.1:8000
* Add notes using UI (form in `index.html`)

---

# 📘 API Documentation

* Swagger UI 👉 http://127.0.0.1:8000/docs
* ReDoc 👉 http://127.0.0.1:8000/redoc

---

# 📌 API Endpoints

## ➕ Create Note

**POST** `/notes`

```json id="zj9qnx"
{
  "title": "Sample Note",
  "description": "This is a test note"
}
```

---

## 📄 Get All Notes

**GET** `/notes`

---

# 🔄 Data Flow

1. User submits form (HTML)
2. Request goes to FastAPI route
3. Route calls schema validation
4. Data stored in MongoDB
5. Response sent back to UI

---

# 🔐 Environment Variables

| Variable  | Description                     |
| --------- | ------------------------------- |
| MONGO_URI | MongoDB Atlas connection string |

---

# ⚠️ Best Practices Used

* ✔️ Clean folder structure (MVC-like)
* ✔️ Separation of concerns (routes, schemas, models)
* ✔️ Environment variable security
* ✔️ Modular FastAPI design

---

# 📸 Screenshots (Add Later)

* UI Page (`index.html`)
* Swagger API docs
* MongoDB Atlas data

---

# 🚀 Future Enhancements

* ✏️ Update notes
* ❌ Delete notes
* 🔐 Authentication (JWT)
* 🔍 Search notes
* 📄 Pagination
* 🌐 Deploy on Render

---

# 🤝 Contributing

Contributions are welcome! Feel free to fork and improve.

---

# 📄 License

MIT License

---

# 👨‍💻 Author

Dinesh Sonawane
GitHub: https://github.com/Dinesh23123

---

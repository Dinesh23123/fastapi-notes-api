# 📝 FastAPI Notes App (MongoDB + Templates)

A full-stack Notes application built using **FastAPI**, **MongoDB Atlas**, and **Jinja2 Templates**.
This project allows users to **create, view, update, and delete notes** with a clean UI and backend API.

---

# 🚀 Features

* ✅ Create notes (title + description)
* 📄 View notes (API + UI)
* ✏️ Update existing notes
* ❌ Delete notes
* 🎨 User-friendly frontend using HTML + CSS (Jinja2 templates)
* ⚡ FastAPI backend with modular and scalable structure
* 🌐 MongoDB Atlas cloud database integration
* 🔐 Secure handling of environment variables using `.env`

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

```
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
└── README.md
```

---

# ⚙️ Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Dinesh23123/fastapi-notes-app.git
cd fastapi-notes-app
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv myenv
```

### Activate:

**Windows**

```bash
myenv\Scripts\activate
```

**Mac/Linux**

```bash
source myenv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a `.env` file:

```env
MONGO_URI=your_mongodb_connection_string
```

---

# ▶️ Run the Application

```bash
uvicorn index:app --reload
```

App will run at:
👉 http://127.0.0.1:8000

---

# 🌐 Web Interface

* Home Page 👉 http://127.0.0.1:8000
* Add, update, and delete notes using UI

---

# 📘 API Documentation

* Swagger UI 👉 http://127.0.0.1:8000/docs
* ReDoc 👉 http://127.0.0.1:8000/redoc

---
<!-- 
# 📌 API Endpoints

## ➕ Create Note

POST `/notes`

## 📄 Get All Notes

GET `/notes`

## ✏️ Update Note

PUT `/notes/{id}`

## ❌ Delete Note

DELETE `/notes/{id}`

--- -->

# 🔄 Data Flow

1. User submits form (HTML)
2. Request goes to FastAPI route
3. Route validates data using schemas
4. Data stored in MongoDB
5. Response returned to UI

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

# 🧠 Key Learnings

* Built REST APIs using FastAPI
* Integrated MongoDB with Python backend
* Implemented full CRUD operations
* Used Jinja2 for server-side rendering
* Managed environment variables securely

---
<!-- 
# 📸 Screenshots (Add Later)

* UI Page (`index.html`)
* Notes Listing
* Swagger API docs
* MongoDB Atlas data

--- -->

# 🚀 Future Enhancements

* 🔐 User authentication (JWT-based login & signup)
* 👤 User-specific notes (multi-user support)
* 🔍 Search and filter notes
* 📄 Pagination for better performance
* 🧾 Form validation and error handling
* 🎨 Improved UI/UX with modern design (Bootstrap/Tailwind)
* 🌐 Deploy application on Render or Railway
* 📦 Docker support for containerization
* 📊 Add logging and monitoring

---

# 🤝 Contributing

Contributions are welcome! Feel free to fork and improve.

---

<!-- # 📄 License

MIT License

--- -->

# 👨‍💻 Author

Dinesh Sonawane
GitHub: https://github.com/Dinesh23123

---

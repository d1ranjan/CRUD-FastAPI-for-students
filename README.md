# Student Management CRUD API

A Python backend project for the EWB Edu Tech internship assignment, built with **FastAPI**, **SQLAlchemy**, and **SQLite**. The route files follow the structure in the assignment notebook and keep Create, Read, Update, and Delete operations separate.

## Features

- Create, list, search, retrieve, update, and delete student records.
- SQLite persistence with SQLAlchemy.
- Request validation with Pydantic and email validation.
- Duplicate email protection and clear 404 responses for missing records.
- Search by name or course and paginate with `skip` / `limit`.
- Interactive Swagger documentation at `/docs`.
- Automated tests for CRUD behavior and common error cases.
- Render deployment configuration included.
- Optional Ollama AI is not included because it is not required for the core assignment.

## Project structure

```text
student-crud-fastapi/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── model.py
│   ├── schema.py
│   └── routes/
│       ├── __init__.py
│       ├── base.py
│       ├── create_students.py
│       ├── get_students.py
│       ├── update_students.py
│       └── delete_students.py
├── tests/
├── .env.example
├── .gitignore
├── main.py
├── requirements.txt
├── render.yaml
└── README.md
```

## Requirements

- Python 3.10 or newer
- pip

## Run locally (Windows PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:
- API docs: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health

The default database is `students.db` in the project root. It is created automatically. The database file is ignored by Git.

## API endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/students` | Create a student |
| `GET` | `/students` | List students; optional `name`, `course`, `skip`, `limit` |
| `GET` | `/students/{student_id}` | Retrieve one student |
| `PATCH` | `/students/{student_id}` | Partially update a student |
| `DELETE` | `/students/{student_id}` | Delete a student |
| `GET` | `/health` | Health check |

## Example request

Use Swagger UI or send this JSON to `POST /students`:

```json
{
  "name": "Alex Student",
  "date_of_birth": "2005-04-12",
  "email": "alex@example.com",
  "phone": "9876543210",
  "course": "Computer Science",
  "address": "Kolkata"
}
```

Example filters:
- `GET /students?name=Alex`
- `GET /students?course=Computer%20Science`
- `GET /students?skip=0&limit=20`

Use only dummy student data for demos. Do not add real students' personal information to a public repository.

## Run tests

```powershell
pytest -q
```

## Upload to GitHub

Create an empty repository on GitHub, then from the project directory run:

```powershell
git init
git add .
git commit -m "Build Student Management CRUD API"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/student-crud-fastapi.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

## Deploy to Render

1. Push the project to GitHub.
2. Sign in to Render and create a new Blueprint using the repository.
3. Review the service settings and deploy.
4. Open your deployed URL followed by `/docs`.

**SQLite hosting note:** Render's free web services use an ephemeral filesystem. Data stored in the default SQLite file can be lost when the service restarts or redeploys. For durable hosted data, use a host with a persistent disk and configure `DATABASE_URL` accordingly, or choose a managed database supported by your deployment plan.

## Notes

- The API does not provide authentication; do not expose real student data.
- The optional Ollama extension can be added later. It is intentionally omitted so the mandatory CRUD assignment stays simple and reproducible.

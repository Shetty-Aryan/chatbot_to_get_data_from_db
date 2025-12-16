# 🧠 Chatbot Client Management System

A full-stack application where users interact with a chatbot to retrieve client and address data. The chatbot processes natural language queries, calls backend APIs, and displays results in a React frontend.

## Tech Stack
- **Frontend:** React.js, JavaScript, HTML/CSS
- **Backend:** Python, FastAPI, SQLAlchemy, Pydantic v2
- **Database:** PostgreSQL (Neon)

## APIs
- `GET /clients`: Get all clients.
- `GET /clients/name/{name}`: Get client by name.
- `GET /clients/{id}/addresses`: Get addresses by client ID.
- `GET /clients/name/{name}/addresses`: Get addresses by client name.
- `POST /chat`: Chatbot endpoint that routes user queries.

## How to Run

**Backend:**
```bash
cd backend
pythonenv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

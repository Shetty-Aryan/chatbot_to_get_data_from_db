# Chatbot to Get Data from Database

A full-stack web application that allows users to interact with a chatbot to retrieve client and address information stored in a PostgreSQL database.

The application uses a React frontend, a FastAPI backend, and PostgreSQL (Neon) as the database. It is fully deployed and accessible online.

---

## Tech Stack

Frontend:
- React (JavaScript)
- Deployed on Vercel

Backend:
- FastAPI (Python)
- SQLAlchemy ORM
- Deployed on Render

Database:
- PostgreSQL (Neon – cloud hosted)

---

## Features

- Chatbot interface to query client data
- Fetch all clients via chat
- Search clients by name
- Click on a client row to view full address details
- REST APIs for clients and addresses
- Fully deployed frontend and backend
- CORS enabled for cross-origin communication

---

## API Endpoints

- `POST /chat` – Chatbot query handler  
- `GET /clients` – Get all clients  
- `GET /clients/name/{name}` – Get clients by name  
- `GET /clients/{client_id}/addresses` – Get addresses by client ID  
- `GET /clients/name/{name}/addresses` – Get addresses by client name  

---

## Project Structure

chatbot_to_get_data_from_db/
│
├── backend/
│ ├── main.py
│ ├── models.py
│ ├── schemas.py
│ ├── crud.py
│ ├── database.py
│ └── requirements.txt
│
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ │ ├── ChatBox.jsx
│ │ │ └── DataGrid.jsx
│ │ ├── api.js
│ │ └── App.js
│ └── package.json
│
└── README.md

yaml
Copy code

---

## How the Chatbot Works

Users can type queries such as:
- “Show all clients”
- “Get client named John”
- “Show addresses for client John”

The chatbot processes the message and fetches data from the database using backend APIs, then displays results in a table.

---

## Local Setup (Optional)

Backend:
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
Frontend:

bash
Copy code
cd frontend
npm install
npm start
Deployment
Frontend deployed on Vercel

Backend deployed on Render

Database hosted on Neon PostgreSQL

Frontend communicates with backend using deployed API URLs

No localhost calls in production

Notes
Free tiers are used for all services

Backend may sleep when idle (Render free tier)

Suitable for college projects, demos, and learning purposes


from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import crud, schemas
from schemas import ChatRequest,ChatResponse
from crud import detect_intent
from fastapi.middleware.cors import CORSMiddleware


#to run: uvicorn main:app --reload

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://chatbot-to-get-data-from-gqaasi3ir-shetty-aryans-projects.vercel.app/"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/clients", response_model=list[schemas.ClientOut])
def get_clients(db: Session=Depends(get_db)):
    return crud.get_clients(db)

@app.get("/clients/name/{name}",response_model=list[schemas.ClientOut])
def get_client(name: str, db: Session=Depends(get_db)):
    return crud.get_client_by_name(db,name)

@app.get("/clients/{client_id}/addresses", response_model=list[schemas.AddressOut])
def get_addresses(client_id: str, db: Session = Depends(get_db)):
    return crud.get_addresses_by_client_id(db, client_id)

@app.get("/clients/name/{name}/addresses", response_model=list[schemas.AddressOut])
def get_addresses_by_name(name: str, db: Session = Depends(get_db)):
    return crud.get_addresses_by_client_name(db, name)

@app.post("/chat", response_model=schemas.ChatResponse)
def chat(req: schemas.ChatRequest, db: Session = Depends(get_db)):

    intent = detect_intent(req.message)

    if intent == "GET_CLIENTS":
        clients = crud.get_clients(db)
        data = [schemas.ClientOut.from_orm(c) for c in clients]

    elif intent == "GET_CLIENT_BY_NAME":
        name = req.message.split()[-1]
        clients = crud.get_client_by_name(db, name)
        data = [schemas.ClientOut.from_orm(c) for c in clients]

    elif intent == "GET_ADDRESS_BY_NAME":
        name = req.message.split()[-1]
        addresses = crud.get_addresses_by_client_name(db, name)
        data = [schemas.AddressOut.from_orm(a) for a in addresses]

    elif intent == "GET_ADDRESS_BY_ID":
        client_id = req.message.split()[-1]
        addresses = crud.get_addresses_by_client_id(db, client_id)
        data = [schemas.AddressOut.from_orm(a) for a in addresses]

    else:
        data = {"message": "Sorry, I did not understand your request"}

    return {
        "intent": intent,
        "data": data
    }

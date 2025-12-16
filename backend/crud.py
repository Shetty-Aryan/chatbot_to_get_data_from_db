from sqlalchemy.orm import Session
from models import Client, Address

def get_clients(db: Session):
    return db.query(Client).all()

def get_client_by_name(db: Session, name: str):
    return db.query(Client).filter(Client.first_name.ilike(f"%{name}%")).all()

def get_addresses_by_client_id(db: Session, client_id):
    return db.query(Address).filter(Address.party_id==client_id).all()

def get_addresses_by_client_name(db: Session, name: str):
    return (
        db.query(Address)
        .join(Client, Address.party_id == Client.pty_id)
        .filter(Client.first_name.ilike(f"%{name}%"))
        .all()
    )

def detect_intent(message: str):
    msg = message.lower()

    # 1. List all clients
    if ("list" in msg or "all" in msg) and "client" in msg:
        return "GET_CLIENTS"

    # 2. Get address by client name
    if "address" in msg and "name" in msg:
        return "GET_ADDRESS_BY_NAME"

    # 3. Get address by client id
    if "address" in msg and "id" in msg:
        return "GET_ADDRESS_BY_ID"

    # 4. Get client by name
    if "client" in msg and "name" in msg:
        return "GET_CLIENT_BY_NAME"

    return "UNKNOWN"
from sqlalchemy.orm import Session
from models import Client, Address


# ---------------------------
# DATABASE QUERIES
# ---------------------------

def get_clients(db: Session):
    return db.query(Client).all()


def get_client_by_name(db: Session, name: str):
    return (
        db.query(Client)
        .filter(Client.first_name.ilike(f"%{name}%"))
        .all()
    )


def get_addresses_by_client_id(db: Session, client_id):
    return (
        db.query(Address)
        .filter(Address.party_id == client_id)
        .all()
    )


def get_addresses_by_client_name(db: Session, name: str):
    return (
        db.query(Address)
        .join(Client, Address.party_id == Client.pty_id)
        .filter(Client.first_name.ilike(f"%{name}%"))
        .all()
    )


# ---------------------------
# NLP / INTENT HELPERS
# ---------------------------

def extract_name(message: str):
    """
    Extracts client name from natural language queries.
    Supports:
    - get client john
    - get address of john
    - get address of client john
    """
    words = message.lower().strip().split()

    # Case: "client john"
    if "client" in words:
        idx = words.index("client")
        if idx + 1 < len(words):
            return words[idx + 1]

    # Case: "address of john"
    if "of" in words:
        idx = words.index("of")
        if idx + 1 < len(words):
            return words[idx + 1]

    return None


def detect_intent(message: str):
    msg = message.lower()
    

    # ADDRESS intent (check first)
    if "address" in msg or "addresses" in msg:
        if "id" in msg:
            return "GET_ADDRESS_BY_ID"
        return "GET_ADDRESS_BY_NAME"

    # CLIENT intent
    if "client" in msg or "clients" in msg:
        if "list" in msg or "all" in msg or "show" in msg:
            return "GET_CLIENTS"
        return "GET_CLIENT_BY_NAME"

    return "UNKNOWN"

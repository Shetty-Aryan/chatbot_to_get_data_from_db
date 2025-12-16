from pydantic import BaseModel, ConfigDict
from uuid import UUID
from typing import Any

#pydantic - used to validate the data receieved ,i.e, to see that it matches the expected types
#typing-  used for type hints.
#orm_mode- allows pydantic to read data directly from ORM objects
class ClientOut(BaseModel):
    pty_id: UUID
    first_name: str
    last_name: str
    phone: str

    model_config = ConfigDict(from_attributes=True)


class AddressOut(BaseModel):
    line1: str
    city: str
    zip: str

    model_config = ConfigDict(from_attributes=True)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    intent: str
    data: object

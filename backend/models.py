from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database import Base

class Client(Base):
    __tablename__="client"
    pty_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name=Column(String)
    last_name=Column(String)
    phone=Column(String)

class State(Base):
    __tablename__="state"
    stt_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name=Column(String)
    pincode=Column(String)

class Address(Base):
    __tablename__ = "address"
    add_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    line1 = Column(String)
    line2 = Column(String)
    city = Column(String)
    zip = Column(String)
    state_id = Column(UUID, ForeignKey("state.stt_id"))
    party_id = Column(UUID, ForeignKey("client.pty_id"))
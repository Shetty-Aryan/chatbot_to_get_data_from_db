from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os
from dotenv import load_dotenv

#fastAPI- to create RESTful APIs
#uvicorn- Runs FastAPI apps to serve requests
#sqlalchemy-Allows you to write Python code instead of raw SQL to interact with databases.
#

load_dotenv()
DATABASE_URI=os.getenv("POSTGRES_URI")

engine = create_engine(
    DATABASE_URI,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10
)

#connects python to database

SessionLocal=sessionmaker(bind=engine)#used to create session object

Base=declarative_base()#used to create a base class (tables as python classes)
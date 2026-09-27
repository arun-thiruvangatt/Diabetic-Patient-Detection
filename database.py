from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.engine import URL

url = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password="qwe123@456",
    host="127.0.0.1",
    port=5432,
    database="factory",
)

engine = create_engine(url, echo=True)

Base = declarative_base()

Session = sessionmaker()
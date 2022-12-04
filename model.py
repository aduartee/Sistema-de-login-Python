from sqlalchemy import create_engine, Column, Integer, String, text, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from hashlib import sha256

# Fornece os dados para realizar a conexão com o banco de dados
USUARIO = "root"
PASSWORD = ""
HOST = "localhost"
BANCO = "login"
PORT = "3306"

CON = f"mysql+pymysql://{USUARIO}:{PASSWORD}@{HOST}:{PORT}/{BANCO}"
engine = create_engine(CON, echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Pessoa(Base):
    __tablename__ = "Pessoa"
    id = Column(Integer, primary_key=True)
    nome = Column(String(40))
    email = Column(String(40))
    senha = Column(String(40))

Base.metadata.create_all(engine)

import hashlib

from model import Pessoa
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from hashlib import sha256

def Conec():
    USUARIO = "root"
    PASSWORD = ""
    HOST = "localhost"
    BANCO = "login"
    PORT = "3306"

    CON = f"mysql+pymysql://{USUARIO}:{PASSWORD}@{HOST}:{PORT}/{BANCO}"
    engine = create_engine(CON, echo=False)
    Session = sessionmaker(bind=engine)
    return Session()


class Cadastro():
    @classmethod
    def verifica_dados(cls, nome, email, senha):
        if len(nome) > 40 or len(nome) < 3 :
            return 2

        if len(email) > 200:
            return 3

        if len(senha) > 40 or len(senha) < 3:
            return 4

        return 1

    @classmethod
    def cadastrar(cls, nome, email, senha):
        session = Conec()
        usuario = session.query(Pessoa).fiter(Pessoa.email == email).all()

        if len(usuario) > 0
            return 5

        dados_verificados = cls.verifica_dados(nome, email, senha)

        if dados_verificados != 1:
            return dados_verificados()

        try:
            senha = hashlib.sha256()

        except:
            pass









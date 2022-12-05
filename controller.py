from model import Pessoa
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import hashlib

def Conec():
    USUARIO = "root"
    PASSWORD = ""
    HOST = "localhost"
    BANCO = "login"
    PORT = "3306"

    CON = f'mysql+pymysql://{USUARIO}:{PASSWORD}@{HOST}:{PORT}/{BANCO}'
    engine = create_engine(CON, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()


class Cadastro():
    @classmethod
    def verifica_dados(cls, nome, email, senha):
        if len(nome) > 40 or len(nome) < 3:
            return 2

        if len(email) > 200:
            return 3

        if len(senha) > 40 or len(senha) < 3:
            return 4

        return 1

    @classmethod
    def cadastrar(cls, nome, email, senha):
        Session = Conec()
        usuario = Session.query(Pessoa).filter(Pessoa.email == email).all()

        if len(usuario) > 0:
            return 5

        dados_verificados = cls.verifica_dados(nome, email, senha)

        if dados_verificados != 1:
            return dados_verificados()

        try:
            senha = hashlib.sha256(senha.encode()).hexdigest()
            p1 = Pessoa(
                nome=nome,
                email=email,
                senha=senha
            )
            session.add(p1)
            session.commit(p1)
            return 1

        except:
            return 3


class Controller_login:
    @classmethod
    def Login(cls, email, senha):
        session = Conec()
        senha = hashlib.sha256(senha.encode()).hexdigest()
        logado = session.query(Pessoa).filter(Pessoa.email == email).filter(Pessoa.senha == senha).all()

        if len(logado) == 1:
            return {'logado': True, 'id': logado[0].id}

        else:
            return False

print(Cadastro.cadastrar('Arthur', 'email', 'senha'))


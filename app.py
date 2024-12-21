from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração do banco SQLite
DATABASE_URL = "sqlite:///academia.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Definição da tabela Alunos
class Aluno(Base):
    __tablename__ = 'alunos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_completo = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    nome_responsavel = Column(String, nullable=True)
    telefone = Column(String, nullable=False)
    menor_de_idade = Column(Boolean, default=False)

# Criar a tabela
Base.metadata.create_all(engine)

# Criar uma sessão para interagir com o banco
SessionLocal = sessionmaker(bind=engine)

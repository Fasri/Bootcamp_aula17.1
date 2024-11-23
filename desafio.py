from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

Base = declarative_base()

class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(20))
    email = Column(String(50))
    endereco = Column(String(100))

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(200))
    preco = Column(Integer)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))
    
    # Estabelece a relação entre Produto e Fornecedor
    fornecedor = relationship("Fornecedor")

engine = create_engine('sqlite:///desafio.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Inserindo fornecedores
try:
    with Session() as session:
        fornecedores = [
            Fornecedor(nome='Fornecedor A', telefone='(11) 1234-5678', email='fornecedora@exemplo.com', endereco='Rua A, 123'),
            Fornecedor(nome='Fornecedor B', telefone='(21) 9876-5432', email='fornecedorb@exemplo.com', endereco='Rua B, 456'),
            Fornecedor(nome='Fornecedor C', telefone='(31) 5555-5555', email='fornecedorc@exemplo.com', endereco='Rua C, 789'),
        ]

        session.add_all(fornecedores)
        session.commit()
except SQLAlchemyError as e:
    print("Erro ao inserir fornecedores:", e)   

# Inserindo produtos
try:
    with Session() as session:
        produtos = [
            Produto(nome='Produto A', descricao='Descrição do Produto A', preco=10, fornecedor=fornecedores[0]),
            Produto(nome='Produto B', descricao='Descrição do Produto B', preco=20, fornecedor=fornecedores[1]),
            Produto(nome='Produto C', descricao='Descrição do Produto C', preco=30, fornecedor=fornecedores[2]),
        ]

        session.add_all(produtos)
        session.commit()
except SQLAlchemyError as e:
    print("Erro ao inserir produtos:", e)
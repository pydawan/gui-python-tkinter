# -*- coding: utf-8 -*-
"""Exemplo de CRUD com Python, SQLAlchemy e SQLite3"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Para debug utilizar ``echo=True``:
# engine = create_engine('sqlite:///db.sqlite3', echo=True)

if __name__ == '__main__':
    engine = create_engine('sqlite:///db.sqlite3')
else:
    engine = create_engine('sqlite:///database/db.sqlite3')

# Criar banco na memória
# engine = create_engine('sqlite://')

# Criando uma classe "Session" já configurada.
# Session é instanciado posteriormente para interação com a tabela.
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Users(Base):
    """Classe representa uma tabela do banco."""
    # ``__tablename__`` - Define o nome da tabela.
    # Se o nome da tabela não for definido é utilizado o nome da classe.
    __tablename__ = 'users'

    # Colunas da tabela.
    user_id = Column(name='user_id', type_=Integer, autoincrement='auto', primary_key=True)
    name = Column(name='Name', type_=String(128))
    age = Column(name='Age', type_=Integer)
    gender = Column(name='Gender', type_=String(16))


if __name__ == "__main__":
    # Removendo todas as tabelas do banco.
    # Base.metadata.drop_all(engine)

    # Criando todas as tabelas.
    Base.metadata.create_all(engine)

    # Criando uma sessão (add, commit, query, etc).
    session = Session()

    # Criando os dados que serão inseridos na tabela.
    user = Users()
    user.name = 'Renato'
    user.age = 35
    user.gender = 'Masculino'
    # Inserindo registro na tabela.
    # session.add(user)

    # Persistindo os dados.
    # session.commit()

    # Consultar todos os registros.
    records = session.query(Users).all()
    for row in records:
        print(f'ID: {row.user_id} - Nome: {row.name} - Idade: {row.age} - Sexo: {row.gender}')
    print('---\n')

    # Consulta com filtro.
    records = session.query(Users).filter(Users.name.ilike('%re%')).all()
    for row in records:
        print(f'ID: {row.user_id} - Nome: {row.name} - Idade: {row.age} - Sexo: {row.gender}\n')
    print('---\n')

    # Alterar registro.
    print('ANTES da alteração:')
    record = session.query(Users).filter(Users.user_id == 1).first()
    print(f'ID: {record.user_id} - Nome: {record.name} - Idade: {record.age} - Sexo: {record.gender}')

    new_data = {'name': 'Rafaela', 'age': 50, 'gender': 'Feminino'}
    session.query(Users).filter(Users.user_id == 1).update(new_data)
    session.commit()

    print('DEPOIS da alteração:')
    record = session.query(Users).filter(Users.user_id == 1).first()
    print(f'ID: {record.user_id} - Nome: {record.name} - Idade: {record.age} - Sexo: {record.gender}')
    print('---\n')

    # Remover um registro da tabela.
    print('ANTES da remoção:')
    record = session.query(Users).filter(Users.user_id == 2).first()
    print(f'ID: {record.user_id} - Nome: {record.name} - Idade: {record.age} - Sexo: {record.gender}')

    session.query(Users).filter(Users.user_id == 1).delete()
    session.commit()

    print('DEPOIS da remoção:')
    record = session.query(Users).filter(Users.user_id == 1).first()
    print(record)
    print('---\n')

    # Fechando a sessão.
    session.close()

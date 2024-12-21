from flask import Flask, request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app import Aluno

app = Flask(__name__)

# Configuração do banco de dados

DATABASE_URL = DATABASE_URL = "postgresql://academia_4nhn_user:<senha>@dpg-ctj1ro52ng1s73bg4d10-a:5432/academia_4nhn"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Rotas da API
@app.route('/alunos', methods=['GET'])
def listar_alunos():
    session = SessionLocal()
    alunos = session.query(Aluno).all()
    session.close()
    return jsonify([{
        'id': aluno.id,
        'nome_completo': aluno.nome_completo,
        'endereco': aluno.endereco,
        'nome_responsavel': aluno.nome_responsavel,
        'telefone': aluno.telefone,
        'menor_de_idade': aluno.menor_de_idade
    } for aluno in alunos])

@app.route('/alunos', methods=['POST'])
def cadastrar_aluno():
    data = request.json
    session = SessionLocal()
    novo_aluno = Aluno(
        nome_completo=data['nome_completo'],
        endereco=data['endereco'],
        nome_responsavel=data.get('nome_responsavel'),
        telefone=data['telefone'],
        menor_de_idade=data['menor_de_idade']
    )
    session.add(novo_aluno)
    session.commit()
    session.close()
    return jsonify({'message': 'Aluno cadastrado com sucesso!'}), 201

@app.route('/alunos/<int:aluno_id>', methods=['PUT'])
def atualizar_aluno(aluno_id):
    data = request.json
    session = SessionLocal()
    aluno = session.query(Aluno).filter(Aluno.id == aluno_id).first()
    if not aluno:
        return jsonify({'message': 'Aluno não encontrado!'}), 404
    aluno.nome_completo = data['nome_completo']
    aluno.endereco = data['endereco']
    aluno.nome_responsavel = data.get('nome_responsavel')
    aluno.telefone = data['telefone']
    aluno.menor_de_idade = data['menor_de_idade']
    session.commit()
    session.close()
    return jsonify({'message': 'Aluno atualizado com sucesso!'})

@app.route('/alunos/<int:aluno_id>', methods=['DELETE'])
def excluir_aluno(aluno_id):
    session = SessionLocal()
    aluno = session.query(Aluno).filter(Aluno.id == aluno_id).first()
    if not aluno:
        return jsonify({'message': 'Aluno não encontrado!'}), 404
    session.delete(aluno)
    session.commit()
    session.close()
    return jsonify({'message': 'Aluno excluído com sucesso!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

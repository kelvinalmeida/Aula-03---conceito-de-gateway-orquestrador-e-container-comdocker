from flask import Flask, jsonify

app = Flask(__name__)

# Simulação de Banco de Dados de Usuários
USUARIOS = {
    "user1": {"nome": "João Silva", "status": "ativo"},
    "user2": {"nome": "Maria Souza", "status": "inativo"}, # Não pagou
    "user3": {"nome": "Pedro Santos", "status": "ativo"}
}

@app.route('/status/<id_usuario>')
def verificar_status(id_usuario):
    # Busca o usuário no dicionário; se não achar, retorna status 'desconhecido'
    usuario = USUARIOS.get(id_usuario, {"status": "desconhecido"})
    
    return jsonify({
        "id": id_usuario,
        "status": usuario['status']
    })

if __name__ == "__main__":
    # Importante: Rodar na porta 5001
    app.run(port=5001, host='0.0.0.0')
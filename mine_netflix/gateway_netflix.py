# gateway_netflix.py (Roda na porta 5000)
import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Bem-vindo ao Gateway da Netflix!"

@app.route('/assistir/<id_filme>/<id_usuario>')
def assistir_filme(id_filme, id_usuario):
    # return "Assistindo filme..."
    # 1. O Gateway pergunta ao Serviço de Assinaturas (Porta 5001) se o usuário pagou
    # O aluno acessa a 5000, mas internamente o Gateway chama a 5001
    # usa o nome do serviço definido no docker
    resposta_conta = requests.get(f'http://cont_servico_assinatura:5001/status/{id_usuario}').json()
    
    if resposta_conta['status'] != 'ativo':
        return jsonify({"erro": "Por favor, renove sua assinatura para assistir."}), 403

    # 2. Se pagou, o Gateway busca o link do vídeo no Serviço de Catálogo (Porta 5002)
    resposta_filme = requests.get(f'http://cont_servico_catalogo:5002/filme/{id_filme}').json()
    
    # 3. Entrega tudo pronto para o usuário
    return jsonify({
        "mensagem": f"Reproduzindo: {resposta_filme['titulo']}",
        "link_video": resposta_filme['url'],
        "qualidade": "4K"
    })

if __name__ == "__main__":
    app.run(port=5000)
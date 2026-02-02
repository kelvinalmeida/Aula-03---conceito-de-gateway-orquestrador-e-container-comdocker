from flask import Flask, jsonify

app = Flask(__name__)

# Simulação de Banco de Dados de Filmes
FILMES = {
    "filme1": {
        "titulo": "A Origem (Inception)", 
        "url": "http://video-server/inception.mp4", 
        "categoria": "Sci-Fi"
    },
    "filme2": {
        "titulo": "O Poderoso Chefão", 
        "url": "http://video-server/godfather.mp4", 
        "categoria": "Drama"
    }
}

@app.route('/filme/<id_filme>')
def detalhes_filme(id_filme):
    filme = FILMES.get(id_filme)
    
    if filme:
        return jsonify(filme)
    else:
        return jsonify({"erro": "Filme não encontrado"}), 404

if __name__ == "__main__":
    # Importante: Rodar na porta 5002
    app.run(port=5002)
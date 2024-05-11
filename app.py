from flask import Flask, request
from caoa import PedidoAI

app = Flask(__name__)

@app.route('/integracao-ia', methods=['POST'])
def index():

    body_json = request.json
    pedido = PedidoAI(body_json['url'], 
             body_json['comentCNPJ'], 
             body_json['comentOC'], 
             body_json['comentEndEnt'], 
             body_json['comentItemPC'], 
             body_json['comentCodigo'], 
             body_json['comentQuant'], 
             body_json['comentPreco'], 
             body_json['comentDesc'])
    return pedido

if __name__ == '__main__':
    app.run(host='SEU_IP_LOCAL', port='8080', debug=True)
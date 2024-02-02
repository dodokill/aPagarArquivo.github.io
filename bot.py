import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 


@app.route('/api/exemplo', methods=['GET'])
def exemplo():
      
    user = request.args.get('DE')
    caminho = "C:/Users/2/Desktop/pasta de remoção/" + user + "/abc/mfa.txt"
    try:
        os.remove(caminho)
        resultado = {
                     'text': "O seu QRCODE Foi resetado com sucesso!",
                     'icon':"success",
                     'title': "QRCODE RESETADO"}
    except OSError as e:
       resultado = {
                     'text': "Usuario não encontrado!",
                     'icon':"error",
                     'title': "QRCODE Não resetado"}

    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)

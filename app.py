from flask import Flask, jsonify, request,send_file
from video import downloadVideo
app = Flask(__name__)
import os
@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Bienvenido a mi API REST!'})

@app.route('/download', methods=['GET'])
def descargar_video():
    #param1 = request.args.get('param1')
    # aquí iría la lógica para obtener los productos de alguna fuente de datos

    url_video =  downloadVideo()

    return send_file(url_video)


if __name__ == '__main__':
    app.run(debug=True)
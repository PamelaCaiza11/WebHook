from flask import Flask, request
from flask_cors import CORS  # Para habilitar CORS

app = Flask(__name__)
CORS(app)  # Habilitar CORS para permitir solicitudes desde otros orígenes

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Extraer datos enviados en el cuerpo de la solicitud
    if not data:
        return "No se enviaron datos", 400  # Devuelve un mensaje de error simple
    print(f"Datos recibidos: {data}")
    return "Hola Mundo", 200  # Devuelve solo el mensaje como texto plano

if __name__ == '__main__':
    app.run(debug=True, port=5000)

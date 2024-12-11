from flask import Flask, jsonify
import requests

app = Flask(__name__)

# URL del servicio de saludo
GREETING_SERVICE_URL = "http://localhost:5000/greet"

@app.route('/user', methods=['GET'])
def get_user():
    username = "Santiago Zurita"  # Simulando que obtenemos el nombre de un usuario
    # Llamada al servicio de saludo
    response = requests.get(GREETING_SERVICE_URL, params={'name': username})
    greeting = response.json().get('message')
    return jsonify({'user': username, 'greeting': greeting})

if __name__ == '__main__':
    app.run(debug=True, port=5001)

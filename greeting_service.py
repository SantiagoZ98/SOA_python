from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Mundo')  # 'Mundo' es el valor predeterminado
    return jsonify({'message': f'Hola, {name}!'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

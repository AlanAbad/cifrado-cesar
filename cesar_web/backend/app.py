from flask import Flask, request, jsonify, send_from_directory
import mysql.connector

app = Flask(__name__, static_folder='../frontend', static_url_path='')

# Configura tu conexión
db_config = {
    'host': 'localhost',
    'user': 'root, localhost',
    'password': '130804',
    'database': 'cesar_db'
}

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    data = request.json
    original = data.get('original')
    cifrado = data.get('cifrado')
    conn = mysql.connector.connect(**db_config)
    cur = conn.cursor()
    cur.execute('INSERT INTO mensajes (original, cifrado) VALUES (%s, %s)', (original, cifrado))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/mensajes', methods=['GET'])
def obtener_mensajes():
    conn = mysql.connector.connect(**db_config)
    cur = conn.cursor(dictionary=True)
    cur.execute('SELECT * FROM mensajes')
    resultados = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(resultados)

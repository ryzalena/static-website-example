from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Путь к директории с файлами
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    # Отдаем index.html
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/health')
def health():
    # Health check endpoint
    return 'OK', 200

if __name__ == '__main__':
    print(f"Starting server on port 8181")
    print(f"Serving files from: {BASE_DIR}")
    app.run(host='0.0.0.0', port=8181, debug=False)

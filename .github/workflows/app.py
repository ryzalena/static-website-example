from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <body style="background:blue;color:white;text-align:center;padding:50px">
    <h1>GitHub Actions CD Pipeline</h1>
    <p>Student: Ryzhova</p>
    <p>Lab 2: DevOps</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8181)

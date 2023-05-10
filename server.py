import subprocess
import socket
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def stress_cpu():
    subprocess.Popen(['python3', 'stress_cpu.py'])
    return 'Stressing CPU'

@app.route('/', methods=['GET'])
def get_ip():
    return socket.gethostname()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)


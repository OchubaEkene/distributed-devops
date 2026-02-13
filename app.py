from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return f"CI/CD LIVE: {socket.gethostname()}"

app.run(host='0.0.0.0', port=3000)

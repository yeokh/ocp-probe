from flask import Flask
import os
import socket


app = Flask(__name__)

@app.route("/")
def hello():

    html = "<h3>Version: {version} </h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(version=os.getenv("VERSION", "0.0"), hostname=socket.gethostname())

@app.route("/version")
def version():
    return os.getenv("VERSION", "0.0")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

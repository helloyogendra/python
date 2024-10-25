import os
import socket
import module
from flask import Flask

app = Flask(__name__)

name = os.getenv("NAME", "World")
hostname = socket.gethostname()

error_message = '<h1 style="color: red;">DB Connection Not Available!!</h1>'

@app.route("/")
def home():
    html = f"<h3> Hello {name} :: </h3> <b> Hostname: </b> {hostname} <br>"
    return html


@app.route('/database')
def database():
    if module.checkDBConnection():
        return f'<h1 style="color: green;">DB Connection Available</h1><br><h2 style="color: blue;">Refer below DB Names:</h2><br><h3> {module.showDatabases()} </h3>'
    else:
        return error_message
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)

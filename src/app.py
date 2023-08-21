from flask import Flask, jsonify, render_template
import socket as sc

app = Flask(__name__)


def fetch_details():
    host_name = sc.gethostname()
    host_ip = sc.gethostbyname(host_name)
    print("Hostname : ", host_name)
    print("IP : ", host_ip)
    return str(host_name), str(host_ip)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )


@app.route("/details")
def details():
    host_name, host_ip = fetch_details()
    return render_template('index.html', HOSTNAME=host_name, IP=host_ip)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

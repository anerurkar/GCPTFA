from flask import Flask
app = Flask(__name__)
import platform



@app.route('/')
def hello():
    return "welcome to custom network of gcp!"

@app.route('/healthcheck')
def healthcheck():
    return "application is healthy"

@app.route('/main')
def main():
    hostname=platform.node()
    print("request is handled by host name {0} ".format(hostname))
    return "Request served by instance {0} ".format(hostname)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port='3000')
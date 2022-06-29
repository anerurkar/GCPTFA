from flask import Flask
app = Flask(__name__)
import platform



@app.route('/')
def hello():
    return "welcome to video service !"

@app.route('/healthcheck')
def healthcheck():
    return "video service application is healthy"

@app.route('/main')
def main():
    hostname=platform.node()
    print("request is handled by host name {0} ".format(hostname))
    return "Request served by instance {0} ".format(hostname)

@app.route('/video')
def video():
    hostname=platform.node()
    print("video request is served by  {0}".format(hostname))
    return "video request is served by  {0}".format(hostname)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port='3000')
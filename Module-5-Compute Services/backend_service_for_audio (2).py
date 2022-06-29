from flask import Flask
app = Flask(__name__)
import platform



@app.route('/')
def hello():
    return "welcome to audio service !"

@app.route('/healthcheck')
def healthcheck():
    return "audio service application is healthy"


@app.route('/audio')
def audio():
    hostname=platform.node()
    print("audio request is served by  {0}".format(hostname))
    return "audio request is served by  {0} ".format(hostname)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port='3000')
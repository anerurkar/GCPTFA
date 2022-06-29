from flask import Flask
app = Flask(__name__)
import platform
import os
port_env=int(os.getenv('PORT',6000))
@app.route('/welcome')
def welcome():
    hostname=platform.node()
    return "welcome to Cloudrun.Request served by cloud run instance {0}".format(hostname)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=port_env)
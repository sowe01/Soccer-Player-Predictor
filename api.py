from flask import Flask, request
import query_sql as q
import json


app = Flask(__name__)

@app.route("/")
def hello():
    hello = "<h1>Bienvenido a Soccer Player Predictor</h1>"
    return hello


@app.route('/tujugador/<name>')
def seeYourPlayer(name):
    info = q.getDataUser(name)
    return json.dumps(info)

@app.route('/df')
def devuelvedf():
    info = q.getdataframe()
    return json.dumps(info)

@app.route('/predict/<name>')
def seepredict(name):
    info = q.getpredict(name)
    return json.dumps(info)

@app.route('/maxevol')
def maximo():
    info = q.getmaxevol()
    return json.dumps(info)

@app.route('/minevol')
def minimo():
    info = q.getminevol()
    return json.dumps(info)


if __name__ == '__main__':
    app.run("0.0.0.0", 5000, debug=True)
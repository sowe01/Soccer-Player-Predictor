from flask import Flask



app = Flask(__name__)

@app.route("/")
def hello():
    hello = "Bienvenido a la API de Análisis de Sentimientos. Juega con FRIENDS y descubre su personalidad"
    return hello


app.run("0.0.0.0", 5000, debug=True)
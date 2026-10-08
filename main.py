from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder="Templates")


@app.route("/")
def inicio():
    return render_template("dashboard.html")


@app.route("/logo")
def logo():
    caminho = os.path.join(app.root_path, "Uploads")
    return send_from_directory(caminho, "logo.png")


@app.route("/dinheiro")
def dinheiro():
    caminho = os.path.join(app.root_path, "Uploads")
    return send_from_directory(caminho, "dinheiro.png")


@app.route("/check")
def check():
    caminho = os.path.join(app.root_path, "Uploads")
    return send_from_directory(caminho, "check.png")


@app.route("/quadrado")
def quadrado():
    caminho = os.path.join(app.root_path, "Uploads")
    return send_from_directory(caminho, "quadrado.png")


@app.route("/calculadora")
def calculadora():
    caminho = os.path.join(app.root_path, "Uploads")
    return send_from_directory(caminho, "calculadora.png")


@app.route("/escudo")
def escudo():
    caminho = os.path.join(app.root_path, "Uploads")
    return send_from_directory(caminho, "escudo.png")


@app.route("/predio")
def predio():
    caminho = os.path.join(app.root_path, "Uploads")
    return send_from_directory(caminho, "predio.png")


@app.route("/sair")
def sair():
    caminho = os.path.join(app.root_path, "Uploads")
    return send_from_directory(caminho, "sair.png")


if __name__ == "__main__":
    app.run(debug=True)
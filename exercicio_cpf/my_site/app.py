from flask import Flask, render_template, request, redirect, url_for
from validate_docbr import CPF, CNPJ

app = Flask(__name__)
cpf = CPF()
cnpj = CNPJ()

@app.route("/gerar/<tipo>")
def gerar(tipo):
    cod = ''
    if tipo == "cpf":
        cod = cpf.generate()
    if tipo == "cnpj":
        cod = cnpj.generate()

    return render_template("gerar.html", tipo = tipo, cod = cod)

@app.route("/validar/<tipo>")
def validar(tipo):
    return render_template("gerar.html", tipo = tipo)

@app.route("/resultado/<tipo>", method="POST")
def resultado(tipo):
    cod = ''
    validador = "Invalido"
    if tipo == cpf:
        cod = request.form["cpf"]
        if cpf.validate(cod):
            validador = "Válido"
    if tipo == cnpj:
        cod = request.form["cnpj"]
        if cnpj.validate(cod):
            validador = "Válido"
    
    return render_template("resultado.html", tipo = tipo, cod = cod, validador = validador )




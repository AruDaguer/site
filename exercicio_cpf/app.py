from flask import Flask, render_template, request, redirect, url_for
from validate_docbr import CPF, CNPJ

app = Flask(__name__)
cpf = CPF()
cnpj = CNPJ()

@app.route("/gerar/<tipo>")
def gerar(tipo):
    cod = ''
    if tipo == "cpf":
        cod = cpf.generate(True)
    if tipo == "cnpj":
        cod = cnpj.generate(True)

    return render_template("gerar.html", tipo = tipo.upper(), cod = cod)

@app.route("/validar/<tipo>")
def validar(tipo):
    return render_template("validar.html", tipo = tipo.upper())

@app.route("/resultado/<tipo>", methods=['POST'])
def resultado(tipo):
    cod = ''
    validador = "Invalido"
    if tipo == "CPF":
        cod = request.form["CPF"]
        if cpf.validate(cod):
            validador = "Válido"
    if tipo == "CNPJ":
        cod = request.form["CNPJ"]
        if cnpj.validate(cod):
            validador = "Válido"
    
    return render_template("resultado.html", tipo = tipo.upper(), cod = cod, validador = validador )




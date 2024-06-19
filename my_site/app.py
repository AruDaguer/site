from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

lista_produtos = [
        {"nome": "Coca-Cola", "descricao": "Bom", "preco": 5.00, "imagem": "https://api.freelogodesign.org/assets/blog/thumb/f4dae7732213491da3952f853c48f6dc_1176x840.jpg"},
        {"nome": "Doritos", "descricao": "Suja Mão", "preco": 7.50, "imagem": "https://1.bp.blogspot.com/-berlgYpJS50/Wvr5Q44W7bI/AAAAAAABqnA/p0J4dlS5urgIEUl0AdW_fz50B7hRBduTQCLcBGAs/s1600/doritos%2B2.jpg"},
        {"nome": "Chocolate", "descricao": "Bom", "preco": 4.75, "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRUD5sBMqGcsSFV-RFdy8KxLsscLWdEWStXA&s"}
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=lista_produtos)


@app.route("/produtos/<nome>")
def produto(nome):
    for produto in lista_produtos:
        if produto["nome"] == nome:
            return render_template("produto.html", produto=produto)
        
    return "Erro: Produto não encontrado"
    
#GET
@app.route("/produtos/cadastrar")
def cadastro_produto():
    return render_template("cadastro-produto.html")

@app.route("/produtos", methods=['POST'])
def salvar_produto():
    nome = request.form['nome']
    descricao = request.form['descricao']
    preco = request.form['preco']
    imagem = request.form['imagem']

    produto = {"nome": nome, "descricao": descricao, "preco" : preco, "imagem": imagem }
    lista_produtos.append(produto)

    return redirect( url_for("produtos"))


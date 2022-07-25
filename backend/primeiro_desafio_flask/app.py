from crypt import methods
import re
from flask import Flask, redirect, render_template, request, redirect, flash, url_for
import mysql.connector

app = Flask(__name__)
app.secret_key = 'secret_key12345'


cnx = mysql.connector.connect(user='root', password='my-teste123',
                              host='localhost',
                              database='PRODUTOS', port=7070)


class Produto:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria



lista_categoria = []

@app.route('/')
def index():
    return render_template('index.html', titulo="Escolha a ação!")


@app.route('/criar', methods=['POST','GET'])
def criar():
    if request.method == 'POST':
        nome = request.form['nome']
        categoria = request.form['options']
        
        if nome != "" and categoria != "" and request.form.get('options') in ['enlatados', 'limpeza', 'comida', 'usaveis']:
            nome = nome.title().strip()
            
            
            
            produto = Produto(nome, categoria)
            
            mycursor = cnx.cursor()
                
            sql = "INSERT INTO produtos (produto_nome, produto_categoria) VALUES (%s, %s)"
            val = (produto.nome, produto.categoria)

            mycursor.execute(sql, val)
                
            cnx.commit()
            mycursor.close()
            
            flash('Produto Cadastrado com sucesso!')
            return redirect(url_for('index'))
        else:
            flash('Produto não cadastrado!', 'error')
            return redirect(url_for('index'))
    else:
        titulo = 'Novo produto'
        return render_template('cadastro.html', titulo = titulo)

@app.route('/listar')
def listar():
    titulo = 'Listar produtos'
    mycursor = cnx.cursor()

    mycursor.execute("SELECT * FROM produtos")

    myresult = mycursor.fetchall()
    
    
    mycursor.close()
    produto = myresult[0]
    # print(produto[1])

    return render_template('listar.html',titulo=titulo, myresult=myresult)

@app.route('/apagarProduto', methods=['POST', "GET"])
def apagarProduto():
    if request.method == 'POST':   
        nome = request.form['nome']
        id = request.form['id_produto']
        print(nome)
        print(id)
        
        mycursor = cnx.cursor()
        
        sql = """DELETE FROM produtos WHERE produto_nome = '%s' and produto_id = '%d'""" % (nome, int(id))
        
        mycursor.execute(sql)
        
        
        cnx.commit()
        mycursor.close()
        
        flash('Produto apagado com sucesso!')
        return redirect(url_for('index'))
    else:
        titulo = 'Apagar produtos'
        return render_template('/apagar.html',titulo=titulo)
    

@app.route('/mudar', methods=['POST', "GET"])
def mudar():
    if request.method == "POST":
        nome = request.form['nome']
        categoria = request.form['options']
        
        nome_novo = request.form['nome_alterar']
        categoria_nova = request.form['options_alterar']
        
        if (nome != "" and categoria != "" and request.form.get('options') in ['enlatados', 'limpeza', 'comida', 'usaveis']) and (nome_novo != "" and categoria_nova != "" and request.form.get('options_alterar') in ['enlatados', 'limpeza', 'comida', 'usaveis']):
            nome = nome.title().strip()
            nome_novo = nome_novo.title().strip()
            
            mycursor = cnx.cursor()
                
            sql = """UPDATE produtos SET produto_nome = '%s' , produto_categoria = '%s' WHERE produto_nome = '%s' AND produto_categoria = '%s' """ % (nome_novo, categoria_nova, nome, categoria)
            

            mycursor.execute(sql)
                
            cnx.commit()
            mycursor.close()
            
            flash('Operação de edição efetuada com sucesso!')
            return redirect(url_for('index'))
        else:
            flash('Operação de edição não efetuada!')
            return redirect(url_for('index'))
    else:
        titulo = 'Mudar produtos'
        return render_template('/editar.html',titulo=titulo)

app.run(debug=True)
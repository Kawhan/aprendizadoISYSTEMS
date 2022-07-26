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
    def __init__(self, nome):
        self.nome = nome

class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria

lista_categoria = []

@app.route('/')
def index():
    return render_template('index.html', titulo="Escolha a ação!")




@app.route('/criar', methods=['POST','GET'])
def criar():
    if request.method == 'POST':
        nome = request.form['nome']
        
        if nome != "":
            nome = nome.title().strip()
            
            produto = Produto(nome)
             
            mycursor = cnx.cursor()
            
        
            sql = """INSERT INTO PRODUTOS (NOME) VALUES ('%s')""" % (produto.nome) 
        

            mycursor.execute(sql)
                
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

    mycursor.execute("SELECT * FROM PRODUTOS LEFT OUTER JOIN CATEGORIA ON PRODUTOS.ID = CATEGORIA.id_produto UNION SELECT * FROM PRODUTOS RIGHT OUTER JOIN CATEGORIA ON PRODUTOS.ID = CATEGORIA.id_produto")
    
    # [(1, 'Kawhan', 1, 'TESTE_categoria', 1)]

    myresult = mycursor.fetchall()
    # print(myresult)
    

    mycursor.close()
    # print(myresult)
    # print(produto[1])

    return render_template('listar.html',titulo=titulo, myresult=myresult)

@app.route('/apagarProduto/<int:id>', methods=['POST', "GET"])
def apagarProduto(id):
    mycursor = cnx.cursor()
        
    sql = """DELETE FROM PRODUTOS WHERE ID = '%d'""" % (int(id))
        
    mycursor.execute(sql)
        
        
    cnx.commit()
    mycursor.close()
        
    flash('Produto apagado com sucesso!')
    return redirect(url_for('index'))




@app.route('/mudar/<int:id>', methods=['POST', "GET"])
def mudar(id):
    if request.method == "POST":
        nome_novo = request.form['nome']
        # categoria_nova = request.form['options']
        
       
        nome_novo = nome_novo.title().strip()
            
        mycursor = cnx.cursor()
                
        sql = """UPDATE PRODUTOS SET NOME = '%s' WHERE ID = '%d' """ % (nome_novo, id)
            

        mycursor.execute(sql)
                
        cnx.commit()
        mycursor.close()
            
        flash('Operação de edição efetuada com sucesso!')
        return redirect(url_for('index'))
    else:
        titulo = 'Mudar produtos'
        return render_template('/editar.html',titulo=titulo, id=id)

@app.route('/mudarCategoria/<int:id>', methods=['POST', "GET"])
def mudarCategoria(id):
    if request.method == "POST":
        nome_novo = request.form['nome']
        # categoria_nova = request.form['options']
        
       
        nome_novo = nome_novo.title().strip()
            
        mycursor = cnx.cursor()
                
        sql = """UPDATE CATEGORIA SET NOME = '%s' WHERE id_produto = '%d' """ % (nome_novo, id)
            

        mycursor.execute(sql)
                
        cnx.commit()
        mycursor.close()
            
        flash('Operação de edição efetuada com sucesso!')
        return redirect(url_for('index'))
    else:
        titulo = 'Mudar produtos'
        return render_template('/editarCategoria.html',titulo=titulo, id=id)

@app.route('/apagarCategoria/<int:id>', methods=['POST', "GET"])
def apagarCategoria(id):
    mycursor = cnx.cursor()
        
    sql = """DELETE FROM CATEGORIA WHERE id_produto = '%d'""" % (int(id))
        
    mycursor.execute(sql)
        
        
    cnx.commit()
    mycursor.close()
        
    flash('CATEGORIA apagada com sucesso!')
    return redirect(url_for('index'))

@app.route('/criarCategoria/<int:id>', methods=['GET', 'POST'])
def criarCategoria(id):
    if request.method == 'POST':
        categoria = request.form['categoria']
        
        if categoria != "":
            categoria = categoria.title().strip()
            
            categoria = Categoria(categoria)
             
            mycursor = cnx.cursor()
            
        
            sql = """INSERT INTO CATEGORIA (NOME,id_produto) VALUES ('%s','%d')""" % (categoria.categoria, id) 
        

            mycursor.execute(sql)
                
            cnx.commit()
            mycursor.close()
            
            flash('CATEGORIA Cadastrada com sucesso!')
            return redirect(url_for('index'))
        else:
            flash('CATEGORIA não cadastrada!', 'error')
            return redirect(url_for('index'))
    else:
        titulo = 'Nova categoria'
        return render_template('cadastroCategoria.html', titulo = titulo, id=id)

app.run(debug=True)
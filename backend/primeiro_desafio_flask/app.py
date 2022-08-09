from crypt import methods
import re
from flask import Flask, redirect, render_template, request, redirect, flash, url_for
import mysql.connector

app = Flask(__name__)
app.secret_key = 'secret_key12345'


cnx = mysql.connector.connect(user='root', password='my-teste123',
                              host='localhost',
                              database='LOJA', port=7070)

class Produto:
    def __init__(self, nome):
        self.nome = nome

class Categoria:
    def __init__(self, nome):
        self.nome = nome

lista_categoria = []

@app.route('/')
def index():
    return render_template('index.html', titulo="Escolha a ação!")

@app.route('/criar', methods=['POST','GET'])
def criar():
    if request.method == 'POST':
        nome = request.form['nome']
        categoria = request.form['options']
        
        if nome != "":
            nome = nome.title().strip()
            categoria = categoria.title().strip()
            
            produto = Produto(nome)
            categoria = Categoria(categoria)
             
            mycursor = cnx.cursor()
            
            mycursor.execute("SELECT ID_CATEGORIA FROM CATEGORIA WHERE NOME = '%s'" % (categoria.nome))
            

            myresult = mycursor.fetchall()
                        
            sql = """INSERT INTO PRODUTOS (NOME, ID_CATEGORIA) VALUES ('%s', '%d')""" % (produto.nome, myresult[0][0]) 
            
            mycursor.execute(sql)
                
            cnx.commit()
            mycursor.close()
            
            flash('Produto Cadastrado com sucesso!')
            return redirect(url_for('index'))
        else:
            flash('Produto não cadastrado!', 'error')
            return redirect(url_for('index'))
    else:
        mycursor = cnx.cursor()
            
        mycursor.execute("SELECT NOME FROM CATEGORIA")
        categorias = mycursor.fetchall()
        # print(categorias)
        
        titulo = 'Novo produto'
        return render_template('cadastro.html', titulo = titulo, categorias = categorias)

@app.route('/listar')
def listar():
    titulo = 'Listar produtos'
    mycursor = cnx.cursor()

    mycursor.execute("SELECT * FROM PRODUTOS JOIN CATEGORIA ON PRODUTOS.ID_CATEGORIA=CATEGORIA.ID_CATEGORIA")
    
    # [(1, 'Kawhan', 1, 'TESTE_categoria', 1)]

    myresult = mycursor.fetchall()
    # print(myresult)
    

    mycursor.close()
    # print(myresult)
    # print(produto[1])

    return render_template('listar.html',titulo=titulo, myresult=myresult)

@app.route('/apagarProduto/<int:id>', methods=['POST', "GET"])
def apagarProduto(id):
    if request.method == 'POST':
        userInput = request.form.get("userInput")
        
        if userInput == "True":
            mycursor = cnx.cursor()
        
            sql = """DELETE FROM PRODUTOS WHERE ID_PRODUTO = '%d'""" % (int(id))
                
            mycursor.execute(sql)
                
                
            cnx.commit()
            mycursor.close()
                
            flash('Produto apagado com sucesso!')
            return redirect(url_for('index'))
        else:
            flash("Operação cancelada com sucesso!")
            return redirect(url_for('index'))
    else:
        mycursor = cnx.cursor()

        mycursor.execute("SELECT NOME FROM PRODUTOS WHERE ID_PRODUTO = '%d'" % (id))
    

        produtos = mycursor.fetchall()
    

        mycursor.close()
        
        titulo = 'Confirmação'
        return render_template('confirm2.html', titulo = titulo , id=id, produto = produtos[0][0])
    

@app.route('/mudar/<int:id>', methods=['POST', "GET"])
def mudar(id):
    if request.method == "POST":
        nome_novo = request.form['nome']
        
       
        nome_novo = nome_novo.title().strip()
            
        mycursor = cnx.cursor()
                
        sql = """UPDATE PRODUTOS SET NOME = '%s' WHERE ID_PRODUTO = '%d' """ % (nome_novo, id)
            

        mycursor.execute(sql)
                
        cnx.commit()
        mycursor.close()
            
        flash('Operação de edição efetuada com sucesso!')
        return redirect(url_for('index'))
    else:
        mycursor = cnx.cursor()
        
        mycursor.execute("SELECT * FROM PRODUTOS WHERE ID_PRODUTO = '%d'" % (id))
        produto = mycursor.fetchall()
        
        titulo = 'Mudar produtos'
        return render_template('/editar.html',titulo=titulo, id=id, produto = produto[0][1])


@app.route('/listarCategorias', methods=['GET'])
def listarCategorias():
    titulo = 'Listar Categorias'
    mycursor = cnx.cursor()

    mycursor.execute("SELECT * FROM CATEGORIA")

    myresult = mycursor.fetchall()
    

    mycursor.close()

    return render_template('listarCategoria.html',titulo=titulo, myresult=myresult)

@app.route('/mudarCategoria/<int:id>', methods=['POST', "GET"])
def mudarCategoria(id):
    if request.method == "POST":
        nome_novo = request.form['nome']
        # categoria_nova = request.form['options']
        
       
        nome_novo = nome_novo.title().strip()
            
        mycursor = cnx.cursor()
                
        sql = """UPDATE CATEGORIA SET NOME = '%s' WHERE ID_CATEGORIA = '%d' """ % (nome_novo, id)
            

        mycursor.execute(sql)
                
        cnx.commit()
        mycursor.close()
            
        flash('Operação de edição efetuada com sucesso!')
        return redirect(url_for('index'))
    else:
        mycursor = cnx.cursor()
        
        mycursor.execute("SELECT * FROM CATEGORIA WHERE ID_CATEGORIA = '%d'" % (id))
        produto = mycursor.fetchall()
        # print(produto)
        
        titulo = 'Mudar produtos'
        return render_template('/editarCategoria.html',titulo=titulo, id=id, produto = produto)

@app.route('/apagarCategoria/<int:id>', methods=['POST', "GET"])
def apagarCategoria(id):
    if request.method == 'POST':
        userInput = request.form.get("userInput")
        
        if userInput == "True":
            try:
                mycursor = cnx.cursor()
                    
                sql = """DELETE FROM CATEGORIA WHERE ID_CATEGORIA = '%d'""" % (int(id))
                    
                mycursor.execute(sql)
                    
                    
                cnx.commit()
                mycursor.close()
                    
                flash('CATEGORIA apagada com sucesso!')
                return redirect(url_for('index'))
            except:
                flash('CATEGORIA associada com produto existente, operação cancelada!', 'error')
                return redirect(url_for('index'))
        else:
            flash('Operação cancelada!')
            return redirect(url_for('index'))
    else:
        mycursor = cnx.cursor()

        mycursor.execute("SELECT NOME FROM CATEGORIA WHERE ID_CATEGORIA = '%d'" % (id))

        categorias = mycursor.fetchall()
    

        mycursor.close()
        
        titulo = 'Confirmação'
        return render_template('confirm.html', titulo = titulo , id=id, categoria = categorias[0][0])
   

@app.route('/criarCategoria', methods=['GET', 'POST'])
def criarCategoria():
    if request.method == 'POST':
        categoria = request.form['categoria']
        
        if categoria != "":
            categoria = categoria.title().strip()
            
            categoria = Categoria(categoria)
             
            mycursor = cnx.cursor()
            
        
            sql = """INSERT INTO CATEGORIA (NOME) VALUES ('%s')""" % (categoria.nome) 
        

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
        return render_template('cadastroCategoria.html', titulo = titulo)

app.run(debug=True)
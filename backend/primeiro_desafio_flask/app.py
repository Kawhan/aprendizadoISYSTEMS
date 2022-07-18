from crypt import methods
from flask import Flask, redirect, render_template, request, redirect, flash
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


@app.route('/cadastro')
def novo():
    titulo = 'Novo produto'
    return render_template('cadastro.html', titulo = titulo)

@app.route('/criar', methods=['POST','GET'])
def criar():
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
        return redirect('/')
    else:
        flash('Produto não cadastrado!', 'error')
        return redirect('/')

@app.route('/listar')
def listar():
    titulo = 'Listar produtos'
    mycursor = cnx.cursor()

    mycursor.execute("SELECT * FROM produtos")

    myresult = mycursor.fetchall()
    
    
    mycursor.close()
    produto = myresult[0]
    print(produto[1])

    return render_template('listar.html',titulo=titulo, myresult=myresult)

@app.route('/apagar')
def apagar():
    titulo = 'Apagar produtos'
    return render_template('/apagar.html',titulo=titulo)
 
    
    
@app.route('/apagarProduto', methods=['POST'])
def apagarProduto():
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
    return redirect ('/')
    
    

app.run(debug=True)
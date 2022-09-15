from flask import Flask, flash, redirect, render_template, request, redirect, session, flash, url_for

# Criando uma classe para associar o que vai ter em cada jogo
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack in Slash', 'PS2')
jogo3 = Jogo('Mortal Combat', 'Luta', 'PS2')
    
lista = [jogo1, jogo2, jogo3]    

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha
    

usuario1 = Usuario('Kawhan Laurindo', 'BD', 'alohomoro')
usuario2 = Usuario('Camila Ferreira', "Mila", "paozinho")
usuario3 = Usuario("Guilherme Louro", 'Cake', 'python')
    
usuarios = { usuario1.nickname: usuario1, 
            usuario2.nickname: usuario2, 
            usuario3.nickname: usuario3}

# Variavel onde vamos colocar nossa aplicação
app = Flask(__name__) # __name__ faz uma referencia a esse proprio arquivo
app.secret_key = 'alura'

# Criando uma rota

@app.route('/')

# Toda vez que criamos uma rota precisamos de uma função que vai definir o que tem dentro dessa rota
# Lembrando que o browser não trabalha com strings puras temos de definir uma tag HTML para que ele possa aparecer
def index():
    return render_template('lista.html', titulo='Jogos', jogos = lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] ==  None:
        return redirect(url_for('login', proxima=url_for('novo')))
    titulo = 'Novo jogo'
    return render_template('novo.html', titulo = titulo)

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima = proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash("Usuario não logado")
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

app.run(debug=True)  
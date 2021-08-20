import sqlite3
from flask import Flask, request, session, g, redirect, abort, render_template, flash

#configurações
DATABASE = "blog.db"
SECRET_KEY = "pudim"

app = Flask(__name__)             #(_name_) é o nome do módulo
app.config.from_object(__name__)

def conectar_bd():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def antes_requisicao():
    g.bd = conectar_bd()


@app.teardown_request
def depois_request(exc):
    g.bd.close()


@app.route('/entradas')                                     #criando uma rota
def exibir_entradas():
    return render_template('exibir_entradas.html')          #chama a págna HTML

@app.route('/hello')
def pagina_inicial():
    return "Hello Word!"
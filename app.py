from os import name
from flask import Flask, request, render_template, redirect, url_for
from conexaoDB import Crud

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/criar', methods=['POST','GET'])
def create():
    if request.method == 'POST':
        form = request.form.to_dict()
        Crud().insertClient(form['name'], form['email'], form['message'])
        return render_template('criar.html', isCreate=True, name=form['name'])

    return render_template('criar.html')

@app.route('/clientes')
def viewClients():
    getClients = Crud().returnAllClients()

    if not getClients:
        return render_template('clientes.html', clientes=False, deleted=request.args.get('deleted'))
    
    return render_template('clientes.html', clientes=getClients, deleted=request.args.get('deleted'))

@app.route('/clientes/<idCliente>')
def getClient(idCliente):
    getOneClient = Crud().returnClient(idCliente)
    return render_template('cliente.html', cliente=getOneClient)

@app.route('/deletar/<idCliente>')
def deleteClient(idCliente):
    Crud().deleteClient(idCliente)
    return redirect(url_for('viewClients', deleted=True))

@app.route('/alterar/<idCliente>', methods=['POST','GET'])
def alterClient(idCliente):
    if request.method == 'POST':
        form = request.form.to_dict()
        Crud().updateClient(form['name'], form['email'], form['message'], idCliente)
        return redirect(url_for('viewClients') )

    client = Crud().returnClient(idCliente)
    return render_template('alterar.html', client=client)

@app.errorhandler(404)
def error(err):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
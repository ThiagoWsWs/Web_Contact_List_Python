from flask import Flask, render_template, request, redirect, url_for, flash
from contato import (
    adicionar_contato,
    listar_contatos,
    buscar_contato,
    editar_contato,
    excluir_contato
)

app = Flask(__name__)
# Necessário para usar mensagens de feedback (flash messages)
app.secret_key = 'uma_chave_secreta_e_segura' 

@app.route('/')
def index():
    # Se o usuário pesquisar algo, filtramos. Se não, listamos todos.
    termo_busca = request.args.get('busca', '')
    if termo_busca:
        lista = buscar_contato(termo_busca)
    else:
        lista = listar_contatos()
    return render_template('index.html', contatos=lista, termo=termo_busca)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form['nome']
    telefone = request.form['telefone']
    email = request.form['email']
    
    sucesso, mensagem = adicionar_contato(nome, telefone, email)
    if not sucesso:
        flash(mensagem, 'danger')
    else:
        flash(mensagem, 'success')
        
    return redirect('/')

@app.route('/excluir/<int:id_contato>')
def excluir(id_contato):
    if excluir_contato(id_contato):
        flash('Contato excluído com sucesso!', 'success')
    else:
        flash('Erro ao excluir contato.', 'danger')
    return redirect('/')

@app.route('/editar/<int:id_contato>', methods=['POST'])
def editar(id_contato):
    nome = request.form['nome']
    telefone = request.form['telefone']
    email = request.form['email']
    
    sucesso, mensagem = editar_contato(id_contato, nome, telefone, email)
    if not sucesso:
        flash(mensagem, 'danger')
    else:
        flash(mensagem, 'success')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
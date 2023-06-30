from models.app import create
from flask import Blueprint, render_template, request, redirect, url_for, jsonify

bp = Blueprint('eventos', __name__)

@bp.route('/create', methods=['POST'])
def create_controller():
    
    nome = request.form['nome']
    inicio = request.form['data_inicio']
    termino = request.form['data_termino']
    hora_inicio = request.form['hora_inicio']
    hotra_termino = request.form['hora_termino']
    local = request.form['local']
    descricao = request.form['descricao']
    vagas = request.form['vagas']
    categoria = request.form['categoria']
    id_user = request.form['id_user']

    if id_user == '1':
        try:
            create(nome=nome, data_inicio=inicio, data_termino=termino, hora_inicio=hora_inicio, hora_termino=hotra_termino, local=local, descricao=descricao, vagas=vagas, categoria=categoria)
        except: 
            return jsonify({"Erro": "Não foi possível criar evento."})
        else:
            return jsonify({"Sucesso": "Evento criado com sucesso."})
    else:
        return "Erro"



    






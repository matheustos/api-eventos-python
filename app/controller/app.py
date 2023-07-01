from validators.validacaoEventos import validaCancelamento, validaData, validaInformacoes
from Model.models import create, cancelar, pegaData
from flask import request, jsonify

def create_controller():

    dados = request.form
    
    nome = request.form['nome']
    inicio = request.form['data_inicio']
    termino = request.form['data_termino']
    hora_inicio = request.form['hora_inicio']
    hora_termino = request.form['hora_termino']
    local = request.form['local']
    descricao = request.form['descricao']
    vagas = request.form['vagas']
    categoria = request.form['categoria']
    id_user = request.form['id_user']


    if validaInformacoes(dados=dados):

        if validaData(dados=dados):

            if id_user == '1':
                try:
                    create(nome=nome, data_inicio=inicio, data_termino=termino, hora_inicio=hora_inicio, hora_termino=hora_termino, local=local, descricao=descricao, vagas=vagas, categoria=categoria)
                except: 
                    return jsonify({"Erro": "Não foi possível criar evento."})
                else:
                    return jsonify({"Sucesso": "Evento criado com sucesso."})
            else:
                return jsonify({"Erro": "Você não tem autorização para executar essa tarefa."})
        else:
            return jsonify({"Erro": "A data do evento deve ser superior à data de hoje."})
    else:
        return jsonify({"Erro": "Todos os campos devem ser preenchidos."})
    
def cancelar_controller():

    dados = request.form
    id = request.form['id']
    id_user = request.form['id_user']

    if validaCancelamento(dados=dados):
        if pegaData(id=id):
            if id_user == '1':
                try:
                    cancelar(id=dados.get('id'))
                except: 
                        return jsonify({"Erro": "Não foi possível cancelar o evento."})
                else:
                    return jsonify({"Sucesso": "Evento cancelado com sucesso."})
            else:
                return jsonify({"Erro": "Você não tem autorização para executar essa tarefa."})
        else:
            return jsonify({"Erro": "Não é possivel cancelar no dia que se inicia o evento."})
    else:
        return jsonify({"Erro": "Todos os campos devem ser preenchidos."})
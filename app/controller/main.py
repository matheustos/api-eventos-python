from validators.validacaoEventos import validaDados, validaData, validaInformacoes
from Model.models import create, cancelar, pegaData, iniciar, concluir, listarEventos, listarEventosPorData, listarEventosPorCat
from flask import request, jsonify
from datetime import date, timedelta
from json import dumps

# função para criar novo evento
def create_controller():

    dados = request.form
    
    nome = request.form['nome'].strip()
    inicio = request.form['data_inicio'].strip()
    termino = request.form['data_termino'].strip()
    hora_inicio = request.form['hora_inicio'].strip()
    hora_termino = request.form['hora_termino'].strip()
    local = request.form['local'].strip()
    descricao = request.form['descricao'].strip()
    vagas = request.form['vagas'].strip()
    categoria = request.form['categoria'].strip()
    id_user = request.form['id_user'].strip()

    # valida se todas as requisições foram passadas
    if validaInformacoes(dados=dados):
        # valida se a data do evento é a mesma de hoje
        if validaData(dados=dados):
            # valida se o usuário tem permissão para inciar o evento
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

#função para iniciar evento
def iniciar_controller():

    dados = request.form
    id = request.form['id'].strip()
    id_user = request.form['id_user'].strip()

    # valida se todas as requisições foram passadas
    if validaDados(dados=dados):
        # valida se a data evento é a mesma de hoje e caso seja, retorna False
        if not pegaData(id=id):
            # valida se o usuário tem permissão para inciar o evento
            if id_user == '1':
                try:
                    iniciar(id=id)
                except: 
                        return jsonify({"Erro": "Não foi possível iniciar o evento."}) 
                else:
                    return jsonify({"Sucesso": "Evento inciado com sucesso."})
            else:
                return jsonify({"Erro": "Você não tem autorização para executar essa tarefa."})
        else:
            return jsonify({"Erro": "Só é possível iniciar o evento no dia agendado."})
    else:
        return jsonify({"Erro": "Todos os campos devem ser preenchidos."})

# função para cancelar evento
def cancelar_controller():

    dados = request.form
    id = request.form['id'].strip()
    id_user = request.form['id_user'].strip()

    # valida se todas as requisições foram passadas
    if validaDados(dados=dados):
        # valida se a data evento é a mesma de hoje e caso seja, retorna False, caso não seja retorna True
        if pegaData(id=id):
            # valida se o usuário tem permissão para inciar o evento
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

# função para concluir evento
def concluir_controller():

    dados = request.form
    id = request.form['id'].strip()
    id_user = request.form['id_user'].strip()

    # valida se todas as requisições foram passadas
    if validaDados(dados=dados):
            # valida se o usuário tem permissão para inciar o evento
            if id_user == '1':
                try:
                    concluir(id=id)
                except:
                    return jsonify({"Erro": "Só é possível concluir um evento que já foi inciado."})
                else:
                    return jsonify({"Sucesso": "Evento concluido com sucesso."})
                    
            else:
                return jsonify({"Erro": "Você não tem autorização para executar essa tarefa."})
    else:
        return jsonify({"Erro": "Todos os campos devem ser preenchidos."})
    
# função para listar todos os eventos
def listarEventos_controller():

    def custom_serialization(obj):
        if isinstance(obj, (date, timedelta)):
            return str(obj)
        raise TypeError(f"Objeto do tipo {type(obj).__name__} não pode ser serializado em JSON")
        
    resultado = listarEventos()

    if resultado:
        eventos = []
        for evento in resultado:
            eventos.append({
                "id": evento[0],
                "Nome": evento[1],
                "Data de Inicio": evento[2],
                "Data de Termino": evento[3],
                "Hora de Inicio": evento[4],
                "Hora de Termino": evento[5],
                "Local": evento[6],
                "Descricao": evento[7],
                "Vagas": evento[8],
                "Categoria": evento[9],
                "Status": evento[10]
            })

        return dumps(eventos, default=custom_serialization)
    else:
        return jsonify({"Erro": "Nenhum evento encontrado."})

# função para listar eventos por data
def listarEventosPorData_controller():

    def custom_serialization(obj):
        if isinstance(obj, (date, timedelta)):
            return str(obj)
        raise TypeError(f"Objeto do tipo {type(obj).__name__} não pode ser serializado em JSON")

    data = request.form['data_inicio'].strip()

    if data:
        resultado = listarEventosPorData(data)

        if resultado:
            eventos = []
            for evento in resultado:
                eventos.append({
                    "id": evento[0],
                    "Nome": evento[1],
                    "Data de Inicio": evento[2],
                    "Data de Termino": evento[3],
                    "Hora de Inicio": evento[4],
                    "Hora de Termino": evento[5],
                    "Local": evento[6],
                    "Descricao": evento[7],
                    "Vagas": evento[8],
                    "Categoria": evento[9],
                    "Status": evento[10]
                })

            return dumps(eventos, default=custom_serialization)
        else:
            return jsonify({"Erro": "Nenhum evento com essa data foi encontrado."})
    else:
        return jsonify({"Erro": "A data de inicio do evento deve ser informada."})
    
# função para listar eventos por categoria
def listarEventosPorCat_controller():

    def custom_serialization(obj):
        if isinstance(obj, (date, timedelta)):
            return str(obj)
        raise TypeError(f"Objeto do tipo {type(obj).__name__} não pode ser serializado em JSON")

    categoria = request.form['categoria'].strip()

    if categoria:
        resultado = listarEventosPorCat(categoria)

        if resultado:
            eventos = []
            for evento in resultado:
                eventos.append({
                    "id": evento[0],
                    "Nome": evento[1],
                    "Data de Inicio": evento[2],
                    "Data de Termino": evento[3],
                    "Hora de Inicio": evento[4],
                    "Hora de Termino": evento[5],
                    "Local": evento[6],
                    "Descricao": evento[7],
                    "Vagas": evento[8],
                    "Categoria": evento[9],
                    "Status": evento[10]
                })

            return dumps(eventos, default=custom_serialization)
        else:
            return jsonify({"Erro": "Não existe nenhum evento dessa categoria."})
    else:
        return jsonify({"Erro": "A categoria deve ser informada."})
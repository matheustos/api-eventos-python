from flask import jsonify, request
from Model.models import inscricao, buscaEvento, verificaStatus, listar_inscritos, presenca
from validators.validacaoInscricao import validaDadosInscricao, validaInscritos, validaPresenca

# realizar inscrição em um evento
def inscricao_controller():

    nome = request.form['nome'].strip()
    evento = request.form['evento'].strip()

    resultado = buscaEvento(evento)

    status = verificaStatus(evento)

    if validaDadosInscricao(nome, evento):
        if resultado:
            if status[0] == "Aberto para inscriçoes":
                try:
                    inscricao(nome, evento)
                except:
                    return jsonify({"Erro": "Não foi possível realizar a inscrição."})
                else:
                    return jsonify({"Sucesso": "Inscrição realizada com sucesso."})
                
            elif status[0] == "Em andamento":
                return jsonify({"Erro": "Não é possível se inscrever em um evento que já foi inciado."})
            
            elif status[0] == "Cancelado":
                return jsonify({"Erro": "Não é possível se inscrever em um evento cancelado."})
            
            elif status[0] == "Concluido":
                return jsonify({"Erro": "Não é possível se inscrever em um evento que já foi concluído."})
        else:
            return jsonify({"Erro": "Não existe evento com esse nome."})   
    else:
        return jsonify({"Erro": "Todos os dados devem ser informados."})
    
# realizar listagem de usuários inscritos em um evento
def inscritos_controller():

    evento = request.form['evento']

    resultado = listar_inscritos(evento)

    if validaInscritos(evento=evento):
        if resultado:
            inscritos = []
            for inscrito in resultado:
                inscritos.append({
                    "id": inscrito[0],
                    "Nome": inscrito[1],
                    "Evento": inscrito[2]
                })
            return jsonify(inscritos)
        else:
            return jsonify({"Erro": "Não há usuários inscritos nesse evento."})
    else:
        return jsonify({"Erro": "É necessário informar o nome do evento."})
    
# realizar confirmação de presença (administrador)
def presenca_controller():

    evento = request.form['evento']
    id_inscrito = request.form['id_inscrito']
    id_user = request.form['id_user']

    if validaPresenca(id_inscrito, evento, id_user):
        if id_user == '1':
            try:
                presenca(id_inscrito, evento)
            except:
                return jsonify({"Erro": "Não foi possivel confirmar a presença."})
            else:
                return jsonify({"Sucesso": "Presença confirmada com sucesso."})
        else:
            return jsonify({"Erro": "Você não tem autorização para realizar essa tarefa."})
    else: 
        return jsonify({"Erro": "É necessário informar todos os dados."})

from flask import jsonify, request
from Model.models import inscricao, buscaEvento, verificaStatus, listar_inscritos, presenca, modifica_vagas, avaliacao, checa_inscrito
from validators.validacaoInscricao import validaDadosInscricao, validaInscritos, validaPresenca, validaAvaliacao

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
                    modifica_vagas(evento)

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

    evento = request.form['evento'].strip()
    id_inscrito = request.form['id_inscrito'].strip()
    id_user = request.form['id_user'].strip()

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
    
def avaliacao_controller():

    nome = request.form['nome'].strip()
    evento = request.form['evento'].strip()
    estrelas = request.form['estrelas'].strip()
    comentario = request.form['comentario'].strip()

    if validaAvaliacao(nome, evento, estrelas, comentario):
        if checa_inscrito(evento, nome):
            resultado = verificaStatus(evento)
            if resultado:
                status = resultado[0]
                if status == "Concluido":
                    try:
                        avaliacao(nome, evento, estrelas, comentario)
                    except:
                        return jsonify({"Erro": "Não foi possivel adicionar a avaliacao."})
                    else:
                        return jsonify({"Sucesso": "Avaliacao adicionada com sucesso."})
                else:
                    return jsonify({"Erro": "Não é possivel avaliar um evento que ainda nao foi concluido."})
            else:
                return jsonify({"Erro": "Nenhum evento encontrado."})
        else:
            return jsonify({"Erro": "Usuário não estava inscrito nesse evento."})
    else:
        return jsonify({"Erro": "Todos os dados devem ser informados."})


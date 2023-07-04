from flask import jsonify, request
from Model.models import inscricao, buscaEvento, verificaStatus
from validators.validacaoInscricao import validaDadosInscricao

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
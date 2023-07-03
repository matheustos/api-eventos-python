from datetime import date, datetime


def validaInformacoes(dados):
        if not dados.get('nome'):
            return False
        if not dados.get('data_inicio'):
            return False
        if not dados.get('data_termino'):
            return False
        if not dados.get('hora_inicio'):
            return False
        if not dados.get('hora_termino'):
            return False
        if not dados.get('local'):
            return False
        if not dados.get('descricao'):
            return False
        if not dados.get('vagas'):
            return False
        if not dados.get('categoria'):
            return False
        if not dados.get('id_user'):
            return False
        
        return True

def validaData(dados):
    # pega a data de hoje
    data_hoje = date.today()

    #converte a string recebida via formulário para o formato date
    data = datetime.strptime(dados.get('data_inicio'), "%Y-%m-%d").date()

    # verifica se a data informada é a mesma de hoje
    if data == data_hoje:
        return False
    return True

def validaDados(dados):
    if not dados.get('id'):
            return False
    if not dados.get('id_user'):
        return False
    return True


def validaDadosInscricao(nome, evento):
    if not nome:
            return False
    if not evento:
            return False
    return True

def validaInscritos(evento):
    if not evento:
        return False
    return True 

def validaPresenca(nome, evento, id_user):
    if not nome:
        return False
    if not evento:
        return False
    if not id_user:
        return False
    return True

def validaAvaliacao(nome, evento, estrelas, comentario):
    if not nome:
        return False
    if not evento:
        return False
    if not estrelas:
        return False
    if not comentario:
        return False
    return True
       
       





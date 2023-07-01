from . import bd
from datetime import date

conexao = bd.conexao
def create(nome, data_inicio, data_termino, hora_inicio, hora_termino, local, descricao, vagas, categoria):

    status = "Aberto para inscriçoes"

    cursor = conexao.cursor()
    comando = f'INSERT INTO eventos (Nome, Inicio, Termino, Hora_inicio, Hora_termino, Local, Descricao, Vagas, Categoria, status) VALUES ("{nome}","{data_inicio}", "{data_termino}", "{hora_inicio}", "{hora_termino}", "{local}", "{descricao}", "{vagas}", "{categoria}", "{status}")'
    cursor.execute(comando)
    conexao.commit()

def pegaData(id):

    cursor = conexao.cursor()
    comando = f'SELECT Inicio FROM eventos WHERE id = "{id}"'
    cursor.execute(comando)
    resultado = cursor.fetchone()

    data = resultado[0]
    # pega a data de hoje
    data_hoje = date.today()

    #converte a string recebida via formulário para o formato date
    #data_formatada = datetime.strptime(data, "%Y-%m-%d").date()

    # verifica se a data informada é a mesma de hoje
    if data == data_hoje:
        return False
    return True

    
def cancelar(id):

    status = "Cancelado"

    cursor = conexao.cursor()
    comando = f'UPDATE eventos SET status = "{status}" WHERE id = "{id}"'
    cursor.execute(comando)
    conexao.commit()

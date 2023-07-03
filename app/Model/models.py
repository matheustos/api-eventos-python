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

def iniciar(id):

    status = "Em andamento"

    cursor = conexao.cursor()
    comando = f'UPDATE eventos SET status = "{status}" WHERE id = "{id}"'
    cursor.execute(comando)
    conexao.commit()

def concluir(id):

    cursor = conexao.cursor()
    comando = f'SELECT status FROM eventos WHERE id = "{id}"'
    cursor.execute(comando)
    resultado = cursor.fetchone()

    status = resultado[0]

    if status == "Em andamento":
        
        status_update = "Concluído"

        comando = f'UPDATE eventos SET status = "{status_update}" WHERE id = "{id}"'
        cursor.execute(comando)
        conexao.commit()

def listarEventos():

    cursor = conexao.cursor()
    comando = f'SELECT * FROM eventos'
    cursor.execute(comando)
    resultado = cursor.fetchall()

    return resultado


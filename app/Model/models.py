from . import bd
from datetime import date

conexao = bd.conexao

# --------------------------------------------------------------EVENTOS-----------------------------------------------------------------------------------

# cria registro de um novo evento no banco de dados
def create(nome, data_inicio, data_termino, hora_inicio, hora_termino, local, descricao, vagas, categoria):

    status = "Aberto para inscriçoes"

    cursor = conexao.cursor()
    comando = f'INSERT INTO eventos (Nome, Inicio, Termino, Hora_inicio, Hora_termino, Local, Descricao, Vagas, Categoria, status) VALUES ("{nome}","{data_inicio}", "{data_termino}", "{hora_inicio}", "{hora_termino}", "{local}", "{descricao}", "{vagas}", "{categoria}", "{status}")'
    cursor.execute(comando)
    conexao.commit()

# busca a data de inicio de um evento e checa se é a mesma data de hoje
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

# realiza alterção do status de um evento para "Cancelado"
def cancelar(id):

    status = "Cancelado"

    cursor = conexao.cursor()
    comando = f'UPDATE eventos SET status = "{status}" WHERE id = "{id}"'
    cursor.execute(comando)
    conexao.commit()

# realiza alterção do status de um evento para "Em andamento"
def iniciar(id):

    status = "Em andamento"

    cursor = conexao.cursor()
    comando = f'UPDATE eventos SET status = "{status}" WHERE id = "{id}"'
    cursor.execute(comando)
    conexao.commit()

# realiza alterção do status de um evento para "Concluido"
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

# busca todos os registros da tabela eventos
def listarEventos():

    cursor = conexao.cursor()
    comando = f'SELECT * FROM eventos'
    cursor.execute(comando)
    resultado = cursor.fetchall()

    return resultado

# busca todos os eventos por data
def listarEventosPorData(data_inicio):

    cursor = conexao.cursor()
    comando = f'SELECT * FROM eventos WHERE Inicio = "{data_inicio}"'
    cursor.execute(comando)
    resultado = cursor.fetchall()

    return resultado

# busca todos os eventos por categoria
def listarEventosPorCat(categoria):

    cursor = conexao.cursor()
    comando = f'SELECT * FROM eventos WHERE Categoria = "{categoria}"'
    cursor.execute(comando)
    resultado = cursor.fetchall()

    return resultado

# --------------------------------------------------------------INSCRIÇÃO-----------------------------------------------------------------------------------

# cria um novo registro na tabela inscritos
def inscricao(nome, evento):

    presenca = "false"

    cursor = conexao.cursor()
    comando = f'INSERT INTO inscritos (Nome, Evento, Presenca) VALUES ("{nome}", "{evento}", "{presenca}")'
    cursor.execute(comando)
    conexao.commit()

# busca evento por nome para checar se o evento existe
def buscaEvento(evento):
    
    cursor = conexao.cursor()
    comando = f'SELECT * FROM eventos WHERE Nome = "{evento}"'
    cursor.execute(comando)
    resultado = cursor.fetchone()

    return resultado

# busca evento por nome para checar se é possível realizar inscrição no evento
def verificaStatus(evento):

    cursor = conexao.cursor()
    comando = f'SELECT status FROM eventos WHERE Nome = "{evento}"'
    cursor.execute(comando)
    resultado = cursor.fetchone()

    return resultado

# realizar busca de usuários inscritos em um evento
def listar_inscritos(evento):

    cursor = conexao.cursor()
    comando = f'SELECT * FROM inscritos WHERE Evento = "{evento}"'
    cursor.execute(comando)
    resultado = cursor.fetchall()

    return resultado

# realizar confirmação de presença de um usuário
def presenca(id_inscrito, evento):

    status = "true"

    cursor = conexao.cursor()
    comando = f'UPDATE inscritos SET Presenca = "{status}" WHERE id = "{id_inscrito}" AND Evento = "{evento}"'
    cursor.execute(comando)
    conexao.commit()

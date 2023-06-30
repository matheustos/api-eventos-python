from . import bd
conexao = bd.conexao

def create(nome, data_inicio, data_termino, hora_inicio, hora_termino, local, descricao, vagas, categoria):


    status = "Aberto para inscriçoes"

    cursor = conexao.cursor()
    comando = f'INSERT INTO eventos (Nome, Inicio, Termino, Hora_inicio, Hora_termino, Local, Descricao, Vagas, Categoria, status) VALUES ("{nome}","{data_inicio}", "{data_termino}", "{hora_inicio}", "{hora_termino}", "{local}", "{descricao}", "{vagas}", "{categoria}", "{status}")'
    cursor.execute(comando)
    conexao.commit()
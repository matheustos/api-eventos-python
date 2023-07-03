import mysql.connector
try:
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password= '',
        database='sistema-de-eventos'
    )
except:
    print("Erro ao conectar no banco de dados.")

cursor = conexao.cursor()


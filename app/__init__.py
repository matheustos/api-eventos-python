from flask import Flask

app = Flask(__name__)

# Configurações
app.config['SECRET_KEY'] = 'chave_secreta'
app.config['JSON_SORT_KEYS'] = False  # Desabilita a ordenação dos JSONs

# Importação das views
import views
bp = views.bp

# Registro do blueprint
app.register_blueprint(bp, url_prefix='/eventos')

if __name__ == '__main__':
    app.run(debug=True)
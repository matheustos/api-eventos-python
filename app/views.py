from controller.main import create_controller, cancelar_controller, iniciar_controller, concluir_controller, listarEventos_controller
from flask import Blueprint


bp = Blueprint('eventos', __name__)

# rota para criar evento
@bp.route('/create', methods=['POST'])
def criarEvento():
    return create_controller()
    
# rota para iniciar o evento
@bp.route('/iniciar', methods=['POST'])
def iniciarEvento():
    return iniciar_controller()

# rota para cancelar o evento
@bp.route('/cancelar', methods=['POST'])
def cancelarEvento():
    return cancelar_controller()

# rota para concluir o evento
@bp.route('/concluir', methods=['POST'])
def concluirEvento():
    return concluir_controller()

# rota para listar todos os eventos
@bp.route('/listar_eventos', methods=['GET'])
def listarEventos():
    return listarEventos_controller()

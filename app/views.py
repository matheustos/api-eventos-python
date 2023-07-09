from controller.main import create_controller, cancelar_controller, iniciar_controller, concluir_controller, listarEventos_controller, listarEventosPorData_controller, listarEventosPorCat_controller
from controller.inscritos import inscricao_controller, inscritos_controller, presenca_controller, avaliacao_controller
from flask import Blueprint


bp = Blueprint('eventos', __name__)

# rota para criar evento (administrador)
@bp.route('/create', methods=['POST'])
def criarEvento():
    return create_controller()
    
# rota para iniciar o evento (administrador)
@bp.route('/iniciar', methods=['POST'])
def iniciarEvento():
    return iniciar_controller()

# rota para cancelar o evento (administrador)
@bp.route('/cancelar', methods=['POST'])
def cancelarEvento():
    return cancelar_controller()

# rota para concluir o evento (administrador)
@bp.route('/concluir', methods=['POST'])
def concluirEvento():
    return concluir_controller()

# rota para listar todos os eventos
@bp.route('/listar_eventos', methods=['GET'])
def listarEventos():
    return listarEventos_controller()

# rota para listar eventos de acordo com a data passada
@bp.route('/listar/data', methods=['POST'])
def listarEventosPorData():
    return listarEventosPorData_controller()

# rota para listar eventos de acordo com a categoria informada
@bp.route('/listar/categoria', methods=['POST'])
def listarPorCategoria():
    return listarEventosPorCat_controller()

# rota para realizar inscrições
@bp.route('/inscricao', methods=['POST'])
def inscricao():
    return inscricao_controller()

# rota para listar usuarios inscritos em um evento
@bp.route('/inscricao/listar', methods=['POST'])
def inscritos():
    return inscritos_controller()

# rota para confirmar presença de um usuário (administrador)
@bp.route('/inscricao/presenca', methods=['POST'])
def presenca():
    return presenca_controller()

# rota para enviar avaliação de um evento
@bp.route('/avaliacao', methods=['POST'])
def avaliacao():
    return avaliacao_controller()
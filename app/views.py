from controller.app import create_controller, cancelar_controller
from flask import Blueprint


bp = Blueprint('eventos', __name__)

@bp.route('/create', methods=['POST'])
def criarEvento():
    return create_controller()
    

@bp.route('/cancelar', methods=['POST'])
def cancelarEvento():
    return cancelar_controller()
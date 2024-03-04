from alpes.seedwork.aplicacion.handlers import Handler
from alpes.modulos.contratos.infraestructura.despachadores import Despachador

class HandlerContratoIntegracion(Handler):

    @staticmethod
    def handle_contrato_creado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-compania')
from auditoria.seedwork.aplicacion.handlers import Handler
from auditoria.modulos.audit.infraestructura.despachadores import Despachador

class HandlerAuditoriaIntegracion(Handler):

    @staticmethod
    def handle_auditoria_creado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-compania')
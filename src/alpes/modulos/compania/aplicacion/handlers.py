from alpes.seedwork.aplicacion.handlers import Handler
from alpes.modulos.compania.infraestructura.despachadores import Despachador

class HandlerCompaniaIntegracion(Handler):

    @staticmethod
    def handle_compania_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-compania')
from pydispatch import dispatcher

from .handlers import HandlerCompaniaIntegracion

from alpes.modulos.compania.dominio.eventos import CompaniaCreada

dispatcher.connect(HandlerCompaniaIntegracion.handle_compania_creada, signal=f'{CompaniaCreada.__name__}Integracion')
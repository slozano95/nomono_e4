from pydispatch import dispatcher

from .handlers import HandlerContratoIntegracion

from contratos.modulos.contratos.dominio.eventos import ContratoCreado

dispatcher.connect(HandlerContratoIntegracion.handle_contrato_creado, signal=f'{ContratoCreado.__name__}Integracion')
from pydispatch import dispatcher

from .handlers import HandlerAuditoriaIntegracion

from contratos.modulos.contratos.dominio.eventos import ContratoCreado

dispatcher.connect(HandlerAuditoriaIntegracion.handle_auditoria_creado, signal=f'{ContratoCreado.__name__}Integracion')
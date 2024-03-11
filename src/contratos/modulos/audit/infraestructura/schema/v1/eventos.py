from pulsar.schema import *
from auditoria.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class AuditoriaCreadaPayload(Record):
    auditoria = String()

class EventoAuditoriaCreada(EventoIntegracion):
    data = AuditoriaCreadaPayload()
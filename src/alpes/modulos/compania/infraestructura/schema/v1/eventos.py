from pulsar.schema import *
from alpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class CompaniaCreadaPayload(Record):
    id = String()

class EventoCompaniaCreada(EventoIntegracion):
    data = CompaniaCreadaPayload()
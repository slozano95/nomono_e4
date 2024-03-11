from pulsar.schema import *
from contratos.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class ContratoCreadoPayload(Record):
    id = String()
    compania = String()

class EventoContratoCreado(EventoIntegracion):
    data = ContratoCreadoPayload()

class CompaniaCreadaPayload(Record):
    compania = String()

class EventoCompaniaCreada(EventoIntegracion):
    data = CompaniaCreadaPayload()
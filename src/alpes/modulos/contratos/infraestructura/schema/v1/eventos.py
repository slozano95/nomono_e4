from pulsar.schema import *
from alpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class ContratoCreadoPayload(Record):
    id = String()
    compania = String()

class EventoContratoCreado(EventoIntegracion):
    data = ContratoCreadoPayload()
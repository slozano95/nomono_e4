from pulsar.schema import *
from alpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class CompaniaCreadaPayload(Record):
    id = String()

class EventoCompaniaCreada(EventoIntegracion):
    data = CompaniaCreadaPayload()
    
class ReservaCreadaPayload(Record):
    id_reserva = String()
    id_cliente = String()
    estado = String()
    fecha_creacion = Long()

class EventoReservaCreada(EventoIntegracion):
    data = ReservaCreadaPayload()
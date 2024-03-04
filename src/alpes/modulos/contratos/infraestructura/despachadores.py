import pulsar
from pulsar.schema import *

from alpes.modulos.contratos.infraestructura.schema.v1.eventos import ContratoCreadoPayload, EventoContratoCreado
from alpes.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoContratoCreado))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        payload = ContratoCreadoPayload(
            id=str(evento.id),
            compania = str(evento.compania)
        )
        evento_integracion = EventoContratoCreado(data=payload)
        print("PUBLICANDO EVENTO CONTRATO CREADO")
        print(evento_integracion)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoContratoCreado))

    def publicar_comando(self, comando, topico):
        pass

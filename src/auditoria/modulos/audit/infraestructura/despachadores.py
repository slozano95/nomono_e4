import pulsar
from pulsar.schema import *

from alpes.modulos.compania.infraestructura.schema.v1.eventos import EventoCompaniaCreada, CompaniaCreadaPayload
from auditoria.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoCompaniaCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        payload = CompaniaCreadaPayload(
            id=str(evento.id), 
        )
        evento_integracion = EventoCompaniaCreada(data=payload)
        print("PUBLICANDO EVENTO COMPANIA CREADA")
        print(evento_integracion)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoCompaniaCreada))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        pass


import logging
import traceback
from alpes.seedwork.infraestructura import utils
from contratos.modulos.contratos.infraestructura.schema.v1.eventos import EventoCompaniaCreada, EventoContratoCreado

import pulsar,_pulsar
from pulsar.schema import *

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-notifier', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='eventos', schema=AvroSchema(EventoCompaniaCreada))
        logging.info('OK: Suscribiendose al tópico de eventos notifier!')
        while True:
            print(f'Evento compania creada notifier recibido')
            mensaje = consumidor.receive()
            print(f'Evento compania creada notifier recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos notifier!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos():
    pass
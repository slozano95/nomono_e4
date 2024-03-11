import logging
import traceback
from auditoria.seedwork.infraestructura import utils
from auditoria.modulos.audit.infraestructura.schema.v1.eventos import EventoCompaniaCreada
import pulsar,_pulsar
from pulsar.schema import *
from dataclasses import dataclass, field
from auditoria.modulos.audit.infraestructura.schema.v1.eventos import EventoContratoCreado
from alpes.modulos.compania.aplicacion.comandos.registrar_compania import RegistrarCompania
from auditoria.seedwork.aplicacion.comandos import ejecutar_commando

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-compania', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='eventos', schema=AvroSchema(EventoContratoCreado))
        logging.info('OK: Suscribiendose al tópico de eventos compania!')
        while True:
            print(f'Evento EventoContratoCreado recibido')
            mensaje = consumidor.receive()
            print(f'Payload recibido: {mensaje.value().data}')
            consumidor.acknowledge(mensaje)
            #EJECUTAR CREACION DE LA COMPANIA
            comando = RegistrarCompania(id=mensaje.value().data.id, nombre=mensaje.value().data.compania)
            ejecutar_commando(comando)
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos compania!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos():
    pass
    # cliente = None
    # try:
    #     cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
    #     consumidor = cliente.subscribe('comandos-compania', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='comandos', schema=AvroSchema(Comando))
    #     logging.info('OK: Suscribiendose al tópico de comandos compania!')
    #     while True:
    #         print(f'Comando compania recibido')
    #         mensaje = consumidor.receive()
    #         print(f'Comando compania recibido: {mensaje.value().data}')

    #         consumidor.acknowledge(mensaje)     
            
    #     cliente.close()
    # except:
    #     logging.error('ERROR: Suscribiendose al tópico de comandos compania!')
    #     traceback.print_exc()
    #     if cliente:
    #         cliente.close()
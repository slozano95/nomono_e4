from __future__ import print_function

from google.protobuf.timestamp_pb2 import Timestamp
from alpes.pb2py import companias_pb2
from alpes.pb2py import companias_pb2_grpc
from alpes.utils import dict_a_proto_itinerarios

import logging
import grpc
import datetime
import os
import json


def importar_comando(json_file):
    json_dict = json.load(json_file)

    return json_dict

def dict_a_proto_reserva(dict_reserva):
    return companias_pb2.Compania(id="123422", nombre="test")

def run():

    print("Crear una compania")
    with grpc.insecure_channel('localhost:50051') as channel:
        json_file = open(f'{os.path.dirname(__file__)}/mensajes/crear_compania.json')
        json_dict = importar_comando(json_file)
        compania = dict_a_proto_reserva(json_dict)
        stub = companias_pb2_grpc.CompaniasStub(channel)
        response = stub.CrearCompania(compania)
        
    print("Greeter client received: " + response.mensaje)
    print(f'Confirmacion: {response}')


if __name__ == '__main__':
    logging.basicConfig()
    run()
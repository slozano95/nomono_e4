from concurrent import futures
import logging

import grpc
from alpes.pb2py import companias_pb2
from alpes.pb2py import companias_pb2_grpc


from alpes.servicios.companias import Companias

def agregar_servicios(servidor):
    companias_pb2_grpc.add_CompaniasServicer_to_server(Companias(), servidor)

def serve():
    port = '50051'
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    agregar_servicios(servidor)

    servidor.add_insecure_port('[::]:' + port)
    servidor.start()
    print("Servidor corriendo por el puerto:" + port)
    servidor.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
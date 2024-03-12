import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime


AEROALPES_HOST = os.getenv("AEROALPES_ADDRESS", default="localhost")
FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

def obtener_companias(root) -> typing.List["Reserva"]:
    json = requests.get(f'http://{AEROALPES_HOST}:5000/companias/get').json()
    companias = []

    for compania in companias:
        companias.append(
            Compania(
                id=compania.get('id'), 
                nombre=compania.get('nombre', '')
            )
        )

    return companias

@strawberry.type
class Compania:
    id: str
    nombre: str

@strawberry.type
class RtaBFF:
    data: str
    codigo: int







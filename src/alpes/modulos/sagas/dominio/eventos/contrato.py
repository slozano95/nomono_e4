from __future__ import annotations
from dataclasses import dataclass, field
import string
import uuid
from alpes.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime
from alpes.modulos.compania.infraestructura.schema.v1.eventos import EventoCompaniaCreada
class EventoCliente(EventoDominio):
    ...


@dataclass
class CompaniaCreada(EventoCompaniaCreada):
    id: uuid.UUID = None
    nombre: string = None

@dataclass
class AuditoriaCreada(EventoCompaniaCreada):
    id: uuid.UUID = None
    nombre: string = None

@dataclass
class CreacionAuditoriaFallida(EventoCompaniaCreada):
    id: uuid.UUID = None
    nombre: string = None
from __future__ import annotations
from dataclasses import dataclass, field
import uuid
from alpes.seedwork.dominio.eventos import (EventoDominio)

@dataclass
class ContratoCreado(EventoDominio):
    id: uuid.UUID = None
    compania: str = ""
    
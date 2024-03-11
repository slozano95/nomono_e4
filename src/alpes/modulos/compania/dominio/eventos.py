from __future__ import annotations
from dataclasses import dataclass, field
import uuid
from alpes.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class CompaniaCreada(EventoDominio):
    id: uuid.UUID = None
    
@dataclass
class CreacionCompaniaFallida(EventoDominio):
    id: uuid.UUID = None
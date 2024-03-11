from __future__ import annotations
from dataclasses import dataclass, field
import uuid
from auditoria.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class AuditoriaCreada(EventoDominio):
    id: uuid.UUID = None
    
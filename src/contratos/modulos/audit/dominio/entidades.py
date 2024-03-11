from __future__ import annotations
from dataclasses import dataclass, field
import uuid
from auditoria.seedwork.dominio.entidades import AgregacionRaiz, Entidad
from auditoria.modulos.audit.dominio.eventos import AuditoriaCreada

@dataclass
class Auditoria(AgregacionRaiz):
    id: str = ""
    nombre: str = ""

    def crear_auditoria(self, compania: Auditoria):
        self.id = compania.id
        self.nombre = compania.nombre
        self.agregar_evento(AuditoriaCreada(id=self.id))

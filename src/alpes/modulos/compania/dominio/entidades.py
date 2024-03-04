from __future__ import annotations
from dataclasses import dataclass, field
import uuid
from alpes.seedwork.dominio.entidades import AgregacionRaiz, Entidad
from alpes.modulos.compania.dominio.eventos import CompaniaCreada

@dataclass
class Compania(AgregacionRaiz):
    id: str = ""
    nombre: str = ""

    def crear_compania(self, compania: Compania):
        self.id = compania.id
        self.nombre = compania.nombre
        self.agregar_evento(CompaniaCreada(id=self.id))

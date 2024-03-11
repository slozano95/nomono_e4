from __future__ import annotations
from dataclasses import dataclass, field
import uuid
from contratos.seedwork.dominio.entidades import AgregacionRaiz, Entidad
from contratos.modulos.contratos.dominio.eventos import ContratoCreado

from contratos.modulos.contratos.aplicacion.handlers import HandlerContratoIntegracion
from contratos.modulos.contratos.infraestructura.despachadores import Despachador


@dataclass
class Contrato(AgregacionRaiz):
    id: str = ""
    nombre: str = ""
    valor: str = ""
    compania: str = ""

    def crear_contrato(self, objeto: Contrato):
        self.id = objeto.id
        self.nombre = objeto.nombre
        self.valor = objeto.valor
        self.compania = objeto.compania
        
        #self.agregar_evento(ContratoCreado(id=self.id, compania=objeto.compania))

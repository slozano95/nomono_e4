from dataclasses import dataclass, field
from alpes.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class LegDTO(DTO):
    fecha_salida: str
    fecha_llegada: str
    origen: dict
    destino: dict

@dataclass(frozen=True)
class SegmentoDTO(DTO):
    legs: list[LegDTO]

@dataclass(frozen=True)
class OdoDTO(DTO):
    segmentos: list[SegmentoDTO]

@dataclass(frozen=True)
class ItinerarioDTO(DTO):
    odos: list[OdoDTO]

@dataclass(frozen=True)
class CreacionCompaniaDTO(DTO):
    id: str = field(default_factory=str)
    nombre: str = field(default_factory=str)
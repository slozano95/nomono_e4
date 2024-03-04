from dataclasses import dataclass, field
from alpes.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class CreacionCompaniaDTO(DTO):
    id: str = field(default_factory=str)
    nombre: str = field(default_factory=str)
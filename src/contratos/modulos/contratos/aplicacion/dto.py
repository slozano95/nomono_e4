from dataclasses import dataclass, field
from contratos.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class CreacionContratoDTO(DTO):
    id: str = field(default_factory=str)
    nombre: str = field(default_factory=str)
    valor: str = field(default_factory=str)
    compania: str = field(default_factory=str)
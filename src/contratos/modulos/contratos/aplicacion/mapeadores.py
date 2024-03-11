from contratos.seedwork.aplicacion.dto import Mapeador as AppMap
from contratos.seedwork.dominio.repositorios import Mapeador as RepMap
from contratos.modulos.contratos.dominio.entidades import Contrato
from contratos.seedwork.aplicacion.dto import DTO
from contratos.modulos.contratos.infraestructura.dto import ContratoDBModel
from .dto import CreacionContratoDTO

class MapeadorCreacionContrato(AppMap):
    def externo_a_dto(self, externo: dict) -> CreacionContratoDTO:
        dto = CreacionContratoDTO(externo["id"],externo["nombre"],externo["valor"], externo["compania"])
        return dto
    
    def dto_a_externo(self, dto: DTO) -> dict:
        return dto.__dict__

class MapeadorCreacionContratoRepo(RepMap):
    
    def obtener_tipo(self) -> type:
        return Contrato.__class__

    def entidad_a_dto(self, entidad: Contrato) -> ContratoDBModel:
        data = ContratoDBModel()
        data.id = entidad.id
        data.nombre = entidad.nombre
        data.valor = entidad.valor
        return data

    def dto_a_entidad(self, dto: CreacionContratoDTO) -> Contrato:
        data = Contrato()
        data.id = dto.id
        data.nombre = dto.nombre
        data.valor = dto.valor
        return data
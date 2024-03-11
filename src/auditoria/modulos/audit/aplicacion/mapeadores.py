from auditoria.seedwork.aplicacion.dto import Mapeador as AppMap
from auditoria.seedwork.dominio.repositorios import Mapeador as RepMap
from auditoria.modulos.audit.dominio.entidades import Auditoria
from auditoria.seedwork.aplicacion.dto import DTO
from auditoria.modulos.audit.infraestructura.dto import AuditoriaDBModel
from .dto import CreacionAuditoriaDTO

class MapeadorAuditoriaContrato(AppMap):
    def externo_a_dto(self, externo: dict) -> CreacionAuditoriaDTO:
        dto = CreacionAuditoriaDTO(externo["id"],externo["nombre"],externo["valor"], externo["compania"])
        return dto
    
    def dto_a_externo(self, dto: DTO) -> dict:
        return dto.__dict__

class MapeadorCreacionAuditoriaRepo(RepMap):
    
    def obtener_tipo(self) -> type:
        return Auditoria.__class__

    def entidad_a_dto(self, entidad: Auditoria) -> AuditoriaDBModel:
        data = AuditoriaDBModel()
        data.id = entidad.id
        data.nombre = entidad.nombre
        data.valor = entidad.valor
        return data

    def dto_a_entidad(self, dto: CreacionAuditoriaDTO) -> Auditoria:
        data = Auditoria()
        data.id = dto.id
        data.nombre = dto.nombre
        data.valor = dto.valor
        return data
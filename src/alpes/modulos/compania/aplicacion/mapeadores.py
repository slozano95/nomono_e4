from alpes.seedwork.aplicacion.dto import Mapeador as AppMap
from alpes.seedwork.dominio.repositorios import Mapeador as RepMap
from alpes.modulos.compania.dominio.entidades import Compania
from alpes.seedwork.aplicacion.dto import DTO
from alpes.modulos.compania.infraestructura.dto import CompaniaModel
from alpes.modulos.contratos.aplicacion.comandos.registrar_compania import RegistrarCompania
from .dto import CreacionCompaniaDTO
from datetime import datetime

class MapeadorCreacion(AppMap):
    def externo_a_dto(self, externo: dict) -> CreacionCompaniaDTO:
        dto = CreacionCompaniaDTO(externo["id"],externo["nombre"])
        return dto
    
    def dto_a_externo(self, dto: DTO) -> dict:
        return dto.__dict__
    
    def externo_comando_a_dto(self, dto: RegistrarCompania) -> CreacionCompaniaDTO:
        dto = CreacionCompaniaDTO(dto.id, dto.nombre)
        return dto

class MapeadorCreacionRepo(RepMap):
    
    def obtener_tipo(self) -> type:
        return Compania.__class__

    def entidad_a_dto(self, entidad: Compania) -> CompaniaModel:
        data = CompaniaModel()
        data.id = entidad.id
        data.nombre = entidad.nombre
        return data

    def dto_a_entidad(self, dto: CreacionCompaniaDTO) -> Compania:
        data = Compania()
        data.id = dto.id
        data.nombre = dto.nombre
        
        return data

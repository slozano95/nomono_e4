
from alpes.config.db import db
from alpes.modulos.compania.dominio.entidades import Compania
from alpes.modulos.compania.dominio.repositorios import RepositorioCompania
from uuid import UUID
from alpes.modulos.compania.aplicacion.mapeadores import MapeadorCreacionRepo

class RepositorioCompaniasSQL(RepositorioCompania):

    def __init__(self):
        pass
        
    
    def obtener_por_id(self, id: UUID) -> Compania:
        # TODO
        raise NotImplementedError

    def obtener_todos(self) -> list[Compania]:
        return []

    def agregar(self, entity: Compania):
        dto = MapeadorCreacionRepo().entidad_a_dto(entidad=entity)
        db.session.add(dto)

    def actualizar(self, entity: Compania):
        # TODO
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        # TODO
        raise NotImplementedError
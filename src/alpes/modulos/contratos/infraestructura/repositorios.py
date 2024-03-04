from alpes.config.db import db
from alpes.modulos.contratos.dominio.entidades import Contrato
from alpes.modulos.contratos.dominio.repositorios import RepositorioContrato
from uuid import UUID
from alpes.modulos.contratos.aplicacion.mapeadores import MapeadorCreacionContratoRepo

class RepositorioContratoSQL(RepositorioContrato):

    def __init__(self):
        pass
        
    
    def obtener_por_id(self, id: UUID) -> Contrato:
        # TODO
        raise NotImplementedError

    def obtener_todos(self) -> list[Contrato]:
        return []

    def agregar(self, entity: Contrato):
        dto = MapeadorCreacionContratoRepo().entidad_a_dto(entidad=entity)
        db.session.add(dto)

    def actualizar(self, entity: Contrato):
        # TODO
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        # TODO
        raise NotImplementedError
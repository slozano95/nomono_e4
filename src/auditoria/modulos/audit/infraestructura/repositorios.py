
from auditoria.config.db import db
from auditoria.modulos.audit.dominio.entidades import Auditoria
from auditoria.modulos.audit.dominio.repositorios import RepositorioAuditoria
from uuid import UUID
from auditoria.modulos.audit.aplicacion.mapeadores import MapeadorCreacionAuditoriaRepo

class RepositorioCompaniasSQL(RepositorioAuditoria):

    def __init__(self):
        pass
        
    
    def obtener_por_id(self, id: UUID) -> Auditoria:
        # TODO
        raise NotImplementedError

    def obtener_todos(self) -> list[Auditoria]:
        return []

    def agregar(self, entity: Auditoria):
        dto = MapeadorCreacionAuditoriaRepo().entidad_a_dto(entidad=entity)
        db.session.add(dto)

    def actualizar(self, entity: Auditoria):
        # TODO
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        # TODO
        raise NotImplementedError
import uuid
from dataclasses import dataclass
from auditoria.modulos.audit.aplicacion.queries.base_query import CompaniaBaseQuery
from auditoria.modulos.audit.dominio.repositorios import RepositorioCompania
from auditoria.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado

@dataclass
class GetAuditoria(Query):
    id: str

class GetAuditoriaHandler(CompaniaBaseQuery):

    def handle(self, query: GetAuditoria) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompania.__class__)
        compania =  self.fabrica_vuelos.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorCompania())
        return QueryResultado(resultado=compania)

@QueryHandler.register(GetAuditoria)
def ejecutar_query_obtener_reserva(query: GetAuditoria):
    handler = GetAuditoriaHandler()
    return handler.handle(query)
import uuid
from dataclasses import dataclass
from contratos.modulos.contratos.aplicacion.queries.base_query import ContratoBaseQuery
from contratos.modulos.contratos.dominio.repositorios import RepositorioContrato
from contratos.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado

@dataclass
class GetContrato(Query):
    id: str

class GetContratoHandler(ContratoBaseQuery):

    def handle(self, query: GetContrato) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompania.__class__)
        compania =  self.fabrica_vuelos.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorContrato())
        return QueryResultado(resultado=compania)

@QueryHandler.register(GetContrato)
def ejecutar_query_obtener_reserva(query: GetContrato):
    handler = GetContratoHandler()
    return handler.handle(query)
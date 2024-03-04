import uuid
from dataclasses import dataclass
from nomono_e3.src.alpes.modulos.compania.aplicacion.queries.base_query import CompaniaBaseQuery
from nomono_e3.src.alpes.modulos.compania.dominio.repositorios import RepositorioCompania
from nomono_e3.src.alpes.modulos.vuelos.infraestructura.mapeadores import MapeadorReserva
from nomono_e3.src.alpes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado

@dataclass
class GetCompanias(Query):
    id: str

class GetCompaniasHandler(CompaniaBaseQuery):

    def handle(self, query: GetCompanias) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompania.__class__)
        compania =  self.fabrica_vuelos.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorReserva())
        return QueryResultado(resultado=compania)

@QueryHandler.register(GetCompanias)
def ejecutar_query_obtener_reserva(query: GetCompanias):
    handler = GetCompaniasHandler()
    return handler.handle(query)
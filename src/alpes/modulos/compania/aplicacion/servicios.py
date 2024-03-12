from alpes.modulos.compania.aplicacion.mapeadores import MapeadorCreacionRepo
from alpes.seedwork.aplicacion.servicios import Servicio
from alpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from alpes.modulos.compania.infraestructura.fabricas import FabricaCompanias, FabricaRepositorio
from alpes.modulos.compania.dominio.repositorios import RepositorioCompania
from alpes.modulos.compania.infraestructura.despachadores import Despachador
from alpes.modulos.compania.infraestructura.schema.v1.eventos import CompaniaCreadaPayload, EventoCompaniaCreada
from alpes.modulos.compania.dominio.entidades import Compania

from .dto import CreacionCompaniaDTO 
import asyncio

class ServicioCreacionCompania(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_companias: FabricaCompanias = FabricaCompanias()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_companias(self):
        return self._fabrica_companias
         
    def crear_compania(self, dto: CreacionCompaniaDTO) -> CreacionCompaniaDTO:
        data: Compania = self.fabrica_companias.crear_objeto(dto, MapeadorCreacionRepo())
        data.crear_compania(data)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompania.__class__)
        self.notificar_creacion_compania(id=dto.id)
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, data)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        return dto
    
    def notificar_creacion_compania(self, id):
        despachador = Despachador()
        dto = EventoCompaniaCreada(data=CompaniaCreadaPayload(id=id))
        #despachador.publicar_evento(dto, 'eventos-notifier')
        despachador.publicar_evento(dto, 'eventos-audit')
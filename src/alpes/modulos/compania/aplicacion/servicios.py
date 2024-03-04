from alpes.seedwork.aplicacion.servicios import Servicio
from alpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from alpes.modulos.compania.infraestructura.fabricas import FabricaCompanias, FabricaRepositorio
from alpes.modulos.compania.dominio.repositorios import RepositorioCompania
from .mapeadores import  MapeadorCreacionRepo
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

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, data)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        return dto
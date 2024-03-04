from alpes.seedwork.aplicacion.servicios import Servicio
from alpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from alpes.modulos.contratos.infraestructura.fabricas import FabricaContrato, FabricaRepositorio
from alpes.modulos.contratos.dominio.repositorios import RepositorioContrato
from alpes.modulos.contratos.dominio.entidades import Contrato
from alpes.modulos.contratos.aplicacion.mapeadores import MapeadorCreacionContratoRepo
from alpes.modulos.contratos.infraestructura.despachadores import Despachador
from .dto import CreacionContratoDTO

class ServicioCreacionContrato(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_contratos: FabricaContrato = FabricaContrato()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_contratos(self):
        return self._fabrica_contratos
         
    def crear_contrato(self, dto: CreacionContratoDTO) -> CreacionContratoDTO:
        data: Contrato = self.fabrica_contratos.crear_objeto(dto, MapeadorCreacionContratoRepo())
        data.crear_contrato(data)
        #Enviar evento a companias
        despachador = Despachador()
        print("EL DTO ESSS")
        print(dto)
        despachador.publicar_evento(dto, 'eventos-compania')
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioContrato.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, data)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        return dto
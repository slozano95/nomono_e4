from auditoria.seedwork.aplicacion.servicios import Servicio
from auditoria.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from auditoria.modulos.audit.infraestructura.fabricas import FabricaAuditoria, FabricaRepositorio
from auditoria.modulos.audit.dominio.repositorios import RepositorioAuditoria
from auditoria.modulos.audit.dominio.entidades import Auditoria
from auditoria.modulos.audit.aplicacion.mapeadores import MapeadorCreacionAuditoriaRepo
from auditoria.modulos.audit.infraestructura.despachadores import Despachador
from .dto import CreacionAuditoriaDTO

class ServicioCreacionAuditoria(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_auditoria: FabricaAuditoria = FabricaAuditoria()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_auditoria(self):
        return self._fabrica_auditoria
         
    def crear_auditoria(self, dto: CreacionAuditoriaDTO) -> CreacionAuditoriaDTO:
        data: Auditoria = self.fabrica_contratos.crear_objeto(dto, MapeadorCreacionAuditoriaRepo())
        data.crear_contrato(data)
        #Enviar evento a companias
        despachador = Despachador()
        print("EL DTO ESSS")
        print(dto)
        despachador.publicar_evento(dto, 'eventos-compania')
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioAuditoria.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, data)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        return dto
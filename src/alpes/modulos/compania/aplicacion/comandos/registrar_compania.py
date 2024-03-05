from alpes.seedwork.aplicacion.comandos import Comando, ComandoHandler
from dataclasses import dataclass, field
from alpes.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass, field
from alpes.seedwork.aplicacion.comandos import ejecutar_commando as comando
from alpes.modulos.compania.aplicacion.servicios import ServicioCreacionCompania
from alpes.modulos.compania.aplicacion.mapeadores import MapeadorCreacion

@dataclass
class RegistrarCompania(Comando):
    id: str
    nombre: str

class RegistrarCompaniaHandler(ComandoHandler):
    def handle(self, comando: Comando):
        print(comando)
        mapper = MapeadorCreacion()
        dto = mapper.externo_comando_a_dto(comando)
        sr = ServicioCreacionCompania()
        sr.notificar_creacion_compania(dto.id)
        

@comando.register(RegistrarCompania)
def ejecutar_comando_crear_reserva(comando: RegistrarCompania):
    handler = RegistrarCompaniaHandler()
    handler.handle(comando)
from dataclasses import dataclass
from alpes.seedwork.aplicacion.comandos import Comando, ComandoHandler
from nomono_e3.src.alpes.seedwork.aplicacion import comandos

@dataclass
class RegistrarCompania(Comando):
    id: str
    nombre: str

class RegistrarCompaniaHandler(ComandoHandler):
    def handle(self, comando: Comando):
        return super().handle(comando)

@comandos.register(RegistrarCompania)
def ejecutar_comando_crear_reserva(comando: RegistrarCompania):
    handler = RegistrarCompaniaHandler()
    handler.handle(comando)
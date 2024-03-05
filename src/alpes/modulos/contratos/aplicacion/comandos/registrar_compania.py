from dataclasses import dataclass
from alpes.seedwork.aplicacion.comandos import Comando, ComandoHandler
from alpes.seedwork.aplicacion import comandos
from alpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

@dataclass
class RegistrarCompania(Comando):
    id: str
    nombre: str

class RegistrarCompaniaHandler(ComandoHandler):
    def handle(self, comando: Comando):
        return super().handle(comando)

@comando.register(RegistrarCompania)
def ejecutar_comando_crear_reserva(comando: RegistrarCompania):
    handler = RegistrarCompaniaHandler()
    handler.handle(comando)
from dataclasses import dataclass
from contratos.seedwork.aplicacion.comandos import Comando, ComandoHandler
from contratos.seedwork.aplicacion import comandos
from contratos.seedwork.aplicacion.comandos import ejecutar_commando as comando

@dataclass
class RegistrarContrato(Comando):
    id: str
    nombre: str

class RegistrarContratoHandler(ComandoHandler):
    def handle(self, comando: Comando):
        return super().handle(comando)

@comando.register(RegistrarContrato)
def ejecutar_comando_crear_reserva(comando: RegistrarContrato):
    handler = RegistrarContratoHandler()
    handler.handle(comando)
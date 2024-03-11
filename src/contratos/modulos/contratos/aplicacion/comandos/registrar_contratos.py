from dataclasses import dataclass
from contratos.seedwork.aplicacion.comandos import Comando, ComandoHandler
from contratos.seedwork.aplicacion import comandos
from contratos.seedwork.aplicacion.comandos import ejecutar_commando as comando

@dataclass
class RegistrarCompania(Comando):
    id: str
    nombre: str

@dataclass
class RegistrarContrato(Comando):
    id: str
    nombre: str

class RegistrarContratoHandler(ComandoHandler):
    def handle(self, comando: Comando):
        pass

@comando.register(RegistrarContrato)
def ejecutar_comando_crear_contrato(comando: RegistrarContrato):
    handler = RegistrarContratoHandler()
    handler.handle(comando)

@dataclass
class EliminarContrato(Comando):
    id: str
    nombre: str

class EliminarContratoHandler(ComandoHandler):
    def handle(self, comando: Comando):
        pass

@comando.register(RegistrarContrato)
def ejecutar_comando_eliminar_contrato(comando: EliminarContrato):
    handler = EliminarContratoHandler()
    handler.handle(comando)
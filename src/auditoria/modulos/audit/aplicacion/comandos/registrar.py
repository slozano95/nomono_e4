from dataclasses import dataclass
from auditoria.seedwork.aplicacion.comandos import Comando, ComandoHandler
from auditoria.seedwork.aplicacion import comandos
from auditoria.seedwork.aplicacion.comandos import ejecutar_commando as comando

@dataclass
class RegistrarAuditoria(Comando):
    id: str
    nombre: str

@dataclass
class EliminarAuditoria(Comando):
    id: str

@dataclass
class RegistrarAuditoriaHandler(ComandoHandler):
    def handle(self, comando: Comando):
        pass

@dataclass
class RegistrarEliminarAuditoriaHandler(ComandoHandler):
    def handle(self, comando: Comando):
        pass


@comando.register(RegistrarAuditoria)
def ejecutar_comando_crear_reserva(comando: RegistrarAuditoria):
    handler = RegistrarAuditoriaHandler()
    handler.handle(comando)

@comando.register(EliminarAuditoria)
def ejecutar_comando_eliminar_reserva(comando: EliminarAuditoria):
    handler = RegistrarEliminarAuditoriaHandler()
    handler.handle(comando)
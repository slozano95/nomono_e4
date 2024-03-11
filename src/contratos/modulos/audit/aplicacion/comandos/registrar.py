from dataclasses import dataclass
from auditoria.seedwork.aplicacion.comandos import Comando, ComandoHandler
from auditoria.seedwork.aplicacion import comandos
from auditoria.seedwork.aplicacion.comandos import ejecutar_commando as comando

@dataclass
class RegistrarAuditoria(Comando):
    id: str
    nombre: str

class RegistrarAuditoriaHandler(ComandoHandler):
    def handle(self, comando: Comando):
        return super().handle(comando)

@comando.register(RegistrarAuditoria)
def ejecutar_comando_crear_reserva(comando: RegistrarAuditoria):
    handler = RegistrarAuditoriaHandler()
    handler.handle(comando)
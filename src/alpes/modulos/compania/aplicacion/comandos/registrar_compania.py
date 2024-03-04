from dataclasses import dataclass
from alpes.seedwork.aplicacion.comandos import Comando, ComandoHandler
from nomono_e3.src.alpes.seedwork.aplicacion import comandos

@dataclass
class RegistrarCompania(Comando):
    id: str
    nombre: str

class RegistrarCompaniaHandler(ComandoHandler):
    def handle(self, comando: Comando):
    #         reserva_dto = ReservaDTO(
    #         fecha_actualizacion=comando.fecha_actualizacion
    #     ,   fecha_creacion=comando.fecha_creacion
    #     ,   id=comando.id
    #     ,   itinerarios=comando.itinerarios)

    # reserva: Reserva = self.fabrica_vuelos.crear_objeto(reserva_dto, MapeadorReserva())
    # reserva.crear_reserva(reserva)

    # repositorio = self.fabrica_repositorio.crear_objeto(RepositorioReservas.__class__)

    # UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, reserva)
    # UnidadTrabajoPuerto.savepoint()
    # UnidadTrabajoPuerto.commit()
        return super().handle(comando)

@comandos.register(RegistrarCompania)
def ejecutar_comando_crear_reserva(comando: RegistrarCompania):
    handler = RegistrarCompaniaHandler()
    handler.handle(comando)
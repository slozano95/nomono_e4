from alpes.modulos.compania.aplicacion.comandos.registrar_compania import EliminarCompania, RegistrarCompania
from alpes.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from alpes.seedwork.aplicacion.comandos import Comando
from alpes.seedwork.dominio.eventos import EventoDominio

from alpes.modulos.sagas.aplicacion.comandos.cliente import RegistrarUsuario, ValidarUsuario
from alpes.modulos.sagas.aplicacion.comandos.pagos import PagarReserva, RevertirPago
from alpes.modulos.sagas.aplicacion.comandos.gds import ConfirmarReserva, RevertirConfirmacion
from alpes.modulos.sagas.dominio.eventos.contrato import AuditoriaCreada, CompaniaCreada, CreacionAuditoriaFallida
from alpes.modulos.compania.dominio.eventos import CompaniaCreada, CreacionCompaniaFallida
from auditoria.modulos.audit.aplicacion.comandos.registrar import EliminarAuditoria, RegistrarAuditoria
from contratos.modulos.contratos.aplicacion.comandos.registrar_contratos import EliminarContrato, RegistrarContrato
from contratos.modulos.contratos.dominio.eventos import ContratoCreado, CreacionContratoFallida

class CoordinadorReservas(CoordinadorOrquestacion):

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=RegistrarCompania, evento=CompaniaCreada, error=CreacionCompaniaFallida, compensacion=EliminarCompania),
            Transaccion(index=2, comando=RegistrarAuditoria, evento=AuditoriaCreada , error=CreacionAuditoriaFallida, compensacion=EliminarAuditoria),
            Transaccion(index=3, comando=RegistrarContrato, evento=ContratoCreado, error=CreacionContratoFallida, compensacion=EliminarContrato),
            Fin(index=4)
        ]

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])
    
    def terminar(self):
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        print(mensaje)

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        ...


# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
def oir_mensaje(mensaje):
    if isinstance(mensaje, EventoDominio):
        coordinador = CoordinadorReservas()
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")
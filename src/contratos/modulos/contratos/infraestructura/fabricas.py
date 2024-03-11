from contratos.seedwork.dominio.repositorios import Mapeador, Repositorio
from contratos.seedwork.dominio.fabricas import Fabrica
from contratos.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass
from contratos.seedwork.dominio.fabricas import Fabrica
from contratos.seedwork.dominio.repositorios import Repositorio
from contratos.modulos.contratos.infraestructura.repositorios import RepositorioContratoSQL

@dataclass
class FabricaContrato(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        compania = mapeador.dto_a_entidad(obj)
        return compania

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        return RepositorioContratoSQL()
        
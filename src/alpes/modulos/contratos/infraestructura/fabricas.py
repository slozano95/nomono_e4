from alpes.seedwork.dominio.repositorios import Mapeador, Repositorio
from alpes.seedwork.dominio.fabricas import Fabrica
from alpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass
from alpes.seedwork.dominio.fabricas import Fabrica
from alpes.seedwork.dominio.repositorios import Repositorio
from alpes.modulos.contratos.infraestructura.repositorios import RepositorioContratoSQL

@dataclass
class FabricaContrato(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        compania = mapeador.dto_a_entidad(obj)
        return compania

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        return RepositorioContratoSQL()
        
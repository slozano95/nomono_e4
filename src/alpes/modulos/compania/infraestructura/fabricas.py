from alpes.seedwork.dominio.repositorios import Mapeador, Repositorio
from alpes.seedwork.dominio.fabricas import Fabrica
from alpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass
        
@dataclass
class FabricaCompanias(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        compania = mapeador.dto_a_entidad(obj)
        return compania


from dataclasses import dataclass, field
from alpes.seedwork.dominio.fabricas import Fabrica
from alpes.seedwork.dominio.repositorios import Repositorio
from alpes.modulos.compania.infraestructura.repositorios import RepositorioCompaniasSQL


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        return RepositorioCompaniasSQL()
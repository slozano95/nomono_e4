from dataclasses import dataclass, field
from auditoria.seedwork.dominio.repositorios import Mapeador, Repositorio
from auditoria.seedwork.dominio.fabricas import Fabrica
from auditoria.seedwork.dominio.repositorios import Repositorio
from auditoria.modulos.audit.infraestructura.repositorios import RepositorioCompaniasSQL

@dataclass
class FabricaAuditoria(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        compania = mapeador.dto_a_entidad(obj)
        return compania

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        return RepositorioCompaniasSQL()
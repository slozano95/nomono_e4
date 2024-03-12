import strawberry
import typing

from strawberry.types import Info
from bff import utils
from bff.despachadores import Despachador

from .esquemas import *

@strawberry.type
class Mutation:

    @strawberry.mutation
    async def crear(self, id: str, nombre: str, info: Info) -> RtaBFF:
        payload = dict(
            id = id,
            nombre = nombre
        )
        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoCrearCompania",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF",
            data = payload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "comando-crear-compania", "public/default/comando-crear-compania")
        
        return RtaBFF(mensaje="Procesando Mensaje", codigo=203)
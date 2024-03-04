from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Compania(_message.Message):
    __slots__ = ["id", "nombre"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NOMBRE_FIELD_NUMBER: _ClassVar[int]
    id: str
    nombre: str
    def __init__(self, id: _Optional[str] = ..., nombre: _Optional[str] = ...) -> None: ...

class RespuestaCompania(_message.Message):
    __slots__ = ["compania", "mensaje"]
    COMPANIA_FIELD_NUMBER: _ClassVar[int]
    MENSAJE_FIELD_NUMBER: _ClassVar[int]
    compania: Compania
    mensaje: str
    def __init__(self, mensaje: _Optional[str] = ..., compania: _Optional[_Union[Compania, _Mapping]] = ...) -> None: ...

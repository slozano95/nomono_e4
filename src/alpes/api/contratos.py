import json
import alpes.seedwork.presentacion.api as api
from flask import request
from flask import Response
from alpes.modulos.contratos.aplicacion.mapeadores import MapeadorCreacionContrato
from alpes.modulos.contratos.aplicacion.servicios import ServicioCreacionContrato
from alpes.seedwork.dominio.excepciones import ExcepcionDominio

bp = api.crear_blueprint('contratos', '/contratos')
@bp.route('/crear', methods=('POST',))
def crear():
    try:
        dict = request.json
        mapper = MapeadorCreacionContrato()
        dto = mapper.externo_a_dto(dict)
        sr = ServicioCreacionContrato()
        dto_final = sr.crear_contrato(dto)
        return mapper.dto_a_externo(dto_final)
    
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

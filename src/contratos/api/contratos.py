import json
import auditoria.seedwork.presentacion.api as api
from flask import redirect, render_template, request, session, url_for
from flask import Response
from contratos.modulos.contratos.aplicacion.mapeadores import MapeadorCreacionContrato
from contratos.modulos.contratos.aplicacion.servicios import ServicioCreacionContrato
from contratos.seedwork.dominio.excepciones import ExcepcionDominio

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

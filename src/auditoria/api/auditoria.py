import json
import auditoria.seedwork.presentacion.api as api
from flask import redirect, render_template, request, session, url_for
from flask import Response
from auditoria.modulos.audit.aplicacion.mapeadores import MapeadorAuditoriaContrato
from auditoria.modulos.audit.aplicacion.servicios import ServicioCreacionAuditoria
from auditoria.seedwork.dominio.excepciones import ExcepcionDominio

bp = api.crear_blueprint('auditoria', '/auditoria')
@bp.route('/crear', methods=('POST',))
def crear():
    try:
        dict = request.json

        mapper = MapeadorAuditoriaContrato()
        dto = mapper.externo_a_dto(dict)
        sr = ServicioCreacionAuditoria()
        dto_final = sr.crear_auditoria(dto)
        return mapper.dto_a_externo(dto_final)
    
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

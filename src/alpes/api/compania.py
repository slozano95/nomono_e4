import json
import alpes.seedwork.presentacion.api as api
from flask import redirect, render_template, request, session, url_for
from flask import Response
from alpes.modulos.compania.aplicacion.mapeadores import MapeadorCreacion
from alpes.modulos.compania.aplicacion.servicios import ServicioCreacionCompania
from alpes.seedwork.dominio.excepciones import ExcepcionDominio

bp = api.crear_blueprint('compania', '/compania')
@bp.route('/crear', methods=('POST',))
def crear():
    try:
        dict = request.json

        mapper = MapeadorCreacion()
        dto = mapper.externo_a_dto(dict)
        sr = ServicioCreacionCompania()
        dto_final = sr.crear_compania(dto)
        return mapper.dto_a_externo(dto_final)
    
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

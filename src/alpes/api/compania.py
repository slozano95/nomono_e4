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

@bp.route('/reserva-comando', methods=('POST',))
def reservar_asincrona():
    try:
        reserva_dict = request.json

        map_reserva = MapeadorReservaDTOJson()
        reserva_dto = map_reserva.externo_a_dto(reserva_dict)

        comando = CrearReserva(reserva_dto.fecha_creacion, reserva_dto.fecha_actualizacion, reserva_dto.id, reserva_dto.itinerarios)
        
        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        ejecutar_commando(comando)
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/reserva', methods=('GET',))
@bp.route('/reserva/<id>', methods=('GET',))
def dar_reserva(id=None):
    if id:
        sr = ServicioReserva()
        map_reserva = MapeadorReservaDTOJson()
        
        return map_reserva.dto_a_externo(sr.obtener_reserva_por_id(id))
    else:
        return [{'message': 'GET!'}]

@bp.route('/reserva-query', methods=('GET',))
@bp.route('/reserva-query/<id>', methods=('GET',))
def dar_reserva_usando_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerReserva(id))
        map_reserva = MapeadorReservaDTOJson()
        
        return map_reserva.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]
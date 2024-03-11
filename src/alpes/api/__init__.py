import os

from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from flask_swagger import swagger

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def registrar_handlers():
    pass
    

def importar_modelos_alchemy():
    
    import alpes.modulos.compania.infraestructura.dto

def comenzar_consumidor():

    import threading    
    import alpes.modulos.compania.infraestructura.consumidores as compania
    threading.Thread(target=compania.suscribirse_a_eventos).start()
    threading.Thread(target=compania.suscribirse_a_comandos).start()
    import alpes.modulos.notifier.infraestructura.consumidores as notifier
    threading.Thread(target=notifier.suscribirse_a_eventos).start()
    # import alpes.modulos.audit.infraestructura.consumidores as audit
    # threading.Thread(target=audit.suscribirse_a_eventos).start()

def create_app(configuracion={}):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)
    
    app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'database.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING')

     # Inicializa la DB
    from alpes.config.db import init_db
    init_db(app)

    from alpes.config.db import db

    importar_modelos_alchemy()
    registrar_handlers()

    with app.app_context():
        db.create_all()
        if not app.config.get('TESTING'):
            comenzar_consumidor()

     # Importa Blueprints
    from . import compania
    from . import contratos

    # Registro de Blueprints
    app.register_blueprint(compania.bp)
    app.register_blueprint(contratos.bp)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "My API"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app

"""DTOs para la capa de infrastructura del dominio

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio

"""

from auditoria.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

class AuditoriaDBModel(db.Model):
    __tablename__ = "auditoria"
    id = db.Column(db.String, primary_key=True)
    nombre = db.Column(db.String, nullable=False, primary_key=False)

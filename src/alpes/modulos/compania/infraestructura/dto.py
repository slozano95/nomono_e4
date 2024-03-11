from alpes.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

class CompaniaModel(db.Model):
    __tablename__ = "compania"
    id = db.Column(db.String, primary_key=True)
    nombre = db.Column(db.String, nullable=False, primary_key=False)

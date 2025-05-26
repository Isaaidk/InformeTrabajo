# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Informe(db.Model):
    __tablename__ = 'INFORME'
    INFORME_ID = db.Column(db.Integer, primary_key=True)
    Numero_Ticket = db.Column(db.Integer)
    FECHA = db.Column(db.Date)
    NOMBRE_CLIENTE = db.Column(db.String(50))
    USURIO_INFORME = db.Column(db.String(100))
    DEPARTAMENTO_ID = db.Column(db.Integer)
    EXTENCION = db.Column(db.Integer)
    TIPO_EQUIPO = db.Column(db.Integer)
    TIPO_MARCA = db.Column(db.Integer)
    MODELO = db.Column(db.String(100))
    CODIGO_UDLA = db.Column(db.Integer, unique=True)
    SERIE = db.Column(db.String(100), unique=True)
    GARANTIA = db.Column(db.Integer)
    DESCRIPCION_PROBLEMA = db.Column(db.Text)
    DIAGNOSTICO = db.Column(db.Text)
    RECOMENDACIÓN = db.Column(db.Text)
    ESTADO = db.Column(db.Integer)
    PERSONA_REVICION = db.Column(db.String(100))

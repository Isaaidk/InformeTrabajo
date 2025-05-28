# routes.py
from flask import render_template
from models import Marca, Modelo, Garantia

def setup_routes(app):
    @app.route('/formulario')
    def formulario():
        marcas = Marca.query.all()
        modelos = Modelo.query.all()
        garantias = Garantia.query.all()
        return render_template('formulario.html', marcas=marcas, modelos=modelos, garantias=garantias)
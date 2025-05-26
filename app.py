# app.py
from flask import Flask, render_template, request, redirect
from config import CONNECTION_STRING
from models import db, Informe
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = CONNECTION_STRING
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    informes = Informe.query.all()
    return render_template('index.html', informes=informes)

@app.route('/agregar', methods=['POST'])
def agregar():
    informe = Informe(
        Numero_Ticket=request.form['ticket'],
        FECHA=datetime.strptime(request.form['fecha'], '%Y-%m-%d'),
        NOMBRE_CLIENTE=request.form['cliente'],
        USURIO_INFORME=request.form['usuario'],
        DEPARTAMENTO_ID=request.form['departamento'],
        EXTENCION=request.form['extencion'],
        TIPO_EQUIPO=request.form['tipo_equipo'],
        TIPO_MARCA=request.form['marca'],
        MODELO=request.form['modelo'],
        CODIGO_UDLA=request.form['codigo_udla'],
        SERIE=request.form['serie'],
        GARANTIA=request.form['garantia'],
        DESCRIPCION_PROBLEMA=request.form['problema'],
        DIAGNOSTICO=request.form['diagnostico'],
        RECOMENDACIÓN=request.form['recomendacion'],
        ESTADO=request.form['estado'],
        PERSONA_REVICION=request.form['persona']
    )
    db.session.add(informe)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

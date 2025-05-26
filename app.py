from flask import Flask, render_template, request, redirect, url_for, session, flash
import pyodbc

app = Flask(__name__)
app.secret_key = 'clave_secreta_segura'

# Conexión a SQL Server
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=SoporteTecnico;Trusted_Connection=yes')
cursor = conn.cursor()

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        tipo_usuario = request.form.get('tipo_usuario', 2)  # Por defecto Regular

        try:
            cursor.execute(
                "INSERT INTO USERS (CORREO_USUARIO, Contraseña, Tipo_Usuario) VALUES (?, ?, ?)",
                (correo, contraseña, tipo_usuario)
            )
            conn.commit()
            flash('Usuario creado exitosamente')
            return redirect(url_for('login'))
        except Exception as e:
            flash(f'Error al crear usuario: {e}')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        password = request.form['password']

        cursor.execute("SELECT * FROM USERS WHERE CORREO_USUARIO = ? AND Contraseña = ?", correo, password)
        user = cursor.fetchone()

        if user:
            session['correo'] = correo
            return redirect(url_for('dashboard'))
        else:
            flash('Credenciales inválidas')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'correo' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', correo=session['correo'])

@app.route('/logout')
def logout():
    session.pop('correo', None)
    flash('Sesión cerrada correctamente')
    return redirect(url_for('login'))
@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if 'correo' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        try:
            ticket = request.form['ticket']
            fecha = request.form['fecha']
            cliente = request.form['cliente']
            usuario = request.form['usuario']
            departamento = request.form['departamento']
            extencion = request.form.get('extencion') or None
            tipo_equipo = request.form['tipo_equipo']
            marca = request.form['marca']
            modelo = request.form['modelo']
            codigo_udla = request.form['codigo_udla']
            serie = request.form['serie']
            garantia = request.form['garantia']
            problema = request.form['problema']
            diagnostico = request.form['diagnostico']
            recomendacion = request.form['recomendacion']
            estado = request.form['estado']
            persona = request.form['persona']

            cursor.execute("""
                INSERT INTO INFORME 
                (Numero_Ticket, FECHA, NOMBRE_CLIENTE, USURIO_INFORME, DEPARTAMENTO_ID, EXTENCION,
                 TIPO_EQUIPO, TIPO_MARCA, MODELO, CODIGO_UDLA, SERIE,
                 GARANTIA, DESCRIPCION_PROBLEMA, DIAGNOSTICO, RECOMENDACIÓN,
                 ESTADO, PERSONA_REVICION)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                ticket, fecha, cliente, usuario, departamento, extencion,
                tipo_equipo, marca, modelo, codigo_udla, serie,
                garantia, problema, diagnostico, recomendacion,
                estado, persona
            ))
            conn.commit()
            flash('Informe agregado correctamente', 'success')
        except Exception as e:
            flash(f'Error al agregar informe: {e}', 'danger')
        return redirect(url_for('agregar'))

    # GET: Cargar datos para los selects y listar informes
    cursor.execute("SELECT * FROM DEPARTAMENTO")
    departamentos = cursor.fetchall()

    cursor.execute("SELECT * FROM TIPO_EQUIPO")
    equipos = cursor.fetchall()

    cursor.execute("SELECT * FROM TIPO_MARCA")
    marcas = cursor.fetchall()

    cursor.execute("SELECT * FROM GARANTIA")
    garantias = cursor.fetchall()

    cursor.execute("SELECT * FROM ESTADO")
    estados = cursor.fetchall()

    cursor.execute("SELECT * FROM USERS")
    usuarios = cursor.fetchall()

    cursor.execute("SELECT * FROM INFORME")
    informes = cursor.fetchall()

    return render_template('index.html',
                           departamentos=departamentos,
                           equipos=equipos,
                           marcas=marcas,
                           garantias=garantias,
                           estados=estados,
                           usuarios=usuarios,
                           informes=informes,
                           correo_usuario=session['correo'])

if __name__ == '__main__':
    app.run(debug=True)

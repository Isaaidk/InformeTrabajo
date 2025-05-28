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
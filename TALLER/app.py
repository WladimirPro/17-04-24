from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL

app = Flask (__name__)

#conecion a BD
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'Usuarios'         
mysql = MySQL(app)

app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    return render_template('menu.html')


@app.route('/registro')
def registro():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contactos')
    data = cur.fetchall()
    return render_template('registroU.html',contactos = data )

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        nombrecompleto = request.form['nombrecompleto']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contactos (nombrecompleto, phone, email) VALUES(%s, %s, %s)',
                    (nombrecompleto, phone, email))
        mysql.connection.commit()
        flash('Contacto agregado exitosamente')
        return redirect(url_for('registro'))


@app.route('/edit/<id>') 
def edit_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contactos WHERE id = %s',(id,))
    data = cur.fetchall()
    return render_template('editarU.html',contact = data[0])

@app.route('/update/<id>', methods = ['POST'])
def up_contact(id):
    if request.method == 'POST':
        nombrecompleto = request.form['nombrecompleto']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Contactos 
            SET NombreCompleto = %s,
                Phone = %s,
                Email = %s
            WHERE id = %s
        """, (nombrecompleto, phone, email, id))
        mysql.connection.commit()
        flash('Contacto actualizado correctamente')
        return redirect(url_for('registro'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contactos where id = {0}'.format(id))
    mysql.connection.commit()
    flash('contacto eliminado')
    return redirect(url_for('registro'))

#xdxdxdxdxdxdxdxdxdxdxdxdxdxdxddxdxdxddxdxdxdxdxdxdxxddxdxdxdxdxxddxdxdxdxdxdxdxdxdxdxdxdxdxdxdxdxdxdxdxdxdxxddxdxdxdxdxdx


@app.route('/registrodepartamento')
def registrodepartamento():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM departamentos')
    data1 = cur.fetchall()
    return render_template('departamento.html',departamentos = data1 )

@app.route('/add_departamento', methods=['POST'])
def add_departamento():
    if request.method == 'POST':
        descripcion = request.form['descripcion']
        nrohabitacion = request.form['nrohabitacion']
        ubicacion = request.form['ubicacion']
        piso = request.form['piso']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO departamentos (descripcion, nrohabitacion, ubicacion, piso) VALUES(%s, %s, %s,%s)',
                    (descripcion, nrohabitacion, ubicacion, piso))
        mysql.connection.commit()
        flash('departamento agregado exitosamente')
        return redirect(url_for('registrodepartamento'))


@app.route('/editdepartamento/<id>') 
def edit_departamento(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM departamentos WHERE id = %s',(id,))
    data1 = cur.fetchall()
    return render_template('editarD.html',departamento = data1[0])

@app.route('/updatedepartamento/<id>', methods = ['POST'])
def up_departamento(id):
    if request.method == 'POST':
        descripcion = request.form['descripcion']
        nrohabitacion = request.form['nrohabitacion']
        ubicacion = request.form['ubicacion']
        piso = request.form['piso']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE departamentos 
            SET descripcion = %s,
                nrohabitacion = %s,
                ubicacion = %s,
                piso = %s
            WHERE id = %s
        """, (descripcion, nrohabitacion, ubicacion, piso, id))
        mysql.connection.commit()
        flash('departamento actualizado correctamente')
        return redirect(url_for('registrodepartamento'))

@app.route('/deletedepartamento/<string:id>')
def delete_departamento(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM departamentos where id = {0}'.format(id))
    mysql.connection.commit()
    flash('departamento eliminado')
    return redirect(url_for('registrodepartamento'))


if __name__ == '__main__':
    app.run(port=3000,debug=True)
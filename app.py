from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Estructura de datos para almacenar las habitaciones
habitaciones = {
    '101': {'nombre': '', 'reservada': False},
    '102': {'nombre': '', 'reservada': False},
    '103': {'nombre': '', 'reservada': False},
    # Agrega más habitaciones según sea necesario
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reserve', methods=['POST'])
def reserve():
    nombre = request.form['name']
    habitacion = request.form['room']
    if habitacion in habitaciones and not habitaciones[habitacion]['reservada']:
        habitaciones[habitacion]['nombre'] = nombre
        habitaciones[habitacion]['reservada'] = True
    return redirect(url_for('index'))

@app.route('/habitaciones')
def ver_habitaciones():
    return render_template('habitaciones.html', habitaciones=habitaciones)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
from flask import Flask, request, render_template

app = Flask(__name__, template_folder="templates")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        #crear una validación dentro del codigo para evitar errores
        if not all(10 <= nota <= 70 for nota in [nota1, nota2, nota3]) or not (0 <= asistencia <= 100):
            return "Los valores ingresados están fuera del rango. reingresa."
        #operacion aritmetica de promedio
        promedio = (nota1 + nota2 + nota3) / 3
        #resultado de la operación entre notas y asistencia
        estado = "Aprobado" if promedio >= 40 and asistencia >= 75 else "Reprobado"
        return render_template('ejercicio1.html', promedio=promedio, estado=estado)

    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']
        # Encontrar el nombre con mayor cantidad de caracteres y su longitud
        nombres = [(nombre, len(nombre)) for nombre in [nombre1, nombre2, nombre3]]
        nombre_mas_largo, caracteres_mas_largos = max(nombres, key=lambda x: x[1])
        return render_template('ejercicio2.html', nombre_mas_largo=nombre_mas_largo,
                               caracteres_mas_largos=caracteres_mas_largos)

    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run()

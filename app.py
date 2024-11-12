from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def calculoPromedio(uno, dos, tres):
    suma = uno + dos + tres
    promedio = suma / 3
    return promedio


def calculoNombreMasLargo(array):
    nombreLargo = ''
    for item in array:
        if len(item) > len(nombreLargo):
            nombreLargo = item
    return nombreLargo


@app.route('/ejercicioUno', methods=['GET', 'POST'])
def ejercicioUno():
    if request.method == 'POST':
        # Procesar los datos del formulario
        notaUno = request.form['notaUno']
        notaDos = request.form['notaDos']
        notaTres = request.form['notaTres']
        asistencia = request.form['asistencia']

        promedioNotas = calculoPromedio(float(notaUno), float(notaDos), float(notaTres))

        if promedioNotas >= 40 and int(asistencia) >= 75:
            mensaje = f'APROBADO, promedio de notas es: {promedioNotas}.'
            return render_template('ejercicioUno.html', mensaje=mensaje)
        else:
            mensaje = f'REPROBADO.'
            return render_template('ejercicioUno.html', mensaje=mensaje)

    return render_template('ejercicioUno.html')


@app.route('/ejercicioDos', methods=['GET', 'POST'])
def ejercicioDos():
    if request.method == 'POST':
        # Procesar los datos del formulario
        nombreUno = request.form['nombreUno']
        nombreDos = request.form['nombreDos']
        nombreTres = request.form['nombreTres']

        arrayNombres = []
        arrayNombres.append(nombreUno)
        arrayNombres.append(nombreDos)
        arrayNombres.append(nombreTres)

        nombreFinal = calculoNombreMasLargo(arrayNombres)

        mensaje = f'El nombre más largo es {nombreFinal} y tiene {len(nombreFinal)} caracteres.'
        return render_template('ejercicioDos.html', mensaje=mensaje)

    return render_template('ejercicioDos.html')


if __name__ == '__main__':
    app.run()

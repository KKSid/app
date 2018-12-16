import math
from flask import Flask, render_template, request,make_response

app = Flask(__name__)


@app.route('/')
def index():
    VX1 = request.cookies.get('X1')
    VX2 = request.cookies.get('X2')
    Guardada = request.cookies.get('Guardada')
    print(Guardada)
    if Guardada == "si":
        return  '<h4>Se Obtuvo de cookies </h4>'+'<h4>Valor de X1 </h4>'+ VX1+'<h4>Valor de X2 </h4>'+ VX2
    else:
        return render_template("index.html")


@app.route('/calcular', methods = ['POST', 'GET'])
def calcular():
    if request.method == 'POST':
       Guardada = ''
       VA = int(request.form['A'])
       VB = int(request.form ['B'])
       VC = int(request.form['C'])
       X1 = (-VB + (math.sqrt((VB ** 2) - (4 * VA * VC)))) / (2 * VA)
       X2 = (-VB - (math.sqrt((VB ** 2) - (4 * VA * VC)))) / (2 * VA)
       calcular = make_response(render_template('resultado.html', X1 = X1, X2 = X2))

       calcular.set_cookie('X1', str(X1))
       calcular.set_cookie('X2', str(X2))
       calcular.set_cookie('Guardada', 'si')

       return calcular


if __name__ == '__main__':
    app.run(debug=False)

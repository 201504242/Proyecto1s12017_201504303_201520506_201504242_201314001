import matriz
from flask import Flask, request, Response
app = Flask("SERVIDOR")

MATRIZ = matriz.Matriz()

@app.route("/")
def hi():
	return "hola"

#----------------------------Matriz
@app.route("/insertarMatriz",methods=['POST'])
def insertarMatriz():
	empresa= str(request.form['empresa'])
	departamento= str(request.form['departamento'])
	nombre = str(request.form['nombre'])
	MATRIZ.Insertar(empresa,departamento,nombre)
	MATRIZ.report()

if __name__ == "__main__":
  app.run()
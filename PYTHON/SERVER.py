import matriz
from flask import Flask, request, Response
app = Flask("SERVIDOR")

MATRIZ = matriz.Matriz()

@app.route("/")
def hi():
	return "hola"

#----------------------------Matriz
#insertar nuevo usuario
@app.route("/insertarMatriz",methods=['POST'])
def insertarMatriz():
	empresa= str(request.form['empresa'])
	departamento= str(request.form['departamento'])
	nombre = str(request.form['nombre'])
	MATRIZ.Insertar(empresa,departamento,nombre)
	MATRIZ.report()

#login
@app.route("/login",methods=['POST'])
def login():
	empresa= str(request.form['empresa'])
	departamento= str(request.form['departamento'])
	usuario= str(request.form['usuario'])
	password = str(request.form['password'])
	if MATRIZ.login(empresa,departamento,usuario,password)!=None:
		return True
	return False

#insertar nuevo activo
@app.route("/insertarActivo",methods=['POST'])
def insertarActivo():
	empresa= str(request.form['empresa'])
	departamento= str(request.form['departamento'])
	usuario = str(request.form['usuario'])
	nombreActivo = str(request.form['nombreActivo'])
	descripcionActivo = str(request.form['descripcionActivo'])
	idActivo = str(request.form['idActivo'])
	MATRIZ.insertarActivo(empresa,departamento,usuario,nombreActivo,descripcionActivo,idActivo)

#modificar activo
@app.route("/modificarActivo",methods=['POST'])
def modificarActivo():
	empresa= str(request.form['empresa'])
	departamento= str(request.form['departamento'])
	usuario = str(request.form['usuario'])
	idActivo = str(request.form['idActivo'])
	nombre = str(request.form['nombre'])
	descripcion = str(request.form['descripcion'])
	MATRIZ.modificarActivo(empresa,departamento,usuario,idActivo,nombre,descripcion)
	#MATRIZ.report()

#Obtener Activo
@app.route("/obtenerActivo",methods=['POST'])
def obtenerActivo():
	empresa= str(request.form['empresa'])
	departamento= str(request.form['departamento'])
	usuario = str(request.form['usuario'])
	idActivo = str(request.form['idActivo'])
	return MATRIZ.obtenerActivo(empresa,departamento,usuario,idActivo)

if __name__ == "__main__":
  app.run()
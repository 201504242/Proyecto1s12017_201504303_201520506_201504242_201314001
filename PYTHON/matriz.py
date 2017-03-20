import os
class Nodo(object):
	"""docstring for Nodo"""
	def __init__(self,empresa,departamento,nombre):
		super(Nodo, self).__init__()
		self.empresa = empresa
		self.departamento = departamento
		self.nombre = nombre
		self.x = 0
		self.y = 0
		self.derecha = None
		self.izquierda = None
		self.arriba = None
		self.abajo = None

class Matriz(object):
	"""docstring for Matriz"""
	def __init__(self):
		super(Matriz, self).__init__()
		self.primero = Nodo("","","")
		self.lengthX = 0
		self.lengthY = 0
#----------------------------------------------Metodo Insertar
	def Insertar(self,empresa,departamento,nombre):
		nuevo = Nodo(empresa,departamento,nombre)
		#Comprobamos si esta vacia la matriz
		if self.primero.derecha == None:
			self.lengthX += 1
			self.lengthY += 1
			self.amplicarCabeceras()
			self.ampliarColumna()
			self.ampliarFila()
			self.getNodo(1,1).nombre = nombre
			self.getNodo(1,0).empresa = empresa
			self.getNodo(0,1).departamento = departamento
		else:
			if self.empresaExistente(empresa) == None :
				if self.departamentoExistente(departamento) == None:
					self.lengthX += 1
					self.lengthY += 1
					self.amplicarCabeceras()
					self.ampliarColumna()
					self.ampliarFila()
					nodo = self.getNodo(self.lengthX,self.lengthY)
					nodo.nombre = nombre
					self.getNodo(self.lengthX,0).empresa = empresa
					self.getNodo(0,self.lengthY).departamento = departamento
#----------------------------------------------Metodo para Reporte
	def report(self):
		matrizdot = open("matriz.dot","w")
		auxiliar = self.primero
		cadena = "rankdir=TB; \n node [shape=box];\n node [style=filled]; \n node [fillcolor=\"#31CEF0\"];\n node [color=\"#31CEF0\"];\n edge [color=\"#31CEF0\"];"
		apuntadores = ""
		rank =""
		rangoY = self.lengthY+1
		rangoX = self.lengthX+1
		for y in range(0,rangoY):
			rank = rank + "\n {rank=same"
			for x in range(0,rangoX):
				auxiliar = self.getNodo(x,y)
				posicion = str(auxiliar.x) + str(auxiliar.y)
				rank = rank + "\""+posicion+"\";"
				if x==0:
					cadena = cadena +"\n"+ str(auxiliar.x) + str(auxiliar.y) + "[label = \""+str(auxiliar.departamento)+"\"] ;"
				elif y==0:
					cadena = cadena +"\n"+ str(auxiliar.x) + str(auxiliar.y) + "[label = \""+str(auxiliar.empresa)+"\"] ;"
				else:
					cadena = cadena +"\n"+ str(auxiliar.x) + str(auxiliar.y) + "[label = \""+str(auxiliar.nombre)+"\"] ;"
				if auxiliar.derecha != None:
					apuntadores = apuntadores + "\n" + str(auxiliar.x) + str(auxiliar.y) + " -> " +str(auxiliar.derecha.x) + str(auxiliar.derecha.y) +  ";"
				if auxiliar.arriba != None:
					apuntadores = apuntadores + "\n" + str(auxiliar.x) + str(auxiliar.y) +" -> " +str(auxiliar.arriba.x) + str(auxiliar.arriba.y) + ";"
				if auxiliar.abajo != None:
					apuntadores = apuntadores + "\n" + str(auxiliar.x) + str(auxiliar.y) +" -> " +str(auxiliar.abajo.x) + str(auxiliar.abajo.y) + ";"
				if auxiliar.izquierda != None:
					apuntadores = apuntadores + "\n" + str(auxiliar.x) + str(auxiliar.y) +" -> " +str(auxiliar.izquierda.x) + str(auxiliar.izquierda.y) + ";"
			rank = rank + "}"

		matrizdot.write("digraph G { \n" + cadena + "\n" + apuntadores + "\n"+rank+" }")
		matrizdot.close()
		os.system("Matriz.bat")					
#----------------------------------------------Metodos de busqueda
	def empresaExistente(self,empresa):
		auxiliar = self.primero
		while auxiliar != None:
			if str(auxiliar.empresa) == str(empresa):
				return auxiliar
			auxiliar = auxiliar.derecha
		return None

	def departamentoExistente(self,departamento):
		auxiliar = self.primero
		while auxiliar != None:
			if str(auxiliar.departamento) == str(departamento):
				return auxiliar
			auxiliar = auxiliar.abajo
		return None
#----------------------------------------------Metodos de Ampliacion
	def amplicarCabeceras(self):
		auxiliar = self.primero
		x = 0
		while auxiliar!=None and (x < self.lengthX):
			if auxiliar.derecha == None:
				nuevo = Nodo("","","")
				nuevo.x=self.lengthX
				nuevo.y=0
				self.pointers(nuevo)
			auxiliar = auxiliar.derecha
			x += 1

		auxiliar = self.primero
		y = 0
		while auxiliar!=None and (y<self.lengthY) :
			if auxiliar.abajo == None:
				nuevo = Nodo("","","")
				nuevo.x=0
				nuevo.y=self.lengthY
				self.pointers(nuevo)
			auxiliar = auxiliar.abajo
			y += 1

	#Se debe ampliar el length antes de ingresar ya sea lengthX o lengthY
	def ampliarColumna(self):
		cabecera = self.getNodo(self.lengthX,0)
		y = 1
		while y <= self.lengthY:
			nuevo=Nodo("","","")
			nuevo.x = self.lengthX
			nuevo.y = y
			self.pointers(nuevo)
			y += 1

	def ampliarFila(self):
		cabecera = self.getNodo(0,self.lengthY)
		x = 1
		while x <= self.lengthX:
			nuevo=Nodo("","","")
			nuevo.x = x
			nuevo.y = self.lengthY
			self.pointers(nuevo)
			x += 1
#----------------------------------------------Metodo getNodo
	def getNodo(self,col,fila):
		aux = self.primero
		while aux != None:
			if str(aux.x) == str(col):
				aux2 = aux
				while aux2 != None:
					if str(aux2.y) == str(fila):
						return aux2
					aux2 = aux2.abajo
			aux = aux.derecha
		return None
#----------------------------------------------Punteros
	def pointers(self,nuevo):
		left = self.getNodo( (int(nuevo.x) - 1), nuevo.y)
		rigth = self.getNodo((int(nuevo.x) + 1), nuevo.y)
		up = self.getNodo( nuevo.x,int(nuevo.y) - 1)
		down = self.getNodo( nuevo.x,int(nuevo.y) +1)
		
		nuevo.izquierda = left
		nuevo.derecha = rigth
		nuevo.arriba = up
		nuevo.abajo = down

		if down != None:
			down.arriba = nuevo
		if up != None:
			up.abajo = nuevo
		if left != None:
			left.derecha = nuevo
		if rigth != None:
			rigth.izquierda = nuevo
m = Matriz()
m.Insertar("glorsys","conta","lucas")
m.Insertar("ofert","ope","marcos")
m.report()
#m.Insertar("oferta","df","lucas")
#print(m.getNodo(1,1).empresa)
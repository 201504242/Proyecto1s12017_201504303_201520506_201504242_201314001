import os
import lista
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
		self.usuarios = lista.Lista()

class Matriz(object):
	"""docstring for Matriz"""
	def __init__(self):
		super(Matriz, self).__init__()
		self.primero = Nodo("","","")
		self.lengthX = 0
		self.lengthY = 0
#----------------------------------------------Metodo Insertar
	def Insertar(self,empresa,departamento,nombre,usuario,password):
		nuevo = Nodo(empresa,departamento,nombre)
		#Comprobamos si esta vacia la matriz
		if self.primero.derecha == None:
			self.lengthX += 1
			self.lengthY += 1
			self.amplicarCabeceras()
			self.ampliarColumna()
			self.ampliarFila()
			self.getNodo(1,1).nombre = nombre
			self.getNodo(1,1).usuarios.insertar(nombre,usuario,password)
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
					nodo.usuarios.insertar(nombre,usuario,password)
					self.getNodo(self.lengthX,0).empresa = empresa
					self.getNodo(0,self.lengthY).departamento = departamento
				else:
					self.lengthX += 1
					self.amplicarCabeceras()
					self.ampliarColumna()
					departamento = self.departamentoExistente(departamento)
					nodo = self.getNodo(self.lengthX,departamento.y)
					nodo.nombre = nombre
					nodo.usuarios.insertar(nombre,usuario,password)
					self.getNodo(self.lengthX,0).empresa = empresa
			else:
				if self.departamentoExistente(departamento) == None:
					self.lengthY += 1
					self.amplicarCabeceras()
					self.ampliarFila()
					empresa = self.empresaExistente(empresa)
					nodo = self.getNodo(empresa.x,self.lengthY)
					nodo.nombre = nombre
					nodo.usuarios.insertar(nombre,usuario,password)
					self.getNodo(0,self.lengthY).departamento = departamento
				else:
					empresa = self.empresaExistente(empresa)
					departamento = self.departamentoExistente(departamento)
					nodo = self.getNodo(empresa.x,departamento.y)
					#nodo.nombre = nombre
					nodo.usuarios.insertar(nombre,usuario,password)
					nodo.usuarios.report() 
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

#---------------------------------------------- Acciones con ACTIVOS
	def insertarActivo(self,empresa,departamento,usuario,nombreActivo,descripcionActivo,idActivo):
		empresa = self.empresaExistente(empresa)
		departamento = self.departamentoExistente(departamento)
		if (empresa!=None) and (departamento!=None):
			nodo = self.getNodo(empresa.x,departamento.y)
			if nodo != None:
				usuario = nodo.usuarios.buscarUsuario(usuario)
				if usuario!=None:
					usuario.arbol.insertarNUEVO(nombreActivo,descripcionActivo,idActivo)

	def obtenerActivo(self,empresa,departamento,usuario,idActivo):
		empresa = self.empresaExistente(empresa)
		departamento = self.departamentoExistente(departamento)
		if (empresa!=None) and (departamento!=None):
			nodo = self.getNodo(empresa.x,departamento.y)
			if nodo != None:
				usuario = nodo.usuarios.buscarUsuario(usuario)
				if usuario!=None:
					return usuario.arbol.buscarIDactivo(idActivo,usuario.arbol.raiz)

	def login(self,empresa,departamento,usuario,password):
		empresa = self.empresaExistente(empresa)
		departamento = self.departamentoExistente(departamento)
		if (empresa!=None) and (departamento!=None):
			nodo = self.getNodo(empresa.x,departamento.y)
			if nodo != None:
				return nodo.usuarios.login(usuario,password)
		return None

	def modifcarActvio(self,empresa,departamento,usuario,idActivo,nombre,descripcion):
		empresa = self.empresaExistente(empresa)
		departamento = self.departamentoExistente(departamento)
		if (empresa!=None) and (departamento!=None):
			nodo = self.getNodo(empresa.x,departamento.y)
			if nodo != None:
				usuario = nodo.usuarios.buscarUsuario(usuario)
				if usuario!=None:
					activo = usuario.arbol.buscarIDactivo(idActivo,usuario.arbol.raiz)
					activo.descripcion = descripcion
					activo.nombre = nombre
#m = Matriz()
#m.Insertar("glorsys","conta","lucas","lc","123d") # Nuevo
#m.Insertar("ofert","ope","marcos","mc","123") #Ninguno existente
#m.Insertar("cops","secretaria","paula","p","123") #Ninugno existente
#m.Insertar("nueva","secretaria","ricarda","r","123") #Existente departamento
#m.Insertar("ofert","notariado","denis","d","123") #Existente empresa
#m.Insertar("glorsys","conta","Magy","m","123") #Existente ambos
#m.insertarActivo("glorsys","conta","lc","Computadora","Lapto utilizada para saber mas xD","t2y3u4")
#print(m.obtenerActivo("glorsys","conta","lc","t2y3u4").nombre)
#m.modifcarActvio("glorsys","conta","lc","t2y3u4","dddd","djdjd")
#print(m.obtenerActivo("glorsys","conta","lc","t2y3u4").nombre)
#print(m.login("glorsys","conta","lc","123d"))
#m.report()
#m.Insertar("oferta","df","lucas")
#print(m.getNodo(1,1).empresa)
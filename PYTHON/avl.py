class Nodo(object):
	
	def __init__(self,id,nombre,descripcion,idActivo):
		self.id = id
		self.nombre = nombre
		self.descripcion = descripcion		
		self.idActivo=idActivo
		self.fe =0 
		self.hijoDerecho = None
		self.hijoIzquierdo = None

	def getNombre(self):
		return self.nombre

class Arbol(object):
	def __init__(self):
		self.raiz = None
		self.length = 0

#--------------------------------------------- Metodo Buscar
	def buscar(self,id,raiz):
		if raiz == None:
			return None
		elif int(raiz.id) == int(id):
			return raiz
		elif int(raiz.id) < int(id) : 
			return self.buscar(id,raiz.hijoDerecho)
		else :
			return self.buscar(id,raiz.hijoIzquierdo)

#--------------------------------------------- Metodo para el Fe
	def obtenerFE(self,nodo):
		if nodo==None:
			return -1
		else:
			return nodo.fe

	def max(num1,num2):
		if num1 > num2:
			return num1
		else:
			return num2
#--------------------------------------------- Rotacion simple Izquierda
	def rotacionIzquierda(self,nodo):
		aux = nodo.hijoIzquierdo
		nodo.hijoIzquierdo = aux.hijoDerecho
		aux.hijoDerecho = nodo
		nodo.fe = max(self.obtenerFE(nodo.hijoIzquierdo),self.obtenerFE(nodo.hijoDerecho)) + 1;
		aux.fe = max(self.obtenerFE(aux.hijoIzquierdo),self.obtenerFE(aux.hijoDerecho)) + 1;
		return aux

#--------------------------------------------- Rotacion simple Izquierda
	def rotacionDerecha(self,nodo):
		aux = nodo.hijoDerecho
		nodo.hijoDerecho = aux.hijoIzquierdo
		aux.hijoIzquierdo = nodo
		nodo.fe = max(self.obtenerFE(nodo.hijoIzquierdo),self.obtenerFE(nodo.hijoDerecho)) + 1;
		aux.fe = max(self.obtenerFE(aux.hijoIzquierdo),self.obtenerFE(aux.hijoDerecho)) + 1;
		return aux

#--------------------------------------------- Rotacion doble a la Izquierda
	def rotacionDobleIzquierda(self,nodo):
		nodo.hijoIzquierdo = rotacionDerecha(nodo.hijoIzquierdo)
		aux = rotacionIzquierda(nodo)
		return aux

#--------------------------------------------- Rotacion doble a la Dereccha
	def rotacionDobleDerecha(self,nodo):
		nodo.hijoDerecho = rotacionIzquierda(nodo.hijoDerecho)
		aux = rotacionDerecha(nodo)
		return aux
		
#--------------------------------------------- Insertar
	def insertar(self,nuevo,subarbol):		
		nuevoPadre = subarbol
		if int(nuevo.id) < int(subarbol.id) :
			if subarbol.hijoIzquierdo == None:
				subarbol.hijoIzquierdo = nuevo
			else:
				subarbol.hijoIzquierdo = self.insertar(nuevo,subarbol.hijoIzquierdo)
				if (self.obtenerFE(subarbol.hijoIzquierdo) - self.obtenerFE(subarbol.hijoDerecho)) == 2 :
					if int(nuevo.id) < int(subarbol.hijoIzquierdo.id) :
						nuevoPadre = self.rotacionIzquierda(subarbol)
					else:
						nuevoPadre = self.rotacionDobleIzquierda(subarbol)
		elif int(nuevo.id) > int(subarbol.id) :
			if subarbol.hijoDerecho == None:
				subarbol.hijoDerecho = nuevo
			else:
				subarbol.hijoDerecho =self.insertar(nuevo,subarbol.hijoDerecho)
				if (self.obtenerFE(subarbol.hijoDerecho) - self.obtenerFE(subarbol.hijoIzquierdo)) == 2 :
					if int(nuevo.id) > int(subarbol.hijoDerecho.id):
						nuevoPadre = self.rotacionDerecha(subarbol)
					else:
						nuevoPadre = self.rotacionDobleDerecha(subarbol)
		else:
			print("Nodo duplicado")
		if (subarbol.hijoIzquierdo == None) and (subarbol.hijoDerecho != None):
			subarbol.fe= subarbol.hijoDerecho.fe + 1
		elif (subarbol.hijoIzquierdo != None) and (subarbol.hijoDerecho == None):
			subarbol.fe = subarbol.hijoIzquierdo.fe + 1 
		else:
			subarbol.fe = max(self.obtenerFE(subarbol.hijoIzquierdo),self.obtenerFE(subarbol.hijoDerecho)) +1
		return nuevoPadre

	def insertarNUEVO(self,ide,nombre,descripcion,idActivo):
		nuevo = Nodo(self.length,nombre,descripcion,idActivo)
		if self.raiz == None:
			self.raiz = nuevo
		else:
			self.raiz = self.insertar(nuevo,self.raiz);		
		self.length += 1

#--------------------------------------------- Recorrido
	#Retornar el nodo donde se encuentra el id que se le mando
	def inOrden(self,r,ide):
		if r != None:
			self.inOrden(r.hijoIzquierdo,ide)
			print(r.nombre)
			#if int(r.id) == int(id):
			#	print(r.id)
			#	return r
			self.inOrden(r.hijoDerecho,ide)
		return "fin"

	def puta(self,palabra,raiz):
		
		if raiz !=None:
			self.puta(palabra,raiz.hijoIzquierdo)
			if raiz.hijoIzquierdo != None:
				print("hijo Izquierdo--------"+str(raiz.hijoIzquierdo.id))
			else:
				print("hijo Izquierdo--------"+str(raiz.hijoIzquierdo))
			print("padre--------"+str(raiz.id))
			if raiz.hijoDerecho != None:
				print("hijo Derecho--------"+str(raiz.hijoDerecho.id))
			else:
				print("hijo Izquierdo--------"+str(raiz.hijoIzquierdo))
			self.puta(palabra,raiz.hijoDerecho)

	def buscarIDactivo(self,palabra,raiz):
		if raiz != None:
			if self.buscarIDactivo(palabra,raiz.hijoIzquierdo) != None:
				return self.buscarIDactivo(palabra,raiz.hijoIzquierdo)
			if raiz.nombre == palabra:
				return raiz
			if self.buscarIDactivo(palabra,raiz.hijoDerecho) != None:
				return self.buscarIDactivo(palabra,raiz.hijoDerecho)


arbolAVL = Arbol()
arbolAVL.insertarNUEVO(1,"a","Esto es la prueba 1","ds")

arbolAVL.insertarNUEVO(2,"b","Esto es la prueba 2","d")

arbolAVL.insertarNUEVO(3,"c","Esto es la prueba 3","kdk")

arbolAVL.insertarNUEVO(4,"d","Esto es la prueba 4","fjfjf")

arbolAVL.insertarNUEVO(5,"e","Esto es la prueba 5","jdjdjdjd")

arbolAVL.insertarNUEVO(6,"f","Esto es la prueba 6","jajaja")
arbolAVL.insertarNUEVO(7,"j","Esto es la prueba 6","jajaja")


print(arbolAVL.buscarIDactivo("c",arbolAVL.raiz).id)
#print(arbolAVL.inOrden(arbolAVL.raiz,4))
#print(arbolAVL.buscar(5,arbolAVL.raiz))

#print(type(arbolAVL.inOrden(arbolAVL.raiz,"jdjdjdjd")))
#print(type(arbolAVL.inOrden(arbolAVL.raiz)))


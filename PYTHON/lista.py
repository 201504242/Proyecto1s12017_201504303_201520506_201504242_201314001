class Nodo(object):
	"""docstring for Nodo"""
	def __init__(self, valor,indice):
		self.valor=valor
		self.indice=indice
		self.siguiente = None

	def getValor(self):
		return self.valor

	def getIndice(self):
		return self.indice

	def getSiguiente(self):
		return self.siguiente
	
class Lista(object):
	"""docstring for Lista"""
	def __init__(self):
		self.primero = None
		self.length = 0

	def getLength(self):
		return self.length

	def getPrimero(self):
		return self.primero

	def insertar(self,valor):
		nuevo = Nodo(valor,self.length)
		if self.primero == None:
			self.primero = nuevo
		else:
			auxiliar = self.primero
			while auxiliar != None:
				if auxiliar.siguiente == None:
					break
				auxiliar = auxiliar.siguiente
			auxiliar.siguiente=nuevo
		self.length = self.length + 1

	def buscar(self,valor):
		auxiliar = self.primero
		while auxiliar != None:
			if auxiliar.getValor() == valor:
				print(auxiliar.getIndice())
				return "EL DATO SE ENCUENTRA EN EL INDICE: "+ str(auxiliar.getIndice())
			auxiliar = auxiliar.siguiente
		return "NO SE ENCONTRO EL DATO"

	def eliminar(self,valor):
		print("valor entrante: "+ valor)
		if valor == "0":
			self.primero = self.primero.siguiente
		else:
			auxiliar = self.primero
			while auxiliar != None:
				if auxiliar.siguiente.getIndice() == int(valor):
					auxiliar2 = auxiliar.siguiente
					auxiliar.siguiente = auxiliar2.siguiente
					auxiliar2.siguiente=None
					break
				auxiliar = auxiliar.siguiente
		print("Eliminado valor")
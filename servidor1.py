from flask import Flask, session 
from flask import request
from flask import make_response
from graphviz import Digraph
import pickle
app = Flask(__name__)
class nodosimple():
	"""docstring for nodosimple"""
	def __init__(self,dato,indice):
		super(nodosimple, self).__init__()
		self.dato = dato
		self.nodosiguiente	=  None
		self.indice = indice
class lista():
	def __init__(self):
			self.raiz = None	
			self.count = 0
	def insertar(self,dato):
		nodo = nodosimple(dato,self.count)
		self.count = self.count + 1
		if self.raiz == None :
			self.raiz = nodo
		else:
				aux = self.raiz
				while aux != None :
					if aux.nodosiguiente == None:
						aux.nodosiguiente = nodo
						break
					else:
						aux = aux.nodosiguiente
    
	def delete(self,indice):
		aux = self.raiz
		if indice == 0:
			self.raiz = self.raiz.nodosiguiente
		else:		
			while aux != None :
				#print("Se ensiclo aqui")
				
				if aux.nodosiguiente != None:
					#print(str(aux.nodosiguiente.indice))	
					if str(aux.nodosiguiente.indice) == str(indice):
						#print("ELIMIMINO EL DATOO")
						aux.nodosiguiente = aux.nodosiguiente.nodosiguiente
				aux = aux.nodosiguiente	
		return "ok"					
	def buscar(self,cadena):
		aux = self.raiz
		while aux != None :
					if aux.dato == cadena:
							return 'El dato se encuenra en ' + str(aux.indice)
							break
					else:	
							aux = aux.nodosiguiente 				
		return "No se enconto dato "
	def graficar(self):
		dot = Digraph()
		aux = self.raiz#En esta Pasada solo creo los nodos
		dot.node("Null","Nulo")
		while aux != None :
			dot.node(str(aux.indice),str(aux.dato))	
			aux = aux.nodosiguiente
		aux = self.raiz;	
		while aux != None :
			if aux.nodosiguiente != None:
					dot.edge(str(aux.indice),str(aux.nodosiguiente.indice))
					#dot.edge(str(aux.indice) +str(aux.nodosiguiente.indice), constraint='false')
			else:
					dot.edge(str(aux.indice),"Null")
					#dot.edge("Null","Null")
					#print(aux.indice)					
			aux = aux.nodosiguiente
		#dot.render('round-table.gv', view=True)
		dot.format = 'png' 
		dot.render('lista')	
		return dot.source		
class nodo():
	def __init__(self,correo):
		x = correo.split("@")
		inicial = x[0]
		inicial = inicial[0]
		self.derecha = None
		self.izquierda = None
		self.abajo = None
		self.arriba = None
		self.dominio = x[1]
		self.letra = inicial
		self.correo = correo
		self.x = 0
		self.y = 0
		self.z = 0
		self.siguiente = None
class pila():
	def __init__(self):
		self.cabeza = None
	def push(self,dato):
		nuevo = nodosimple(dato,0)
		if self.cabeza == None:
			self.cabeza = nuevo
		else:
			nuevo.nodosiguiente = self.cabeza
			self.cabeza = nuevo
	def pop(self):
		if self.cabeza != None:
			aux = self.cabeza
			self.cabeza = self.cabeza.nodosiguiente
			return aux.dato
		return "null"	
	def peek(self):
		if self.cabeza != None:
			return self.cabeza.dato
	def graficar(self):
		if self.cabeza != None:
			dot = Digraph('structs',node_attr={'shape':'plaintext'})

			aux = self.cabeza
			tabla = '<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">'
			while aux != None:
				tabla = tabla + '<TR><TD>'+aux.dato+'</TD></TR>'
				aux = aux.nodosiguiente
			tabla = tabla + '</TABLE>>'	
			dot.node('structura1',tabla)
			dot.format = 'png' 
			dot.render('PILA')
			return dot.source			
class cola():
	def __init__(self):
		self.cabeza = None
	def push(self,dato):
		nuevo = nodosimple(dato,0)
		if self.cabeza == None:
			self.cabeza = nuevo
		else:
			aux = self.cabeza
			while aux.nodosiguiente != None:
				aux = aux.nodosiguiente
			aux.nodosiguiente = nuevo
	def pop(self):
		aux = self.cabeza
		self.cabeza = self.cabeza.nodosiguiente
		return aux.dato
	def graficar(self):
		dot = Digraph()
		if self.cabeza != None:
			dot.node('cabeza',"cabeza "+self.cabeza.dato)
			dot.node('null','nulo')
			aux = self.cabeza
			diferenciador = 0
			while aux.nodosiguiente != None:
				aux = aux.nodosiguiente
				dot.node(str(aux.dato)+str(diferenciador),str(aux.dato))
				diferenciador = diferenciador + 1
		#dot.node(str(aux.dato),str(aux.dato))	
			if self.cabeza.nodosiguiente != None:
				dot.edge('cabeza',str(self.cabeza.nodosiguiente.dato)+str(0))
				aux = self.cabeza.nodosiguiente
				diferenciador = 0
				while aux.nodosiguiente != None:
					dot.edge(str(aux.dato)+str(diferenciador),str(aux.nodosiguiente.dato)+str(diferenciador+1))
					diferenciador = diferenciador + 1
					aux = aux.nodosiguiente
			
				dot.edge(str(aux.dato)+str(diferenciador),"null")
		else:
			dot.node('cabeza','Null')	
		dot.format = 'png' 
		dot.render('cola')	
		return dot.source			
class dispersa():
	def __init__(self):
		self.cabeza = None
	def insertar(self,correo):
		nuevo = nodo(correo)
		if self.cabeza == None:
			aux = nodo(nuevo.correo) 
		      #creo la cabeza y las primeras cabezeras 
			self.cabeza = nuevo
			nuevo.correo = None
			derecha = nodo(correo)
			derecha.x = 1
			derecha.y = 0
			derecha.letra = None
			derecha.correo = None
			derecha.izquiera = self.cabeza
			derecha.arriba = self.cabeza
			derecha.abajo = aux 
			#print("derecha " +  derecha.inicial )
			abajo = nodo(correo)
			abajo.x = 0
			abajo.y = 1
			abajo.correo = None
			self.cabeza.derecha = derecha
			self.cabeza.abajo = abajo
			abajo.derecha = aux
			aux.arriba = derecha 
			aux.izquierda = abajo
			aux.x = 1
			aux.y = 1
			derecha.letra = None
			abajo.dominio = None
			self.cabeza.letra = None
			self.cabeza.dominio = None
			#print("inserte "+ str(aux.correo) )
		else:
			nododominio = None
			nodoletra = None
			aux = self.cabeza
			while aux != None:
				if aux.dominio == nuevo.dominio:
					nododominio = aux
				aux = aux.derecha
			aux = self.cabeza
			while aux != None:
				if aux.letra == nuevo.letra:
					nodoletra = aux 
				aux = aux.abajo			
			if nododominio == None: 
				temp = self.cabeza
				while temp != None:
					if temp.derecha == None:
						cabe = nodo(correo)
						cabe.correo = None
						cabe.letra = None
						cabe.x = temp.x + 1
						cabe.y = 0
						temp.derecha = cabe
						cabe.izquierda = temp
						temp = cabe
						nododominio = cabe
					temp = temp.derecha
			if nodoletra == None:
				temp = self.cabeza
				while temp != None:
					if temp.abajo == None:
						ab = nodo(correo)
						ab.correo = None
						ab.dominio = None
						ab.x = 0
						ab.y = temp.y +1
						ab.arriba = temp
						temp.abajo = ab
						temp = ab
						nodoletra = ab
					temp = temp.abajo
			#HASTA AQUI HAY CABEZERAS Y LETRAS NUEVAS 				
			ys = nodoletra.y 
			xs = nododominio.x
			tempD = nododominio
			actualD = None
			actualL = None
			tempL = nodoletra
			while tempD != None:
				if tempD.y > ys:
					actualD = tempD
					break
				if tempD.abajo == None:
					actualD = tempD 	
				tempD = tempD.abajo
			while tempL != None:
				if tempL.x > xs:
					actualL = tempL
					break
				if tempL.derecha == None:
					actualL = tempL
				tempL = tempL.derecha
			print( " EL NODO  dominio : X " + str(actualD.x) + " Y : " +str(actualD.y) + " EN LETRA X: "+ str(actualL.x) + " Y : " +str(actualL.y)+ "Insertando :" + correo + "EN X,Y"+ str(xs)+","+str(ys) )
			# ALFIN COMIENZA LA INSERCION :33
			print(self.buscar(xs,ys))
			profundidad = self.buscar(xs,ys)
			if  profundidad != None:
				print("**** Se encontro el nodo x,y :  "+ str(xs) + "," + str(ys))
				aux = profundidad
				while aux.siguiente != None:
					if aux.siguiente == None:
						break
					aux = aux.siguiente
				print("El nodo dodne se quedo es " + str(aux.correo) + "Y insertando " + str(nuevo.correo) )
				nuevo.x = aux.x 
				nuevo.y = aux.y 
				nuevo.z = aux.z + 1	
				aux.siguiente = nuevo 
			else:	
				if actualD.arriba == None:
					actualD.abajo = nuevo
					nuevo.arriba = actualD
					nuevo.x = xs
					nuevo.y = ys
					#print("LA insercion va para arriba")
				else:
					auxiliar = actualD.arriba 
					nuevo.arriba  = auxiliar
					auxiliar.abajo = nuevo
					actualD.arriba = nuevo 
					nuevo.abajo = actualD
					nuevo.x = xs
					nuevo.y = ys
				if actualL.izquierda == None:
					actualL.derecha = nuevo 
					nuevo.izquierda = actualL
					nuevo.x = xs
					nuevo.y = ys
				else:
					auxliar = actualL.izquierda
					nuevo.izquierda = auxliar 
					auxliar.derecha = nuevo
					actualL.izquierda = nuevo 
					nuevo.derecha = actualL
					nuevo.x = xs
					nuevo.y = ys 
				#print( " SE suponer ya inserte hasta en medio XDD ")
			#else:
			#	print("ENTROOOOO AQUIIIIIIIII*******************MIRAMEEEEW")
			#	nodito = self.buscar(xs,ys)
			#	while nodito != None:
			#		if nodito.siguiente ==None:
			#			nodito.siguiente = nuevo
			#			print("******************* INSertoO A dentro de " + str(nuevo.correo) )
			#		nodito= nodito.siguiente
						
				#Insertar en la lista del nodo 
	def getnombre(self,aux2):
		return str(aux2.x) + ","+ str(aux2.y) + ","+str(aux2.z)					
	def graficar(self):
		dot = Digraph()
		aux = self.cabeza
		aux2 = self.cabeza.derecha
		aux3 = self.cabeza.derecha #KHE???? 

		while aux != None:
			while aux2 != None:
				print()
				aux3 = aux2.siguiente
				if aux3 != None:
					nombre = str(aux2.x) + ","+ str(aux2.y) + ","+str(aux2.z)
					tabla = '<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">'
					tabla = tabla+"<TR><TD>"+str(aux2.correo)+"</TD></TR>"
					while aux3 != None:
						tabla = tabla + "<TR>"
						tabla = tabla + "<TD>"+ str(aux3.correo) + "</TD>"
						tabla = tabla + "</TR>"
						aux3 = aux3.siguiente
					tabla = tabla +'</TABLE>>'	
					dot.node(nombre,tabla)
				else: 
					nombre = str(aux2.x) + ","+ str(aux2.y) + ","+str(aux2.z)
					if aux2.y == 0: 
						dot.node (nombre,aux2.dominio)
					if aux2.x == 0:
						dot.node (nombre,aux2.letra)
						
					dot.node(nombre,aux2.correo)			
				aux2 = aux2.derecha
			print("SAlto Linea WEON")	
			aux = aux.abajo
			aux2 = aux
		#### CREAMOS LOS ENLACES 	
		aux = self.cabeza
		aux2 = self.cabeza
		while aux != None:
			while aux2 != None:
				nombre = str(aux2.x) + ","+ str(aux2.y) + ","+str(aux2.z)
				if aux2.derecha != None:
					dot.edge(nombre,self.getnombre(aux2.derecha))
				if aux2.arriba != None:
					dot.edge(nombre,self.getnombre(aux2.arriba))
				if aux2.izquierda != None:
					dot.edge(nombre,self.getnombre(aux2.izquierda))
				if aux2.abajo != None:
					dot.edge(nombre,self.getnombre(aux2.abajo))																	
				aux2 = aux2.derecha
			print("SAlto Linea WEON")	
			aux = aux.abajo
			aux2 = aux
		aux = self.cabeza
		aux2 = self.cabeza
		while aux != None:
			primero = aux2
			while aux2 != None:	
				if aux2.derecha == None:
					break

				aux2 = aux2.derecha
			final = aux2
			dot.edge(self.getnombre(primero),self.getnombre(final))
			dot.edge(self.getnombre(final),self.getnombre(primero))	
			print("SAlto Linea WEON")	
			aux = aux.abajo
			aux2 = aux
		aux = self.cabeza
		aux2 = self.cabeza
		while aux != None:
			primero = aux2
			while aux2 != None:	
				if aux2.abajo == None:
					break

				aux2 = aux2.abajo
			final = aux2
			dot.edge(self.getnombre(primero),self.getnombre(final))
			dot.edge(self.getnombre(final),self.getnombre(primero))	
			print("SAlto Linea WEON")	
			aux = aux.derecha
			aux2 = aux						
		dot.format = 'png' 
		dot.render('matriz')
		return dot.source	
				
	def debug(self):
		aux = self.cabeza 
		aux2 = self.cabeza
		aux3 = self.cabeza #KHE???? 
		while aux != None:
			while aux2 != None:
				aux3 = aux2.siguiente
				print(str(aux2.correo)+" con las inicial " + str(aux2.letra) + " Y el dominio " + str(aux2.dominio) + " x: " + str(aux2.x) + "Y :"+ str(aux2.y))
				while aux3 != None:
					print(str(aux3.correo)+" con las inicial " + str(aux3.letra) + " Y el dominio " + str(aux3.dominio) + " x: " + str(aux3.x) + "Y :"+ str(aux3.y) + " Z : " + str(aux3.z) )
					aux3 = aux3.siguiente
				aux2 = aux2.derecha
			print("SAlto Linea WEON")	
			aux = aux.abajo
			aux2 = aux
	def buscar(self,x,y):
		aux = self.cabeza
		aux2 = self.cabeza
		while aux != None:
			while aux2 != None:
				#print ("VOY En el x : " + str(aux2.x) + " Y " +str(aux2.y))
				if aux2.x == x and aux2.y == y:
					print (" encontre "+ str(aux2.correo))
					return aux2
				aux2 = aux2.derecha
			aux = aux.abajo
			aux2 = aux		
		return None
	def buscar_porletra(self,letra):
		respuesta = ""
		nodoletra = None
		aux = self.cabeza 
		aux2 = None
		aux3 = self.cabeza #KHE???? 
		while aux != None:
			if aux.letra == letra:
				nodoletra = aux 
			aux = aux.abajo
		
		if nodoletra != None:	
			aux2 = nodoletra.derecha
		
		while aux2 != None:
			aux3 = aux2
				#print(" Con letra "+ str(letra)+"Se econtro "+ str(aux2.correo))
			respuesta = respuesta + ", "+aux2.correo
			while aux3.siguiente != None:
				#print(" Con letra "+ str(letra)+"Se econtro "+ str(aux3.correo))
				respuesta = respuesta + ", " + aux3.correo
				aux3 = aux3.siguiente
			aux2 = aux2.derecha
		if respuesta == "":
			respuesta  = "No se encontro "	
		return respuesta	
	def buscar_porCorreo(self,correo):
		correo  = correo.replace('@','')
		respuesta = ""
		nododominio = None
		aux = self.cabeza
		aux2 = None
		while aux != None:
			if aux.dominio == correo:
				nododominio = aux 
			aux = aux.derecha
		if nododominio != None:	
			aux2 = nododominio.abajo

		while aux2 != None:
			aux3 = aux2
			#print(" Con letra "+ str(letra)+"Se econtro "+ str(aux2.correo))
			respuesta = respuesta +" , " +aux2.correo
			while aux3.siguiente != None:
				#print(" Con letra "+ str(letra)+"Se econtro "+ str(aux3.correo))
				respuesta = respuesta + ", "+ aux3.correo
				aux3 = aux3.siguiente
			aux2 = aux2.abajo
		if respuesta == "":
			respuesta = "No se encontro"	
		return respuesta	
 	# NODO PARA LISTA Y COLA Y PILA 
	def eliminar(self,email):
		nodoArriba = None
		nodoAbajo = None
		nodoIzquierda = None
		nodoDerecha = None
		nodosiguiente = None
		aux = self.cabeza 
		aux2 = self.cabeza
		aux3 = self.cabeza #KHE???? 
		while aux != None:
			while aux2 != None:

				aux3 = aux2.siguiente
				anterior = aux2
				print(aux2.correo)
				if aux2.correo == email:
					print("Encontre el correoe  "+ email)
					if aux2.siguiente != None:
						print("No Tiene Nodos Internos" )
						nodosiguiente = aux2.siguiente
						nodoIzquierda = aux2.izquierda
						nodoDerecha = aux2.derecha
						nodoAbajo = aux2.abajo
						nodoArriba = aux2.arriba
						aux2 = nodosiguiente
						if nodoIzquierda !=  None: 
							nodoIzquierda.derecha = aux2
						if nodoDerecha != None:
							nodoDerecha.izquierda = aux2
						if nodoArriba != None:
							nodoArriba.abajo = aux2
						if nodoAbajo != None:
							nodoAbajo.arriba = aux2
						aux2.izquierda = nodoIzquierda
						aux2.derecha = nodoDerecha
						aux2.arriba = nodoArriba
						aux2.abajo = nodoAbajo
					else:
						print("  Tiene Nodos Internos" )
						nodoIzquierda = aux2.izquierda
						nodoDerecha = aux2.derecha
						nodoAbajo = aux2.abajo
						nodoArriba = aux2.arriba
						aux2.izquierda.derecha = nodoDerecha
						if nodoDerecha != None:
							aux2.derecha.izquierda = nodoIzquierda
						aux2.arriba.abajo = nodoAbajo
						if nodoAbajo != None:
							aux2.abajo.arriba = nodoArriba
					break			
				while aux3 != None:
					if aux3.correo == email:
						anterior.siguiente = aux3.siguiente
						break
					anterior = anterior.siguiente	
					aux3 = aux3.siguiente
				aux2 = aux2.derecha	
			print("SAlto Linea WEON")	
			aux = aux.abajo
			aux2 = aux
		aux = self.cabeza
		dizquierda = None
		dderecha =None
		larriba = None
		labajo = None
		while aux != None:
			if aux.abajo == None:
				dizquierda = aux.izquierda
				dderecha = aux.derecha
				print("**ELMINANDO CABEZERAS ** iz =" + str(aux.dominio) + " dere " + str(aux.dominio))
				if dizquierda != None:
					dizquierda.derecha = dderecha
				if dderecha != None:
					dderecha.izquierda = dizquierda	
			aux = aux.derecha
		aux = self.cabeza
		while aux != None:
			if aux.derecha == None:
				larriba = aux.arriba
				labajo = aux.abajo
				if larriba != None:
					larriba.abajo = labajo
				if labajo != None:
					labajo.arriba =larriba
			aux = aux.abajo		


@app.route('/')
def index():
	print ('hola mundo')
	return  ' '
app.secret_key = 'clave'
@app.route('/crearlista')
def clista():

	listita = lista ()
	#resp = make_response('Cookie Establecida')
	#session['lista'] = listita	
	pickle_out = open("lista.pic","wb")
	pickle.dump(listita,pickle_out)
	pickle_out.close()

	return "adios"
	#return resp	
@app.route('/buscarlista')
def mbista():
	param = request.args.get('p1','*N*')
	pickle_in = open("lista.pic","rb")
	listita = pickle.load(pickle_in)
	respuesta = listita.buscar(param)
	pickle_out = open("lista.pic","wb")
	pickle.dump(listita,pickle_out)
	pickle_out.close()
	return respuesta 
@app.route('/eliminarlista')
def mlista():
	param = request.args.get('p1','*N*')
	pickle_in = open("lista.pic","rb")
	listita = pickle.load(pickle_in)
	#listita.delete(8)
	print(param)
	listita.delete(param)
	print(listita.raiz.dato)
	listita.graficar()
	pickle_out = open("lista.pic","wb")
	pickle.dump(listita,pickle_out)
	pickle_out.close()
	return "ok"	
@app.route('/insertarLista')
def insertarLista():
	param = request.args.get('p1','*N*')
	pickle_in = open("lista.pic","rb")
	listita = pickle.load(pickle_in)
	listita.insertar(param)
	listita.graficar()
	pickle_out = open("lista.pic","wb")
	pickle.dump(listita,pickle_out)
	pickle_out.close()
	listita.graficar()
	return "ok"
@app.route('/pila')
def cpila():

	pilita = pila()
	#resp = make_response('Cookie Establecida')
	#session['lista'] = listita	
	pickle_out = open("pila.pic","wb")
	pickle.dump(pilita,pickle_out)
	pickle_out.close()

	return "adios"
	#return resp	
@app.route('/pilapop')
def mpilapop():
	pickle_in = open("pila.pic","rb")
	pila = pickle.load(pickle_in)
	resultado = pila.pop()
	pila.graficar()
	pickle_out = open("pila.pic","wb")
	pickle.dump(pila,pickle_out)
	pickle_out.close()
	return resultado
@app.route('/pilapeek')	
def pilapeek():
	param = request.args.get('p1','*N*')
	pickle_in = open("pila.pic","rb")
	listita = pickle.load(pickle_in)
	
	pickle_out = open("pila.pic","wb")
	pickle.dump(listita,pickle_out)
	pickle_out.close()
	return listita.peek()
@app.route('/pilapush')
def pilapuhs():
	param = request.args.get('p1','*N*')
	pickle_in = open("pila.pic","rb")
	listita = pickle.load(pickle_in)
	print(param)
	listita.push(param)
	listita.graficar()
	pickle_out = open("pila.pic","wb")
	pickle.dump(listita,pickle_out)
	pickle_out.close()
	return "ok"	
@app.route('/cola')
def ccola():

	ma = cola()
	#resp = make_response('Cookie Establecida')
	#session['lista'] = listita	
	pickle_out = open("cola.pic","wb")
	pickle.dump(ma,pickle_out)
	pickle_out.close()
	
	return "ok"
	#return resp	
@app.route('/encolar')
def encolar():
	param = request.args.get('p1','*N*')
	pickle_in = open("cola.pic","rb")
	listita = pickle.load(pickle_in)
	listita.push(param)
	listita.graficar()
	pickle_out = open("cola.pic","wb")
	pickle.dump(listita,pickle_out)
	pickle_out.close()
	return "ok"	
@app.route('/sacarcola')
def sacarcola():
	param = request.args.get('p1','*N*')
	pickle_in = open("cola.pic","rb")
	ma = pickle.load(pickle_in)
	
	resultado = ma.pop()
	ma.graficar()
	pickle_out = open("cola.pic","wb")
	pickle.dump(ma,pickle_out)
	pickle_out.close()
	return resultado	

@app.route('/crearmatriz')
def cmatriz():

	ma = dispersa()
	#resp = make_response('Cookie Establecida')
	#session['lista'] = listita	
	pickle_out = open("matriz.pic","wb")
	pickle.dump(ma,pickle_out)
	pickle_out.close()
	ma.debug()
	return "ok"
	#return resp	
@app.route('/agregarm')
def aggm():
	param = request.args.get('p1','*N*')
	pickle_in = open("matriz.pic","rb")
	listita = pickle.load(pickle_in)
	listita.insertar(param)
	pickle_out = open("matriz.pic","wb")
	pickle.dump(listita,pickle_out)
	pickle_out.close()
	return "ok"	
@app.route('/eliminarm')
def aggm2():
	param = request.args.get('p1','*N*')
	pickle_in = open("matriz.pic","rb")
	listita = pickle.load(pickle_in)
	listita.eliminar(param)
	listita.graficar()
	pickle_out = open("matriz.pic","wb")
	pickle.dump(listita,pickle_out)
	pickle_out.close()
	return "ok"	
@app.route('/buscarl')
def aggm3():
	param = request.args.get('p1','*N*')
	pickle_in = open("matriz.pic","rb")
	listita = pickle.load(pickle_in)
	result = listita.buscar_porletra(param)
	listita.graficar()
	pickle_out = open("matriz.pic","wb")
	pickle.dump(listita,pickle_out)
	pickle_out.close()
	return result
@app.route('/buscard')
def aggm4():
	param = request.args.get('p1','*N*')
	pickle_in = open("matriz.pic","rb")
	listita = pickle.load(pickle_in)
	result = listita.buscar_porCorreo(param)
	listita.graficar()
	pickle_out = open("matriz.pic","wb")
	pickle.dump(listita,pickle_out)
	pickle_out.close()
	return result

@app.route('/parametros')
def parametros():
		param = request.args.get('p1','no exisite2')
		listita = lista ()
		listita.insertar("HOla mundo1")
		listita.insertar("Hola mundo 2")
		listita.insertar("hola mundo 3 ")
		listita.insertar("hola mundo 4 ")
		listita.insertar("hola mundo 4 ")
		graficolista = listita.graficar()
		print(listita.graficar())
		listita.delete(1)
		aux = listita.raiz
		while True:
			print(aux.dato)
			print(aux.indice)
			if aux.nodosiguiente == None:
				break
			else:
				
				aux = aux.nodosiguiente
		buscando = listita.buscar("Hola mundo 2")		
		print(buscando)
		print("************COLA************")

		colita = cola()
		colita.push("H")
		colita.push("O")
		colita.push("L")
		colita.push("A")
		colita.push("O")
		graficocola  = colita.graficar()
		print(colita.graficar())
		print(colita.pop())
		print(colita.pop())
		
		print(colita.pop())
		
		print(colita.pop())
		print("************Pila************")
		pilita = pila()
		pilita.push("A")
		pilita.push("A1")
		pilita.push("A2")
		pilita.push("A")
		pilita.push("A3")
		graficopila = pilita.graficar()
		print("************Matria dispersa************")
		matriz = dispersa()
		matriz.insertar("jorged@gmail.com")
		matriz.insertar("janiel@gmail.com")

		matriz.insertar("jorgito2@gmail.com")
		matriz.insertar("Daniel@Hmail.com")
		matriz.insertar("Damariz@jorge.com")
		matriz.insertar("Danielito@Hmail.com")
		matriz.insertar("janiel@Hmail.com")
		matriz.insertar("maria@gmail.com")
		matriz.insertar("mzzzz@yahoo.es")
		matriz.insertar("zzzz@yahoo.es")
		matriz.insertar("z1@gmail.com")
		matriz.insertar("Danielito@gmail.com")
		matriz.insertar("maco@gmail.com")
		
		matriz.buscar(1,1)
		matriz.debug()
		resp = matriz.graficar()
		print("ELIMINARR*********************************")
		matriz.eliminar("zzzz@yahoo.es")
		matriz.eliminar("Damariz@jorge.com")
		matriz.eliminar("maria@gmail.com")
		matriz.eliminar("maco@gmail.com")
		matriz.debug()
		print("POR LETRA")
		print(str(matriz.buscar_porletra("D")))
		print("POR correo")
		print(str(matriz.buscar_porCorreo("@gmail.com")))
		return resp

if __name__ == '__main__':
	app.run(debug = True )



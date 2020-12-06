'''
				PROYECTO FINAL
			"Ciudad más cercana"
		Alumno: Juventino Aguilar Correa
			Materia: Algebra Lineal
	Concepto utilizado: Distancia entre Vectores
'''

#1.Librerias Necesarias para la operacion del programa
import turtle
import random
import math

#2.Definimos ventana donde se ejecutara el programa, susdimensiones y el titulo
wn = turtle.Screen()
wn.title("Problema del Viajero")
wn.setup(1300,700)
wn.tracer(0)

#3 Aqui se solicita al usuario ingrsar el numero de ciudades, el numero debe ser mayor a una ciudad y menor a 501
#  ciudades para que el programa no demore tanto en posicionarlas en pantalla
ciudades = 0
while (ciudades<1) or (ciudades>501) :
	ciudades = (int)(wn.textinput("Ciudades", "Indicanos el número de ciudades por visitar\n* Su posicion se generara automaticamente)\n* Debe ser mayor a 1 y menor a 501"))

listaC = []

#3.1 Se crean el numero de ciudades solicitadas y se agregan a un arreglo
for i in range(0, ciudades):
	listaC.append(turtle.Turtle())

ciudadesX = []
ciudadesY = []
numAnadidos = 0
primeraCiudad = False
ciudadPase = False

c = 0

#4 En este for lo que haremos sera dibujar las ciudades en pantalla. 
# La posicion de las ciudades se generará automaticamente, por lo cual existe el problema de que dos ciudades
# aparezcan en el mismo lugar, para solucionar dicho problema se realizara lo siguiente (leer siguiente comentarioo)
for i in range(0, ciudades):
	
	listaC[i].penup()
	listaC[i].shape("circle")
	listaC[i].color("blue")
	
	rX = random.randint(-635, 635)
	rY = random.randint(-335, 335)

#4.1 Primero, la primera ciudad se generara en cualquier posicion
	if (primeraCiudad == False):
		ciudadesX.append(rX)
		ciudadesY.append(rY)
		numAnadidos+=1
		listaC[i].goto(rX, rY)
		primeraCiudad = True

#4.2 Despues, si la primera ciudad ya se creo, deberemos ir creando ciudades pero con la restriccion de que no esten
# en un pperimetro de 15 pixeles de ninguna ciudad, si es que lo llegan a estar, su posicion se generara nuevamente
	else: 
		while ciudadPase == False:
			duplicado = False
			for j in range(0, numAnadidos):
				if (rX >= ciudadesX[j]-20) and (rX <= ciudadesX[j]+20) and (rY >= ciudadesY[j]-20) and (rY <= ciudadesY[j]+20):
					duplicado = True
					break 
			if duplicado == False:
				ciudadPase = True
			else:
				rX = random.randint(-635, 635)
				rY = random.randint(-335, 335)
		if ciudadPase == True:
			ciudadesX.append(rX)
			ciudadesY.append(rY)
			numAnadidos += 1
			listaC[i].goto(rX, rY)
			ciudadPase = False

wn.update()

#5 Solicitar ubicación del usuario (en este caso es la tortuga que aprecerá en el programa), para saber cual sera su punto de partida
px = (int)(wn.textinput("Ubicación X","Indicanos tu posicion X, de inicio\n*Respecto a las coordenadas de un plano cartesiano"))
py = (int)(wn.textinput("Ubicación Y","Indicanos tu posicion Y, de inicio\n*Respecto a las coordenadas de un plano cartesiano"))

#5.1 Dibujar Ciudad Inicial, la cual será  una ciudad aparte de las ya creadas, desde aquí comenzara a moverse el usuario, y aqui sera donde al ultimo vuelva a llegar
ciudadI = turtle.Turtle()
ciudadI.shape("square")
ciudadI.color("blue")
ciudadI.penup()
ciudadI.goto(px, py)
#5.2 Dibujar al usuario en la pantalla con la posicion previamente establecida
usuario = turtle.Turtle()
usuario.shape("turtle")
usuario.color("green")
usuario.penup()
usuario.goto(px,py)

# *Este comando de aqui nos sirve para recargar la pantalla se utiliza mucho en todo el programa
wn.update()

#6 En este apartado se le solicita el modo de avance al usuario.
# Si es modo manual el usuario debera indicar cuando la tortuga debera moverse a la siguiente ciudad
#Si es automatico, la tortuga se movera automaticamente sin necesidad de que el usuario se lo indique
modo = "x"
while modo!="m" and modo!= "a" :
	modo = wn.textinput("Escoga un modo de avance","-Para escoger modo manual escriba: 'm'\n-Para escoger modo automatico escriba: 'a'")

ciudadesDistancias = []
ciudadesFalantes = ciudades
usuario.pendown()
distanciaT = 0

#7 Aquí vamos a repertir el buscar la ciudad mas cercana el mismo numero de veces que el numero de ciudades
for i in range(0,ciudades):

	if modo=="m":
		continuar=0
		while (continuar!=1):
			continuar = (int)(wn.textinput("Continuar","Escriba '1' para continuar con la siguiente ciudad"))

	wn.update()
	#Aqui se calcula la distancia que existe entre la posicion donde se encuentra la tortuga y todos las ciudades que faltan por visitar
	for j in range(0,ciudadesFalantes):
	#Para esto se utiliza la formula de Distancia entre Vectores, la cual es la siguiente
		ciudadesDistancias.append(math.sqrt( (((usuario.xcor()) - (ciudadesX[j]))**2) + (((usuario.ycor()) - (ciudadesY[j]))**2)))

	#Cuando ya se conocen las distancias entre la tortuga y todas las ciudades faltantes, se ordenan de menor a mayor para saber a cual ir 
	ciudadesDistancias_copy=sorted(ciudadesDistancias)

	#Aqui se va sumando el total de distancia recorrida por la tortuga
	distanciaT += ciudadesDistancias_copy[0]
	#Este metodo del objeto usuario nois sirve para llevar a la tortuga hacia la ciudad mas cercana dependiendo del orden del arreglo previamente ordenado
	usuario.goto(ciudadesX[ciudadesDistancias.index(
		ciudadesDistancias_copy[0])], ciudadesY[ciudadesDistancias.index(ciudadesDistancias_copy[0])])
	#Las ciudades faltanates van disminuyendo
	ciudadesFalantes-=1
	#Las ciudades visitadas van cambiando su color a rojo con el metodo "color"
	listaC[ciudadesDistancias.index(ciudadesDistancias_copy[0])].color("red")
	listaC.pop(ciudadesDistancias.index(ciudadesDistancias_copy[0]))
	#Vamos eliminando las coordenadas de las ciudades que ya han sido visitadas con el metodo "pop"
	ciudadesX.pop(ciudadesDistancias.index(ciudadesDistancias_copy[0]))
	ciudadesY.pop(ciudadesDistancias.index(ciudadesDistancias_copy[0]))
	#Se vacian los arreglos que contenian las distancias entre la tortuga y las ciudades
	ciudadesDistancias = []
	ciudadesDistancias_copy = []

#Por ultimo llevamos a la tortuga a su punto de inicio, en donde tambien se encuantra la ciudad origen
distanciaT += math.sqrt( (((usuario.xcor()) - (px))**2) + (((usuario.ycor()) - (py))**2))
ciudadI.color("red")
usuario.goto(px, py)
#Se muestra en la consola el mensaje "Recorrido Completado" y las distancia total recorrida
print("Recorrido Completado")
print("Ditancia recorrida: ",distanciaT)
wn.update()	


#Se le solicita al usuario si quiere continuar viendo la pantalla o cerrar el programa
terminar = 2
while terminar != 0 and terminar != 1:
	terminar = (int)(wn.textinput("Recorrido Completado","La distancia total recorrida es mostrada en a línea de comandos\n-Para cerrar el programa escriba: '0'\n-Para ccontinuar visualizando el programa escriba: '1'"))

if terminar == 0:
	wn.bye()
else:
	#Si se escoge seguir viendo el programa, la ventana se actualizara indefinidamente hasta que se cierre manualmente la ventana
	while True:
		wn.update()		

from framework_mesa import Model
from framework_mesa.space import MultiGrid
from framework_mesa.datacollection import DataCollector

from proyecto_compartir_pelear_grandes_chicos.agentes import Jugadores
from proyecto_compartir_pelear_grandes_chicos.schedule import RandomActivationByBreed

from proyecto_compartir_pelear_grandes_chicos.resolucionDeConflictos import ResolucionDeConflictosEntreDosAgentes

import random

class Ambiente(Model):
	height = 20
	width = 20

	distanciaMaximaVecinos = 20 
	cantidadDeHalcones = 0
	cantidadDeParadojicos =0
	cantidadDePalomas = 0
	valorDelRecurso = 5
	costeDeLesion = 10
	probabilidadDeQueElMayorGane1 = 50
	edadDeReproduccion = 1

	minGlobal = None
	maxGlobal = 0
	
	epoca = 1
	
	description = 'Un modelo descripto por Richard DawkinsA model for simulating wolf and sheep (predator-prey) ecosystem modelling.'
	
	def MostrarMensaje(self):
		mensajeStr = "Estoy mostrando este mensaje"
		return mensajeStr


	def __init__(self, 
		alto = 20,
		ancho = 20,
		distanciaMaximaVecinos = 20, 

		cantidadDePalomasChicos = 0,
		cantidadDePalomasGrandes = 0,
		cantidadDeHalconesChicos = 0,
		cantidadDeHalconesGrandes = 0,
		cantidadDeParadojicosChicos = 5,
		cantidadDeParadojicosGrandes = 0,
		cantidadDeSentidoComunChicos = 0,
		cantidadDeSentidoComunGrandes = 5,

		valorDelRecurso = 5,
		costeDeLesion = 10,
		porcentajeDeQueElMayorGane = 50, 
		edadDeReproduccion = 1
		):
		
		super().__init__()
		self.paso = 1

		self.epoca = 1
		
		self.minGlobal = None
		self.maxGlobal = None
		
		self.alto = alto
		self.ancho = ancho
		
		self.distanciaMaximaVecinos = distanciaMaximaVecinos
		self.cantidadDeHalconesChicos = cantidadDeHalconesChicos
		self.cantidadDeHalconesGrandes = cantidadDeHalconesGrandes
		self.cantidadDePalomasChicos = cantidadDePalomasChicos
		self.cantidadDePalomasGrandes = cantidadDePalomasGrandes
		self.cantidadDeParadojicosChicos = cantidadDeParadojicosChicos
		self.cantidadDeParadojicosGrandes = cantidadDeParadojicosGrandes

		self.cantidadDeSentidoComunChicos = cantidadDeSentidoComunChicos
		self.cantidadDeSentidoComunGrandes = cantidadDeSentidoComunGrandes

		self.valorDelRecurso = valorDelRecurso
		self.costeDeLesion = costeDeLesion
		
		self.edadDeReproduccion = edadDeReproduccion
		
		self.schedule = RandomActivationByBreed(self)
		self.grid = MultiGrid(20, 20, torus=True)
		
		self.grid = MultiGrid(self.alto, self.ancho, torus=False)
		self.datacollector = DataCollector(
			{"Total": lambda m: m.schedule.cantidadDeJugadores0(),
			"SiempreEscala_Grande": lambda m: m.schedule.cantidadDeJugadores("siempreEscala", "grande"),
			"SiempreEscala_Chico": lambda m: m.schedule.cantidadDeJugadores("siempreEscala", "chico"),
			"EscalaSiElOtroEsMasGrande_Grande": lambda m: m.schedule.cantidadDeJugadores("escalaSiElOtroEsMasGrande", "grande"),
			"EscalaSiElOtroEsMasGrande_Chico": lambda m: m.schedule.cantidadDeJugadores("escalaSiElOtroEsMasGrande", "chico"),
			"EscalaSiElOtroEsMasChico_Grande": lambda m: m.schedule.cantidadDeJugadores("escalaSiElOtroEsMasChico", "grande"),
			"EscalaSiElOtroEsMasChico_Chico": lambda m: m.schedule.cantidadDeJugadores("escalaSiElOtroEsMasChico", "chico"),
			"NuncaEscala_Grande": lambda m: m.schedule.cantidadDeJugadores("nuncaEscala", "grande"),
			"NuncaEscala_Chico": lambda m: m.schedule.cantidadDeJugadores("nuncaEscala", "chico")})

		self.probabilidadDeQueElMayorGane1 = porcentajeDeQueElMayorGane / 100.00
		
		i = 0
		while i < self.cantidadDeHalconesChicos:
			
			x = random.randrange(self.ancho)
			y = random.randrange(self.alto)
			
			id = self.next_id()
			estrategia = "siempreEscala"
			
			localia = None
			asimetriaAparente = "chico"
			pos = (x, y)
			jugador1 = Jugadores(id, pos, estrategia, asimetriaAparente, self)
			
			self.grid.place_agent(jugador1, (x, y))
			self.schedule.add(jugador1)
			
			i = i + 1
		    
		i = 0
		while i < self.cantidadDeHalconesGrandes:
			
			x = random.randrange(self.ancho)
			y = random.randrange(self.alto)
			
			id = self.next_id()
			estrategia = "siempreEscala"
			
			localia = None
			asimetriaAparente = "grande"
			pos = (x, y)
			jugador1 = Jugadores(id, pos, estrategia, asimetriaAparente, self)
			
			self.grid.place_agent(jugador1, (x, y))
			self.schedule.add(jugador1)
			
			i = i + 1

		i = 0
		while i < self.cantidadDePalomasChicos:
			
			x = random.randrange(self.ancho)
			y = random.randrange(self.alto)
			
			id = self.next_id()
			estrategia = "nuncaEscala"
			localia = None
			asimetriaAparente = "chico"
			pos = (x, y)
			jugador1 = Jugadores(id, pos, estrategia, asimetriaAparente, self)
			self.grid.place_agent(jugador1, (x, y))
			self.schedule.add(jugador1)
			
			i = i + 1

		i = 0
		while i < self.cantidadDePalomasGrandes:
			
			x = random.randrange(self.ancho)
			y = random.randrange(self.alto)
			
			id = self.next_id()
			estrategia = "nuncaEscala"
			localia = None
			asimetriaAparente = "grande"
			pos = (x, y)
			jugador1 = Jugadores(id, pos, estrategia, asimetriaAparente, self)
			self.grid.place_agent(jugador1, (x, y))
			self.schedule.add(jugador1)
			
			i = i + 1

			
		i = 0
		while i < self.cantidadDeSentidoComunChicos:
			
			x = random.randrange(self.ancho)
			y = random.randrange(self.alto)
			
			id = self.next_id()
			estrategia = "escalaSiElOtroEsMasChico"
			localia = None
			asimetriaAparente = "chico"
			pos = (x, y)
			jugador1 = Jugadores(id, pos, estrategia, asimetriaAparente, self)
			self.grid.place_agent(jugador1, (x, y))
			self.schedule.add(jugador1)
			
			i = i + 1
			
		i = 0
		while i < self.cantidadDeSentidoComunGrandes:
			
			x = random.randrange(self.ancho)
			y = random.randrange(self.alto)
			
			id = self.next_id()
			estrategia = "escalaSiElOtroEsMasChico"
			localia = None
			asimetriaAparente = "grande"
			pos = (x, y)
			jugador1 = Jugadores(id, pos, estrategia, asimetriaAparente, self)
			self.grid.place_agent(jugador1, (x, y))
			self.schedule.add(jugador1)
			
			i = i + 1


		i = 0
		while i < self.cantidadDeParadojicosChicos:
			
			x = random.randrange(self.ancho)
			y = random.randrange(self.alto)
			
			id = self.next_id()
			estrategia = "escalaSiElOtroEsMasGrande"
			localia = None
			asimetriaAparente = "chico"
			pos = (x, y)
			jugador1 = Jugadores(id, pos, estrategia, asimetriaAparente, self)
			self.grid.place_agent(jugador1, (x, y))
			self.schedule.add(jugador1)
			
			i = i + 1
			
		i = 0
		while i < self.cantidadDeParadojicosGrandes:
			
			x = random.randrange(self.ancho)
			y = random.randrange(self.alto)
			
			id = self.next_id()
			estrategia = "escalaSiElOtroEsMasGrande"
			localia = None
			asimetriaAparente = "grande"
			pos = (x, y)
			jugador1 = Jugadores(id, pos, estrategia, asimetriaAparente, self)
			self.grid.place_agent(jugador1, (x, y))
			self.schedule.add(jugador1)
			
			i = i + 1




		self.datacollector.collect(self)     
		self.running = True
	
	def step(self):

		print("Paso: " + str(self.paso))
		print("")
			
		puntajeMinimo = None
		puntajeMaximo = None
		
		for agente in self.schedule.agents:
			
			agente.SetCombatioContraAlguienEnEstaEpoca(False)
			
			puntajeBruto = agente.TotalDePuntos()
			
			if puntajeMinimo == None:
				puntajeMinimo = puntajeBruto
			
			if puntajeMaximo == None:
				puntajeMaximo = puntajeBruto
			
			if puntajeBruto < puntajeMinimo:
				puntajeMinimo = puntajeBruto
			
			if puntajeBruto > puntajeMaximo:
				puntajeMaximo = puntajeBruto
		

		poblacion = self.schedule.cantidadDeJugadores0()

		eliminoIndividiosAlternativos = True
		k = 1
		for agente in self.schedule.agents:
			
			# W(H) = pE(H,H) + (1-p)E(H,D)
			# W(D) = pE(D,H) + (1-p)E(D,D)
			
			# W = pW(H) + (1-p)W(D)
			# pNew = pW(H)/W
			
			# E(D,D)<E(H,D)
			
			# 1/2(V-C) > 0 or
			# V > C
			
			# pNew = V/C
			
			# E(H,I) = E(D,I)
			# pE(H,H) + (1-p)E(H,D) = pE(D,H) + (1-p)E(D,D)
			
			# p(1/2)(V-C) + (1-p)V = (1/2)(1/2)V

			# Cuando un individuo llega a la edad de reproducci&#xF3;n hace copias de s&#xED; mismo. La cantidad de copias que el individuo va a hacer depende no solo de su pontaje sino que depende tambi&#xE9;n de la cantidad de individuos que hay en la poblaci&#xF3;n. Los puntos que los individuos obtuvieron en los combates  se convierten a una escala del 0 al 100. Los que tienen 100 son los individuos que m&#xE1;s puntos obtuvieron y los que tienen 0 son los individuos que menos puntos obtuvieron. 
			
			# Si la poblaci&#xF3;n es de menos de 50 individuos y el sujeto obtiene menos de 50 en la generaci&#xF3;n siguiente habr&#xE1; una sola copia de s&#xED; mismo, si tiene m&#xE1;s de 50 puntos hace 2 copias de s&#xED; mismo. 
			
			# Si la poblaci&#xF3;n esta entra 50 y 100 y el sujeto obtiene menos de 33 no hace copias de s&#xED; mismo, si tiene entre 33 y 66 hace 1 copia de s&#xED; mismo, si tiene m&#xE1;s de 66 hace dos copias de s&#xED; mismo.
			
			# Los descendientes heredan la misma estrategia que los padres. Si los padres son de escalar sus descendientes tienen las mismas estrategias de resoluci&#xF3;n de conflicto.
			
			# Luego de la reproducci&#xF3;n el individuo muere.


			puntajeBruto = agente.TotalDePuntos()
			if (not (puntajeMaximo - puntajeMinimo) == 0):
				puntajeRelativo = (puntajeBruto - puntajeMinimo)/(puntajeMaximo - puntajeMinimo) 
			else:
				puntajeRelativo = 0
			
			puntajePorcentual = round(puntajeRelativo * 100)
			#print("puntajePorcentual:"+str(puntajePorcentual))
			agente.AsignarPuntajePorcentual(puntajePorcentual)


			if agente.Edad() == self.edadDeReproduccion:

				#print("La poblacion actual es de " + str(poblacion))
				#if (poblacion <= 50):
				#	print("El jugador que tiene la menor cantidad de puntos hace una copia de si  mismo, el jugador que tiene la mayor cantidad de puntos hace 2 copias de si mismo")
				
				#if (poblacion > 50 and poblacion < 100):
				#	print("El jugador que tiene la menor cantidad de puntos no hace ninguna copia de si mismo, el jugador que tiene la mayor cantidad de puntos hace 2 copias de si mismo")
				
				#if (poblacion > 50 and poblacion < 100):
				#	print("El jugador que tiene la menor cantidad de puntos no hace ninguna copia de si mismo, el jugador que tiene la mayor cantidad de puntos hace 1 sola copias de si mismo")

				
				numeroDeCopias = 0
				
				if (poblacion <= 5):
					if puntajePorcentual < 50: 
						numeroDeCopias = 1
					if puntajePorcentual >= 50: 
						numeroDeCopias = 2

					#print("numeroDeCopias:"+str(numeroDeCopias))
				
				if (poblacion > 5 and poblacion < 10):
					if puntajePorcentual >= 0 and puntajePorcentual < 60: 
						numeroDeCopias = 1
					if puntajePorcentual >= 60: 
						numeroDeCopias = 2

				# Consideramos que con mas de N individuos hay sobrepoblacion
				# Elegimos aleatoreamente, alternativamente, individuos que van a morir sin reproducirse, e 
				# individuos que van a morir dejando un solo descendiente. De esta forma se reduce la poblacion
				if (poblacion >= 10):
					if(eliminoIndividiosAlternativos == True):
						numeroDeCopias = 0
						eliminoIndividiosAlternativos = False
					else:
						numeroDeCopias = 1
						eliminoIndividiosAlternativos = True
				
				posicionDelAgente = agente.pos
				(p0, p1) = posicionDelAgente
				#print("paso:" + str(self.paso) + " poblacion:" + str(poblacion) + " puntajePorcentual:" + str(puntajePorcentual) + " numeroDeCopias:" + str(numeroDeCopias))

				mostrarMensaje = ""
				mostrarMensaje = mostrarMensaje + " -El jugador "+ agente.Estrategia() + "-" + agente.AsimetriaAparente() + " localizado en (" + str(p0) + "," + str(p1) + ") " +" hizo " + str(numeroDeCopias) + " copias de si mismo por tener un puntaje de " + str(agente.TotalDePuntos())  + " porcentual de "+ str(agente.ValorPuntajePorcentual())+"% en una poblacion de "+ str(poblacion) +" individuos y fueron puestos en:"
				print(mostrarMensaje)

				#print(" -El jugador "+ agente.Estrategia() + "-" + agente.AsimetriaAparente() + " localizado en (" + str(p0) + "," + str(p1) + ") " +" hizo " + str(numeroDeCopias) + " copias de si mismo por tener un puntaje de " + str(agente.TotalDePuntos())  + " porcentual de "+ str(agente.ValorPuntajePorcentual())+"% en una poblacion de "+ str(poblacion) +" individuos y fueron puestos en:")
				i = 0
				while i < numeroDeCopias:
					
					posicionesVecinas  = self.grid.get_neighborhood(posicionDelAgente, True, True)
					posicionElejida = random.choice(posicionesVecinas)
					posCopX = posicionElejida[0]
					posCopY = posicionElejida[1]
					
					estrategia = agente.Estrategia()
					asimetriaAparente = agente.AsimetriaAparente()
					jugador1 = Jugadores(self.next_id(), posicionElejida, estrategia, asimetriaAparente, self)
					self.grid.place_agent(jugador1, posicionElejida)
					self.schedule.add(jugador1)
					print("  posicion: (" + str(posCopX) + "," + str(posCopY) + ") ")
			
					i = i + 1
				#print("")
				
			if agente.Edad() > self.edadDeReproduccion - 1:
				
				(posX, posY) = agente.pos
				
				self.grid.remove_agent(agente)
				self.schedule.remove(agente)

				print("  -El jugador "+ agente.Estrategia() + "-" + agente.AsimetriaAparente() + " localizado en (" + str(posX) + "," + str(posY) + ") " +" fue eliminado por tener mas de " + str(self.edadDeReproduccion + 1))
				print("")
				
			if agente.Edad() >= 0 and agente.Edad() < self.edadDeReproduccion:
				
				(posX, posY) = agente.pos
				posicionesVecinas  = self.grid.get_neighborhood((posX, posY), True, True)
				posicionElejida = random.choice(posicionesVecinas)
				self.grid.move_agent(agente, posicionElejida)












		#print("Contiendas:")
		#print("-")
		i = 1
		for agenteA in self.schedule.agents:
			(p0, p1) = agenteA.pos
			
			if agenteA.Edad() >= 0 and agenteA.Edad() < self.edadDeReproduccion:
				j = 1
				for agenteB in self.grid.get_neighbors((p0, p1), True, include_center = True, radius = self.distanciaMaximaVecinos):
					if agenteB.Edad() >= 0 and agenteB.Edad() <= self.edadDeReproduccion + 1:
						(p20, p21) = agenteB.pos
							
						if (not (agenteA.unique_id == agenteB.unique_id)) and (agenteB.GetCombatioContraAlguienEnEstaEpoca() == False):

							(agenteA, agenteB, pr) = ResolucionDeConflictosEntreDosAgentes(agenteA, agenteB, self.valorDelRecurso, self.costeDeLesion, self.probabilidadDeQueElMayorGane1)

							posicionDelAgente = agenteA.pos
							(posX, posY) = posicionDelAgente

							mostrarMensaje = " \n"	
							mostrarMensaje = mostrarMensaje + " Numero aleatorio: " + str(pr) + " Probabilidad de que el mayor gane: "+ str(self.probabilidadDeQueElMayorGane1) + " \n"	
							mostrarMensaje = mostrarMensaje + "   AgenteA: "+ agenteA.Estrategia() + " " + agenteA.AsimetriaAparente() + " puntos: " + str(agenteA.TotalDePuntos()) +  " localizado en (" + str(posX) + "," + str(posY) + ") peleo contra "	+ " \n"

							#print(" Numero aleatorio: " + str(pr) + " Probabilidad de que el mayor gane: "+ str(self.probabilidadDeQueElMayorGane1))
							#print("   AgenteA: "+ agenteA.Estrategia() + " " + agenteA.AsimetriaAparente() + " puntos: " + str(agenteA.TotalDePuntos()) + " = " + str(agenteA.ValorPuntajePorcentual()) + " localizado en (" + str(posX) + "," + str(posY) + ") peleo contra ")

							posicionDelAgente = agenteB.pos
							(posX, posY) = posicionDelAgente

							mostrarMensaje = mostrarMensaje + "   AgenteB: "+ agenteB.Estrategia() + " " + agenteB.AsimetriaAparente() + " puntos: " + str(agenteB.TotalDePuntos()) +  " localizado en (" + str(posX) + "," + str(posY) + ")"	

							#print("   AgenteB: "+ agenteB.Estrategia() + " " + agenteB.AsimetriaAparente() + " puntos: " + str(agenteB.TotalDePuntos()) + " = " + str(agenteB.ValorPuntajePorcentual()) + " localizado en (" + str(posX) + "," + str(posY) + ")")


							mostrarMensaje = mostrarMensaje + ""	+ " \n"
							print(mostrarMensaje)

							agenteA.SetCombatioContraAlguienEnEstaEpoca(True)
						j = j + 1
				i = i + 1



		puntajeMinimo = None
		puntajeMaximo = None
		
		print(" ")
		for agenteC in self.schedule.agents:
			
			agenteC.SetCombatioContraAlguienEnEstaEpoca(False)
			
			puntajeBruto = agenteC.TotalDePuntos()
			print("puntajeBruto: " + str(puntajeBruto))
			
			if puntajeMinimo == None:
				puntajeMinimo = puntajeBruto
			
			if puntajeMaximo == None:
				puntajeMaximo = puntajeBruto
			
			if puntajeBruto < puntajeMinimo:
				puntajeMinimo = puntajeBruto
			
			if puntajeBruto > puntajeMaximo:
				puntajeMaximo = puntajeBruto

		print(" ")
		#print("puntajeMinimo: " + str(puntajeMinimo))
		#print("puntajeMaximo: " + str(puntajeMaximo))
		print(" ")

		for agente in self.schedule.agents:

			puntajeBruto = agente.TotalDePuntos()
			asimetria = agente.AsimetriaAparente()
			estrategia = agente.Estrategia()


			if (not (puntajeMaximo - puntajeMinimo) == 0):
				puntajeRelativo = (puntajeBruto - puntajeMinimo)/(puntajeMaximo - puntajeMinimo) 
			else:
				puntajeRelativo = 0
			
			puntajePorcentual = round(puntajeRelativo * 100)
			#print("asimetria:"+str(asimetria))
			#print("estrategia:"+str(estrategia))
			#print("puntajePorcentual:"+str(puntajePorcentual))
			agente.AsignarPuntajePorcentual(puntajePorcentual)
		print(" ")




	            
		self.schedule.step()
		self.datacollector.collect(self)

		print(" ")
		print(" ")
		print(" ")

		self.paso = self.paso + 1

	
	def run_model(self, step_count = 200):
		a = 10

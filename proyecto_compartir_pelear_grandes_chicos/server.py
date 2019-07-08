from framework_mesa.visualization.ModularVisualization import ModularServer
from framework_mesa.visualization.UserParam import UserSettableParameter
from framework_mesa.visualization.modules import CanvasGrid, ChartModule, TextElement
from framework_mesa.visualization.UserParam import UserSettableParameter
from framework_mesa.visualization.ModularVisualization import VisualizationElement

from proyecto_compartir_pelear_grandes_chicos.agentes import Jugadores
from proyecto_compartir_pelear_grandes_chicos.model import Ambiente

import os
import tornado.httpserver
import tornado.ioloop
import tornado.web

import random

import numpy as np


#import tornado.web.RequestHandler

from framework_mesa.visualization.TextVisualization import (
	TextData, TextGrid, TextVisualization
)

class HistogramModule(VisualizationElement):

	local_includes = ["framework_mesa/visualization/templates/js/HistogramModule9.js"]
	
	def __init__(self, bins, canvas_height, canvas_width):
		self.canvas_height = canvas_height
		self.canvas_width = canvas_width
		self.bins = bins
		new_element = "new HistogramModule({}, {}, {})"
		new_element = new_element.format(bins,
						canvas_width,
						canvas_height)
		self.js_code = "elements.push(" + new_element + ");"
	
	def render(self, model):
		#wealth_vals = [agent.wealth for agent in model.schedule.agents]
		#hist = np.histogram(wealth_vals, bins=self.bins)[0]
		#return [int(x) for x in hist]    
		
		porcentajeDePalomasGrande = model.schedule.porcentajeDeJugadores("nuncaEscala", "grande")
		
		porcentajeDePalomasChico = model.schedule.porcentajeDeJugadores("nuncaEscala", "chico")
		
		porcentajeDeHalconesGrande = model.schedule.porcentajeDeJugadores("siempreEscala", "grande")
		
		porcentajeDeHalconesChico = model.schedule.porcentajeDeJugadores("siempreEscala", "chico")
		
		porcentajeDeParadojicosGrande = model.schedule.porcentajeDeJugadores("escalaSiElOtroEsMasGrande", "grande")
		
		porcentajeDeParadojicosChico = model.schedule.porcentajeDeJugadores("escalaSiElOtroEsMasGrande", "chico")
		
		porcentajeDeSentidoComunGrande = model.schedule.porcentajeDeJugadores("escalaSiElOtroEsMasChico", "grande")
		
		porcentajeDeSentidoComunChico = model.schedule.porcentajeDeJugadores("escalaSiElOtroEsMasChico", "chico")
		
		return [porcentajeDePalomasGrande, porcentajeDePalomasChico, porcentajeDeHalconesGrande, porcentajeDeHalconesChico, porcentajeDeParadojicosGrande, porcentajeDeParadojicosChico, porcentajeDeSentidoComunGrande, porcentajeDeSentidoComunChico]

def personalizacionDelAmbiente(agent):
	if agent is None:
		return
	
	portrayal = {}






	
	if agent.estrategia == "siempreEscala" and agent.asimetriaAparente == "grande":
			portrayal["Shape"] = "proyecto_compartir_pelear_grandes_chicos/resources/halconGrande.png"
			# https://icons8.com/web-app/36821/German-Shepherd
			portrayal["Estrategia"] = agent.estrategia
			portrayal["Asimetria"] = agent.asimetriaAparente
			portrayal["Edad"] = round(agent.edad, 1)
			portrayal["Puntos"] = agent.TotalDePuntos()
			portrayal["PuntajePorcentual"] = agent.ValorPuntajePorcentual()
			portrayal["Layer"] = 1
			portrayal["text_color"] = "#08088A"
	
	if agent.estrategia == "siempreEscala" and agent.asimetriaAparente == "chico":
			portrayal["Shape"] = "proyecto_compartir_pelear_grandes_chicos/resources/halconChico3.png"
			# https://icons8.com/web-app/36821/German-Shepherd
			portrayal["Estrategia"] = agent.estrategia
			portrayal["Asimetria"] = agent.asimetriaAparente
			portrayal["Edad"] = round(agent.edad, 1)
			portrayal["Puntos"] = agent.TotalDePuntos()
			portrayal["PuntajePorcentual"] = agent.ValorPuntajePorcentual()
			portrayal["Layer"] = 1
			portrayal["text_color"] = "#5858FA"
	
	if agent.estrategia == "nuncaEscala" and agent.asimetriaAparente == "grande":
			portrayal["Shape"] = "proyecto_compartir_pelear_grandes_chicos/resources/palomaGrande3.png"
			# https://icons8.com/web-app/36821/German-Shepherd
			portrayal["Estrategia"] = agent.estrategia
			portrayal["Asimetria"] = agent.asimetriaAparente
			portrayal["Edad"] = round(agent.edad, 1)
			portrayal["Puntos"] = agent.TotalDePuntos()
			portrayal["PuntajePorcentual"] = agent.ValorPuntajePorcentual()
			portrayal["Layer"] = 1
			portrayal["text_color"] = "#8A0829"
	
	if agent.estrategia == "nuncaEscala" and agent.asimetriaAparente == "chico":
			portrayal["Shape"] = "proyecto_compartir_pelear_grandes_chicos/resources/palomaChica3.png"
			# https://icons8.com/web-app/36821/German-Shepherd
			portrayal["Estrategia"] = agent.estrategia
			portrayal["Asimetria"] = agent.asimetriaAparente
			portrayal["Edad"] = round(agent.edad, 1)
			portrayal["Puntos"] = agent.TotalDePuntos()
			portrayal["PuntajePorcentual"] = agent.ValorPuntajePorcentual()
			portrayal["Layer"] = 1
			portrayal["text_color"] = "#FA5882"
	
	if agent.estrategia == "escalaSiElOtroEsMasGrande" and agent.asimetriaAparente == "grande":
			portrayal["Shape"] = "proyecto_compartir_pelear_grandes_chicos/resources/paradojicoGrande.png"
			# https://icons8.com/web-app/36821/German-Shepherd
			portrayal["Estrategia"] = agent.estrategia
			portrayal["Asimetria"] = agent.asimetriaAparente
			portrayal["Edad"] = round(agent.edad, 1)
			portrayal["Puntos"] = agent.TotalDePuntos()
			portrayal["PuntajePorcentual"] = agent.ValorPuntajePorcentual()
			portrayal["Layer"] = 1
			portrayal["text_color"] = "#868A08"
	
	if agent.estrategia == "escalaSiElOtroEsMasGrande" and agent.asimetriaAparente == "chico":
			portrayal["Shape"] = "proyecto_compartir_pelear_grandes_chicos/resources/paradojicoChico.png"
			# https://icons8.com/web-app/36821/German-Shepherd
			portrayal["Estrategia"] = agent.estrategia
			portrayal["Asimetria"] = agent.asimetriaAparente
			portrayal["Edad"] = round(agent.edad, 1)
			portrayal["Puntos"] = agent.TotalDePuntos()
			portrayal["PuntajePorcentual"] = agent.ValorPuntajePorcentual()
			portrayal["Layer"] = 1
			portrayal["text_color"] = "#F2F5A9"
	    
	if agent.estrategia == "escalaSiElOtroEsMasChico" and agent.asimetriaAparente == "grande":
			portrayal["Shape"] = "proyecto_compartir_pelear_grandes_chicos/resources/paradojicoGrande.png"
			# https://icons8.com/web-app/36821/German-Shepherd
			portrayal["Estrategia"] = agent.estrategia
			portrayal["Asimetria"] = agent.asimetriaAparente
			portrayal["Edad"] = round(agent.edad, 1)
			portrayal["Puntos"] = agent.TotalDePuntos()
			portrayal["PuntajePorcentual"] = agent.ValorPuntajePorcentual()
			portrayal["Layer"] = 1
			portrayal["text_color"] = "#8a075a"
	
	if agent.estrategia == "escalaSiElOtroEsMasChico" and agent.asimetriaAparente == "chico":
			portrayal["Shape"] = "proyecto_compartir_pelear_grandes_chicos/resources/paradojicoChico.png"
			# https://icons8.com/web-app/36821/German-Shepherd
			portrayal["Estrategia"] = agent.estrategia
			portrayal["Asimetria"] = agent.asimetriaAparente
			portrayal["Edad"] = round(agent.edad, 1)
			portrayal["Puntos"] = agent.TotalDePuntos()
			portrayal["PuntajePorcentual"] = agent.ValorPuntajePorcentual()
			portrayal["Layer"] = 1
			portrayal["text_color"] = "#8a078a"
	
	return portrayal

canvas_element = CanvasGrid(personalizacionDelAmbiente, 20, 20, 500, 500)
chart_element = ChartModule([{"Label": "SiempreEscala_Grande", "Color": "#08088A"},
				{"Label": "SiempreEscala_Chico", "Color": "#5858FA"},
				{"Label": "EscalaSiElOtroEsMasGrande_Grande", "Color": "#868A08"},
				{"Label": "EscalaSiElOtroEsMasGrande_Chico", "Color": "#F2F5A9"},
				{"Label": "EscalaSiElOtroEsMasChico_Grande", "Color": "#8a075a"},
				{"Label": "EscalaSiElOtroEsMasChico_Chico", "Color": "#8a078a"},
				{"Label": "NuncaEscala_Grande", "Color": "#8A0829"},
				{"Label": "NuncaEscala_Chico", "Color": "#FA5882"}])



distanciaMaximaVecinos= UserSettableParameter('slider', 'Distancia dentro de la cual se consideran adversarios', 20, 1, 20)
cantidadDePalomasChicos= UserSettableParameter('slider', 'Cantidad inicial de individuos chicos que nunca escalan. Solo comparten y ceden si el otro escala', 0, 0, 10) 
cantidadDePalomasGrandes= UserSettableParameter('slider', 'Cantidad inicial de individuos grandes que nunca escalan. Solo comparten y ceden si el otro escala', 0, 0, 10) 
cantidadDeHalconesChicos= UserSettableParameter('slider', 'Cantidad inicial de individuos chicos que siempren escalan. Nunca comparten, gana o pierde el recurso', 0, 0, 10)
cantidadDeHalconesGrandes= UserSettableParameter('slider', 'Cantidad inicial de individuos grandes que siempren escalan. Nunca comparten, gana o pierde el recurso', 0, 0, 10)
cantidadDeParadojicosChicos= UserSettableParameter('slider', 'Cantidad inicial de individuos chicos que escalan solo si el adversario es mas grande', 2, 0, 10)
cantidadDeParadojicosGrandes= UserSettableParameter('slider', 'Cantidad inicial de individuos grandes que escalan solo si el adversario es mas grande', 0, 0, 10)
cantidadDeSentidoComunChicos= UserSettableParameter('slider', 'Cantidad inicial de individuos chicos que escalan solo si el adversario es mas chico', 0, 0, 10)
cantidadDeSentidoComunGrandes= UserSettableParameter('slider', 'Cantidad inicial de individuos grandes que escalan solo si el adversario es mas chico', 2, 0, 10)
valorDelRecurso= UserSettableParameter('slider', 'Valor de un recurso. El ganador de un combate se queda con todo el recurso, si se comparte es mitad para cada uno', 5, 0, 10) 
costeDeLesion= UserSettableParameter('slider', 'Costo de una lesion. Solo el perdedor de un combate paga el costo', 10, 0, 10) 
porcentajeDeQueElMayorGane= UserSettableParameter('slider', 'Porcentaje de veces que el mas grande gana un combate. Si los individuos tienen el mismo tama&#xF1;o la mitad de las veces gana uno y la otra mitad gana el otro.', 50, 0, 100) 
edadDeReproduccion= UserSettableParameter('slider', 'Paso en que se produce la reproduccion y mueren', 1, 0, 10)



histogram = HistogramModule(list(range(10)), 200, 500)



# Asimetria arbitraria
# Se pueden diferenciar entre residentes e intrusos
# pero esta diferencia no influye en nada en el resultado del combate.

# residente-intruso
# estrategia paradojica

# Estrategia condicional de sentido comun
# El residente gana, el intruso se retira
# Estrategia condicional paradojica
# Pagina 92


server = ModularServer(Ambiente, [canvas_element, chart_element, histogram], "Machos galanteadores y fieles. Hembras faciles y esquivas", 
			{"distanciaMaximaVecinos": distanciaMaximaVecinos,
			"cantidadDePalomasChicos": cantidadDePalomasChicos,
			"cantidadDePalomasGrandes": cantidadDePalomasGrandes,
			"cantidadDeHalconesChicos": cantidadDeHalconesChicos,
			"cantidadDeHalconesGrandes": cantidadDeHalconesGrandes,
			"cantidadDeParadojicosChicos": cantidadDeParadojicosChicos,
			"cantidadDeParadojicosGrandes": cantidadDeParadojicosGrandes,
			"cantidadDeSentidoComunChicos": cantidadDeSentidoComunChicos,
			"cantidadDeSentidoComunGrandes": cantidadDeSentidoComunGrandes,
			"valorDelRecurso": valorDelRecurso,
			"costeDeLesion": costeDeLesion,
			"porcentajeDeQueElMayorGane": porcentajeDeQueElMayorGane,
			"edadDeReproduccion": edadDeReproduccion})


#server.port = 8257
server.port = int(os.environ.get("PORT", 5000))

server.launch()

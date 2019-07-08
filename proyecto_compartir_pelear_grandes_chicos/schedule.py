from collections import defaultdict

from framework_mesa.time import RandomActivation
from proyecto_compartir_pelear_grandes_chicos.agentes import Jugadores

class RandomActivationByBreed(RandomActivation):
	model = None
	
	def __init__(self, model):
		super().__init__(model)
		self.agents_by_breed = defaultdict(dict)
		self.model = model
	
	def add(self, agent):
	
		self._agents[agent.unique_id] = agent
		agent_class = type(agent)
		self.agents_by_breed[agent_class][agent.unique_id] = agent
	
	def remove(self, agent):
	
		del self._agents[agent.unique_id]
		
		agent_class = type(agent)
		del self.agents_by_breed[agent_class][agent.unique_id]
	
	def cantidadDeJugadores0(self):
		n = len(self.agents_by_breed[Jugadores])
		return n
	
	def porcentajeDeJugadores(self, estrategia, asimetriaAparente):
		todos = len(self.agents_by_breed[Jugadores])
		n = 0
		for i in self.agents_by_breed[Jugadores]:
			agente3 = self.agents_by_breed[Jugadores][i]
			if agente3.estrategia == estrategia and agente3.asimetriaAparente == asimetriaAparente:
				n = n + 1
		if not n == 0:
			n = round(n/todos, 2)
		else:
			n = 0
		
		return n
	
	def cantidadDeJugadores(self, estrategia, asimetriaAparente):
		todos = len(self.agents_by_breed[Jugadores])
		n = 0
		for i in self.agents_by_breed[Jugadores]:
			agente3 = self.agents_by_breed[Jugadores][i]
			if agente3.estrategia == estrategia and agente3.asimetriaAparente == asimetriaAparente:
				n = n + 1
		
		return n

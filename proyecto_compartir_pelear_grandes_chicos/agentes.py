from framework_mesa import Agent

import random

class Jugadores(Agent):

	edad = 0
	estrategia = "halcon"
	edadDeReplicacionYMuerte = 40
	puntos = 0
	
	def __init__(self, unique_id, pos, estrategia, asimetriaAparente, model):
		super().__init__(unique_id, model)
		self.pos = pos 
		self.edad = 0
		self.estrategia = estrategia
		self.asimetriaAparente = asimetriaAparente
		self.edadDeReplicacionYMuerte = 40
		self.puntos = 0
		self.puntajePorcentual = 0.0
		self.combatioContraAlguienEnEstaEpoca = False
	
	def step(self):
	
		self.edad = self.edad + 1
	
	def AsignarPuntajePorcentual(self, puntajePorcentual):
		self.puntajePorcentual = puntajePorcentual

	def ValorPuntajePorcentual(self):
		return self.puntajePorcentual


	def SumarPuntos(self, puntos):
	
		self.puntos = self.puntos + puntos

	def TotalDePuntos(self):
		return1 = self.puntos
		return return1
	
	def Edad(self):
		return1 = self.edad
		return return1
	
	def Estrategia(self):
		return1 = self.estrategia
		return return1
	
	def AsimetriaAparente(self):
		return1 = self.asimetriaAparente
		return return1
	
	def SetCombatioContraAlguienEnEstaEpoca(self, combatioContraAlguienEnEstaEpoca):
	
		self.combatioContraAlguienEnEstaEpoca = combatioContraAlguienEnEstaEpoca
	
	def GetCombatioContraAlguienEnEstaEpoca(self):
	
		return self.combatioContraAlguienEnEstaEpoca

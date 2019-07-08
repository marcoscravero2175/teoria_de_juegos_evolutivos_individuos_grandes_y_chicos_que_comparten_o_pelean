import random
def ResolucionDeConflictosEntreDosAgentes(agenteA, agenteB, valorDelRecurso, costeDeLesion, probabilidadDeQueElMayorGane1):

	#print("probabilidadDeQueElMayorGane1:"+str(probabilidadDeQueElMayorGane1))

	(posA0, posA1) = agenteA.pos
	(posB0, posB1) = agenteB.pos

	costoDePerderUnaPelea = round((-costeDeLesion), 2)
	puntosPorGanarUnaPelea = round((valorDelRecurso), 2)
	puntosGanadosPorCompartirElRecurso = round((valorDelRecurso/2), 2)
	sinPuntosPorRetirarse = 0
	puntosGanadosSinPelear = round((valorDelRecurso), 2)

	#(puntosPorGanarUnaPelea - costoDePerderUnaPelea-/2
	#puntosPorGanarUnaPelea = 1
	#costoDePerderUnaPelea = 0

	#probabilidadDeQueElMayorGane1 = 0.5
	pr = random.random()
	
	# agenteA:siempreEscala
	if agenteA.Estrategia() == "siempreEscala":

		# agenteA:siempreEscala y agenteB:nuncaEscala
		if agenteB.Estrategia() == "nuncaEscala":
			agenteA.SumarPuntos(puntosGanadosSinPelear)
			agenteB.SumarPuntos(sinPuntosPorRetirarse)
	
			#print("- Resultado de contienda entre " + agenteA.Estrategia() + "-" + agenteA.AsimetriaAparente() + " localizada en (" + str(posA0) + "," + str(posA1) + ") contra " + agenteB.Estrategia()  + "-" +  agenteB.AsimetriaAparente() + " localizado en (" + str(posB0) + "," + str(posB1) + ")")
			#print("  - Al primer jugador le sumo " + str(puntosGanadosSinPelear) + " resultado un total de " + str(agenteA.TotalDePuntos()))
			#print("  - Al segundo jugador le sumo " + str(sinPuntosPorRetirarse) + " resultado un total de " + str(agenteB.TotalDePuntos()))
			#print("")
	
		# agenteA:siempreEscala y agenteB:siempreEscala
		if agenteB.Estrategia() == "siempreEscala":


			# agenteA:siempreEscala y agenteB:siempreEscala
			# agenteA:grande y agenteB:grande
			if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "grande":
				if pr < probabilidadDeQueElMayorGane1:
					agenteA.SumarPuntos(costoDePerderUnaPelea)
					agenteB.SumarPuntos(puntosPorGanarUnaPelea)

				if pr >= probabilidadDeQueElMayorGane1:
					agenteA.SumarPuntos(puntosPorGanarUnaPelea)
					agenteB.SumarPuntos(costoDePerderUnaPelea)


			# agenteA:siempreEscala y agenteB:siempreEscala
			# agenteA:chico y agenteB:chico
			if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "chico":
				if pr < probabilidadDeQueElMayorGane1:
					agenteA.SumarPuntos(puntosPorGanarUnaPelea)
					agenteB.SumarPuntos(costoDePerderUnaPelea)

				if pr >= probabilidadDeQueElMayorGane1:
					agenteA.SumarPuntos(costoDePerderUnaPelea)
					agenteB.SumarPuntos(puntosPorGanarUnaPelea)

			# agenteA:siempreEscala y agenteB:siempreEscala
			# agenteA:chico y agenteB:grande
			if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "grande":
				print("agenteA.unique_id" + str(agenteA.unique_id) + "probabilidad grande " + str(pr)+" probabilidad grande " + str(probabilidadDeQueElMayorGane1))

				if pr < probabilidadDeQueElMayorGane1:
					agenteA.SumarPuntos(costoDePerderUnaPelea)
					agenteB.SumarPuntos(puntosPorGanarUnaPelea)

				if pr >= probabilidadDeQueElMayorGane1:
					agenteA.SumarPuntos(puntosPorGanarUnaPelea)
					agenteB.SumarPuntos(costoDePerderUnaPelea)

			# agenteA:siempreEscala y agenteB:siempreEscala
			# agenteA:grande y agenteB:chico
			if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "chico":
				print("agenteA.unique_id" + str(agenteA.unique_id) + "probabilidad grande " + str(pr)+" probabilidad grande " + str(probabilidadDeQueElMayorGane1))

				if pr < probabilidadDeQueElMayorGane1:
					agenteA.SumarPuntos(puntosPorGanarUnaPelea)
					agenteB.SumarPuntos(costoDePerderUnaPelea)

				if pr >= probabilidadDeQueElMayorGane1:
					agenteA.SumarPuntos(costoDePerderUnaPelea)
					agenteB.SumarPuntos(puntosPorGanarUnaPelea)

	
			#print("- Resultado de contienda entre " + agenteA.Estrategia() + "-" + agenteA.AsimetriaAparente() + " localizada en (" + str(posA0) + "," + str(posA1) + ") contra " + agenteB.Estrategia()  + "-" +  agenteB.AsimetriaAparente() + " localizado en (" + str(posB0) + "," + str(posB1) + ")")
			#print("  - Al primer jugador le sumo " + str(puntosPorGanarUnaPelea) + " resultado un total de " + str(agenteA.TotalDePuntos()))
			#print("  - Al segundo jugador le sumo " + str(costoDePerderUnaPelea) + " resultado un total de " + str(agenteB.TotalDePuntos()))
			#print("")
	
		# agenteA:siempreEscala y agenteB:escalaSiElOtroEsMasGrande
		if agenteB.Estrategia() == "escalaSiElOtroEsMasGrande":

			# agenteA:siempreEscala y agenteB:escalaSiElOtroEsMasGrande
			# agenteA:chico y agenteB:chico
			if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "chico":
				agenteA.SumarPuntos(puntosGanadosSinPelear)
				agenteB.SumarPuntos(sinPuntosPorRetirarse)

			# agenteA:siempreEscala y agenteB:escalaSiElOtroEsMasGrande
			# agenteA:chico y agenteB:grande
			if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "grande":
	
				agenteA.SumarPuntos(puntosGanadosSinPelear)
				agenteB.SumarPuntos(sinPuntosPorRetirarse)

			# agenteA:siempreEscala y agenteB:escalaSiElOtroEsMasGrande
			# agenteA:grande y agenteB:chico
			if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "chico":
	
				if pr <= probabilidadDeQueElMayorGane1:
					agenteA.SumarPuntos(puntosPorGanarUnaPelea)
					agenteB.SumarPuntos(costoDePerderUnaPelea)
	
				if pr > probabilidadDeQueElMayorGane1:
					agenteA.SumarPuntos(costoDePerderUnaPelea)
					agenteB.SumarPuntos(puntosPorGanarUnaPelea)
	
			# agenteA:siempreEscala y agenteB:escalaSiElOtroEsMasGrande
			# agenteA:grande y agenteB:grande
			if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "grande":
				agenteA.SumarPuntos(puntosGanadosSinPelear)
				agenteB.SumarPuntos(sinPuntosPorRetirarse)
	


		# agenteA:siempreEscala y agenteB:escalaSiElOtroEsMasChico
		if agenteB.Estrategia() == "escalaSiElOtroEsMasChico":

			# agenteA:siempreEscala y agenteB:escalaSiElOtroEsMasChico
			# agenteA:chico y agenteB:chico
			if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "chico":
				agenteA.SumarPuntos(puntosGanadosSinPelear)
				agenteB.SumarPuntos(sinPuntosPorRetirarse)

			# agenteA:siempreEscala y agenteB:escalaSiElOtroEsMasChico
			# agenteA:chico y agenteB:grande
			if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "grande":
	
				if pr <= probabilidadDeQueElMayorGane1:
					agenteA.SumarPuntos(costoDePerderUnaPelea)
					agenteB.SumarPuntos(puntosPorGanarUnaPelea)
	
				if pr > probabilidadDeQueElMayorGane1:
					agenteA.SumarPuntos(puntosPorGanarUnaPelea)
					agenteB.SumarPuntos(costoDePerderUnaPelea)


			# agenteA:siempreEscala y agenteB:escalaSiElOtroEsMasChico
			# agenteA:grande y agenteB:chico
			if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "chico":
	
				agenteA.SumarPuntos(puntosGanadosSinPelear)
				agenteB.SumarPuntos(sinPuntosPorRetirarse)
	
			# agenteA:siempreEscala y agenteB:escalaSiElOtroEsMasChico
			# agenteA:grande y agenteB:grande
			if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "grande":
				agenteA.SumarPuntos(puntosGanadosSinPelear)
				agenteB.SumarPuntos(sinPuntosPorRetirarse)



	# agenteA:nuncaEscala
	if agenteA.Estrategia() == "nuncaEscala":
	
		# agenteA:nuncaEscala y agenteB:nuncaEscala
		if agenteB.Estrategia() == "nuncaEscala":
			agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
			agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)
	
		# agenteA:nuncaEscala y agenteB:siempreEscala
		if agenteB.Estrategia() == "siempreEscala":
			agenteA.SumarPuntos(sinPuntosPorRetirarse)
			agenteB.SumarPuntos(puntosGanadosSinPelear)
	
		# agenteA:nuncaEscala y agenteB:escalaSiElOtroEsMasGrande
		if agenteB.Estrategia() == "escalaSiElOtroEsMasGrande":
	
			# agenteA:nuncaEscala y agenteB:escalaSiElOtroEsMasGrande
			# agenteA:chico y agenteB:chico
			if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "chico":
				agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
				agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)

			# agenteA:nuncaEscala y agenteB:escalaSiElOtroEsMasGrande
			# agenteA:chico y agenteB:grande
			if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "grande":
				agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
				agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)

			# agenteA:nuncaEscala y agenteB:escalaSiElOtroEsMasGrande
			# agenteA:grande y agenteB:chico
			if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "chico":
				agenteA.SumarPuntos(sinPuntosPorRetirarse)
				agenteB.SumarPuntos(puntosGanadosSinPelear)

			# agenteA:nuncaEscala y agenteB:escalaSiElOtroEsMasGrande
			# agenteA:grande y agenteB:grande
			if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "grande":
				agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
				agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)
	


		# agenteA:nuncaEscala y agenteB:escalaSiElOtroEsMasChico
		if agenteB.Estrategia() == "escalaSiElOtroEsMasChico":
	
			# agenteA:nuncaEscala y agenteB:escalaSiElOtroEsMasChico
			# agenteA:chico y agenteB:chico
			if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "chico":
				agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
				agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)

			# agenteA:nuncaEscala y agenteB:escalaSiElOtroEsMasChico
			# agenteA:chico y agenteB:grande
			if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "grande":
				agenteA.SumarPuntos(sinPuntosPorRetirarse)
				agenteB.SumarPuntos(puntosGanadosSinPelear)

			# agenteA:nuncaEscala y agenteB:escalaSiElOtroEsMasChico
			# agenteA:grande y agenteB:chico
			if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "chico":
				agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
				agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)

			# agenteA:nuncaEscala y agenteB:escalaSiElOtroEsMasChico
			# agenteA:grande y agenteB:grande
			if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "grande":
				agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
				agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)


	# agenteA:escalaSiElOtroEsMasGrande
	if agenteA.Estrategia() == "escalaSiElOtroEsMasGrande":

		# agenteA:escalaSiElOtroEsMasGrande y agenteB:nuncaEscala
		if agenteB.Estrategia() == "nuncaEscala":

			# agenteA:escalaSiElOtroEsMasGrande y agenteB:nuncaEscala
			# agenteA:chico y agenteB:chico
			if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "chico":
				agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
				agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)

			# agenteA:escalaSiElOtroEsMasGrande y agenteB:nuncaEscala
			# agenteA:chico y agenteB:grande
			if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "grande":
				agenteA.SumarPuntos(puntosGanadosSinPelear)
				agenteB.SumarPuntos(sinPuntosPorRetirarse)

			# agenteA:escalaSiElOtroEsMasGrande y agenteB:nuncaEscala
			# agenteA:grande y agenteB:chico
			if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "chico":
				agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
				agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)

			# agenteA:escalaSiElOtroEsMasGrande y agenteB:nuncaEscala
			# agenteA:grande y agenteB:grande
			if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "grande":
				agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
				agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)
	
		# agenteA:escalaSiElOtroEsMasGrande y agenteB:siempreEscala
		if agenteB.Estrategia() == "siempreEscala":

			# agenteA:escalaSiElOtroEsMasGrande y agenteB:siempreEscala
			# agenteA:chico y agenteB:chico
			if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "chico":
				agenteA.SumarPuntos(puntosGanadosSinPelear)
				agenteB.SumarPuntos(sinPuntosPorRetirarse)

			# agenteA:escalaSiElOtroEsMasGrande y agenteB:siempreEscala
			# agenteA:chico y agenteB:grande
			if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "grande":
				if pr <= probabilidadDeQueElMayorGane1:
					agenteA.SumarPuntos(puntosPorGanarUnaPelea)
					agenteB.SumarPuntos(costoDePerderUnaPelea)
	
				if pr > probabilidadDeQueElMayorGane1:
					agenteA.SumarPuntos(costoDePerderUnaPelea)
					agenteB.SumarPuntos(puntosPorGanarUnaPelea)

			# agenteA:escalaSiElOtroEsMasGrande y agenteB:siempreEscala
			# agenteA:grande y agenteB:chico
			if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "chico":
				agenteA.SumarPuntos(puntosGanadosSinPelear)
				agenteB.SumarPuntos(sinPuntosPorRetirarse)

			# agenteA:escalaSiElOtroEsMasGrande y agenteB:siempreEscala
			# agenteA:grande y agenteB:grande
			if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "grande":
				agenteA.SumarPuntos(puntosGanadosSinPelear)
				agenteB.SumarPuntos(sinPuntosPorRetirarse)
	
		# agenteA:escalaSiElOtroEsMasGrande y agenteB:escalaSiElOtroEsMasGrande
		if agenteB.Estrategia() == "escalaSiElOtroEsMasGrande":

			# agenteA:escalaSiElOtroEsMasGrande y agenteB:escalaSiElOtroEsMasGrande
			# agenteA:chico y agenteB:chico
			if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "chico":
				agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
				agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)

			# agenteA:escalaSiElOtroEsMasGrande y agenteB:escalaSiElOtroEsMasGrande
			# agenteA:chico y agenteB:grande
			if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "grande":
				agenteA.SumarPuntos(puntosGanadosSinPelear)
				agenteB.SumarPuntos(sinPuntosPorRetirarse)

			# agenteA:escalaSiElOtroEsMasGrande y agenteB:escalaSiElOtroEsMasGrande
			# agenteA:grande y agenteB:chico
			if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "chico":
				agenteA.SumarPuntos(sinPuntosPorRetirarse)
				agenteB.SumarPuntos(puntosGanadosSinPelear)

			# agenteA:escalaSiElOtroEsMasGrande y agenteB:escalaSiElOtroEsMasGrande
			# agenteA:grande y agenteB:grande
			if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "grande":
				agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
				agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)



		# agenteA:escalaSiElOtroEsMasGrande y agenteB:escalaSiElOtroEsMasChico
		if agenteB.Estrategia() == "escalaSiElOtroEsMasChico":

			# agenteA:escalaSiElOtroEsMasGrande y agenteB:escalaSiElOtroEsMasChico
			# agenteA:chico y agenteB:chico
			if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "chico":
				agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
				agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)

			# agenteA:escalaSiElOtroEsMasGrande y agenteB:escalaSiElOtroEsMasChico
			# agenteA:chico y agenteB:grande
			if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "grande":
				if pr <= probabilidadDeQueElMayorGane1:
					agenteA.SumarPuntos(costoDePerderUnaPelea)
					agenteB.SumarPuntos(puntosPorGanarUnaPelea)
	
				if pr > probabilidadDeQueElMayorGane1:
					agenteA.SumarPuntos(puntosPorGanarUnaPelea)
					agenteB.SumarPuntos(costoDePerderUnaPelea)

			# agenteA:escalaSiElOtroEsMasGrande y agenteB:escalaSiElOtroEsMasChico
			# agenteA:grande y agenteB:chico
			if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "chico":
				agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
				agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)

			# agenteA:escalaSiElOtroEsMasGrande y agenteB:escalaSiElOtroEsMasChico
			# agenteA:grande y agenteB:grande
			if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "grande":
				agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
				agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)




	# agenteA:escalaSiElOtroEsMasChico
	if agenteA.Estrategia() == "escalaSiElOtroEsMasChico":

		# agenteA:escalaSiElOtroEsMasChico y agenteB:nuncaEscala
		if agenteB.Estrategia() == "nuncaEscala":

			# agenteA:escalaSiElOtroEsMasChico y agenteB:nuncaEscala
			# agenteA:chico y agenteB:chico
			if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "chico":
				agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
				agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)

			# agenteA:escalaSiElOtroEsMasChico y agenteB:nuncaEscala
			# agenteA:chico y agenteB:grande
			if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "grande":
				agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
				agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)


			# agenteA:escalaSiElOtroEsMasChico y agenteB:nuncaEscala
			# agenteA:grande y agenteB:chico
			if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "chico":
				agenteA.SumarPuntos(puntosGanadosSinPelear)
				agenteB.SumarPuntos(sinPuntosPorRetirarse)

			# agenteA:escalaSiElOtroEsMasChico y agenteB:nuncaEscala
			# agenteA:grande y agenteB:grande
			if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "grande":
				agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
				agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)
	
		# agenteA:escalaSiElOtroEsMasChico y agenteB:siempreEscala
		if agenteB.Estrategia() == "siempreEscala":

			# agenteA:escalaSiElOtroEsMasChico y agenteB:siempreEscala
			# agenteA:chico y agenteB:chico
			if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "chico":
				agenteA.SumarPuntos(puntosGanadosSinPelear)
				agenteB.SumarPuntos(sinPuntosPorRetirarse)

			# agenteA:escalaSiElOtroEsMasChico y agenteB:siempreEscala
			# agenteA:chico y agenteB:grande
			if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "grande":
				agenteA.SumarPuntos(puntosGanadosSinPelear)
				agenteB.SumarPuntos(sinPuntosPorRetirarse)


			# agenteA:escalaSiElOtroEsMasChico y agenteB:siempreEscala
			# agenteA:grande y agenteB:chico
			if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "chico":
				if pr <= probabilidadDeQueElMayorGane1:
					agenteA.SumarPuntos(puntosPorGanarUnaPelea)
					agenteB.SumarPuntos(costoDePerderUnaPelea)
	
				if pr > probabilidadDeQueElMayorGane1:
					agenteA.SumarPuntos(costoDePerderUnaPelea)
					agenteB.SumarPuntos(puntosPorGanarUnaPelea)

			# agenteA:escalaSiElOtroEsMasChico y agenteB:siempreEscala
			# agenteA:grande y agenteB:grande
			if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "grande":
				agenteA.SumarPuntos(puntosGanadosSinPelear)
				agenteB.SumarPuntos(sinPuntosPorRetirarse)
	
		# agenteA:escalaSiElOtroEsMasChico y agenteB:escalaSiElOtroEsMasGrande
		if agenteB.Estrategia() == "escalaSiElOtroEsMasGrande":

			# agenteA:escalaSiElOtroEsMasChico y agenteB:escalaSiElOtroEsMasGrande
			# agenteA:chico y agenteB:chico
			if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "chico":
				agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
				agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)

			# agenteA:escalaSiElOtroEsMasChico y agenteB:escalaSiElOtroEsMasGrande
			# agenteA:chico y agenteB:grande
			if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "grande":
				agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
				agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)

			# agenteA:escalaSiElOtroEsMasChico y agenteB:escalaSiElOtroEsMasGrande
			# agenteA:grande y agenteB:chico
			if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "chico":

				if pr <= probabilidadDeQueElMayorGane1:
					agenteA.SumarPuntos(puntosPorGanarUnaPelea)
					agenteB.SumarPuntos(costoDePerderUnaPelea)
	
				if pr > probabilidadDeQueElMayorGane1:
					agenteA.SumarPuntos(costoDePerderUnaPelea)
					agenteB.SumarPuntos(puntosPorGanarUnaPelea)

			# agenteA:escalaSiElOtroEsMasChico y agenteB:escalaSiElOtroEsMasGrande
			# agenteA:grande y agenteB:grande
			if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "grande":
				agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
				agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)



		# agenteA:escalaSiElOtroEsMasChico y agenteB:escalaSiElOtroEsMasChico
		if agenteB.Estrategia() == "escalaSiElOtroEsMasChico":

			# agenteA:escalaSiElOtroEsMasChico y agenteB:escalaSiElOtroEsMasChico
			# agenteA:chico y agenteB:chico
			if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "chico":
				agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
				agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)

			# agenteA:escalaSiElOtroEsMasChico y agenteB:escalaSiElOtroEsMasChico
			# agenteA:chico y agenteB:grande
			if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "grande":
				agenteA.SumarPuntos(sinPuntosPorRetirarse)
				agenteB.SumarPuntos(puntosGanadosSinPelear)

			# agenteA:escalaSiElOtroEsMasChico y agenteB:escalaSiElOtroEsMasChico
			# agenteA:grande y agenteB:chico
			if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "chico":
				agenteA.SumarPuntos(puntosGanadosSinPelear)
				agenteB.SumarPuntos(sinPuntosPorRetirarse)

			# agenteA:escalaSiElOtroEsMasChico y agenteB:escalaSiElOtroEsMasChico
			# agenteA:grande y agenteB:grande
			if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "grande":
				agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
				agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)



	return (agenteA, agenteB, pr)

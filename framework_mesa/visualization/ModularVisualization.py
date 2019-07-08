from framework_mesa.visualization.UserParam import UserSettableParameter

from proyecto_compartir_pelear_grandes_chicos.agentes import Jugadores
from proyecto_compartir_pelear_grandes_chicos.model import Ambiente

import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os
import random
import numpy as np

import tornado.autoreload
import tornado.websocket
import tornado.escape
import tornado.gen
import webbrowser

# -*- coding: utf-8 -*-

"""
ModularServer
=============

A visualization server which renders a model via one or more elements.

The concept for the modular visualization server as follows:
A visualization is composed of VisualizationElements, each of which defines how
to generate some visualization from a model instance and render it on the
client. VisualizationElements may be anything from a simple text display to
a multilayered HTML5 canvas.

The actual server is launched with one or more VisualizationElements;
it runs the model object through each of them, generating data to be sent to
the client. The client page is also generated based on the JavaScript code
provided by each element.

This file consists of the following classes:

VisualizationElement: Parent class for all other visualization elements, with
                      the minimal necessary options.
PageHandler: The handler for the visualization page, generated from a template
             and built from the various visualization elements.
SocketHandler: Handles the websocket connection between the client page and
                the server.
ModularServer: The overall visualization application class which stores and
               controls the model and visualization instance.


ModularServer should *not* need to be subclassed on a model-by-model basis; it
should be primarily a pass-through for VisualizationElement subclasses, which
define the actual visualization specifics.

For example, suppose we have created two visualization elements for our model,
called canvasvis and graphvis; we would launch a server with:

    server = ModularServer(MyModel, [canvasvis, graphvis], name="My Model")
    server.launch()

The client keeps track of what step it is showing. Clicking the Step button in
the browser sends a message requesting the viz_state corresponding to the next
step position, which is then sent back to the client via the websocket.

The websocket protocol is as follows:
Each message is a JSON object, with a "type" property which defines the rest of
the structure.

Server -> Client:
    Send over the model state to visualize.
    Model state is a list, with each element corresponding to a div; each div
    is expected to have a render function associated with it, which knows how
    to render that particular data. The example below includes two elements:
    the first is data for a CanvasGrid, the second for a raw text display.

    {
    "type": "viz_state",
    "data": [{0:[ {"Shape": "circle", "x": 0, "y": 0, "r": 0.5,
                "Color": "#AAAAAA", "Filled": "true", "Layer": 0,
                "text": 'A', "text_color": "white" }]},
            "Shape Count: 1"]
    }

    Informs the client that the model is over.
    {"type": "end"}

    Informs the client of the current model's parameters
    {
    "type": "model_params",
    "params": 'dict' of model params, (i.e. {arg_1: val_1, ...})
    }

Client -> Server:
    Reset the model.
    TODO: Allow this to come with parameters
    {
    "type": "reset"
    }

    Get a given state.
    {
    "type": "get_step",
    "step:" index of the step to get.
    }

    Submit model parameter updates
    {
    "type": "submit_params",
    "param": name of model parameter
    "value": new value for 'param'
    }

    Get the model's parameters
    {
    "type": "get_params"
    }

"""

# Suppress several pylint warnings for this file.
# Attributes being defined outside of init is a Tornado feature.
# pylint: disable=attribute-defined-outside-init


class HomePage(tornado.web.RequestHandler):
	def get(self):

		distancia = 0
		if self.get_argument('distancia', None) != None:
			distancia = int(self.get_argument('distancia', None))
		print("distancia:" + str(distancia))

		self.render('homePage.html')


class RealizaUnaSimulacionMuestraEvolucion(tornado.web.RequestHandler):
	def get(self):

		elements = self.application.visualization_elements
		for i, element in enumerate(elements):
			print(element)
			element.index = i
			print("element.index:" + str(element.index))
		self.render("realizaUnaSimulacionMuestraEvolucion.html", port=self.application.port,
		            model_name=self.application.model_name,
		            description=self.application.description,
		            package_includes=self.application.package_includes,
		            local_includes=self.application.local_includes,
		            scripts=self.application.js_code)


class RealizaVariasSimulacionesCalculaEstadisticos(tornado.web.RequestHandler):
	def get(self):

		distanciaMaximaVecinos = 20

		cantidadNuncaEscalaChicosInicial = 0
		cantidadNuncaEscalaGrandesInicial = 0
		cantidadSiempreEscalaChicosInicial = 0
		cantidadSiempreEscalaGrandesInicial = 0
		cantidadEscalaSiElOtroEsMasGrandeChicosInicial = 5
		cantidadEscalaSiElOtroEsMasGrandeGrandesInicial = 0
		cantidadEscalaSiElOtroEsMasChicoChicosInicial = 0
		cantidadEscalaSiElOtroEsMasChicoGrandesInicial = 5

		cantidadSiempreEscalaGrandes = cantidadSiempreEscalaGrandesInicial
		cantidadSiempreEscalaChicos = cantidadSiempreEscalaChicosInicial
		cantidadNuncaEscalaGrandes = cantidadNuncaEscalaGrandesInicial
		cantidadNuncaEscalaChicos = cantidadNuncaEscalaChicosInicial
		cantidadEscalaSiElOtroEsMasGrandeGrandes = cantidadEscalaSiElOtroEsMasGrandeGrandesInicial
		cantidadEscalaSiElOtroEsMasGrandeChicos = cantidadEscalaSiElOtroEsMasGrandeChicosInicial
		cantidadEscalaSiElOtroEsMasChicoGrandes = cantidadEscalaSiElOtroEsMasChicoGrandesInicial
		cantidadEscalaSiElOtroEsMasChicoChicos = cantidadEscalaSiElOtroEsMasChicoChicosInicial

		valorDelRecurso = 5
		costoDeLesion = 10
		probabilidadDeQueElMayorGane = 50
		edadDeReproduccion = 1
		cantidadDeSimulaciones = 10
		cantidadDePasos = 20

		if self.get_argument('distanciaMaximaVecinos', None) != None:
			distanciaMaximaVecinos = int(self.get_argument('distanciaMaximaVecinos', None))


		if self.get_argument('cantidadSiempreEscalaChicosInicial', None) != None:
			cantidadSiempreEscalaChicosInicial = int(self.get_argument('cantidadSiempreEscalaChicosInicial', None))

		if self.get_argument('cantidadSiempreEscalaGrandesInicial', None) != None:
			cantidadSiempreEscalaGrandesInicial = int(self.get_argument('cantidadSiempreEscalaGrandesInicial', None))

		if self.get_argument('cantidadNuncaEscalaChicosInicial', None) != None:
			cantidadNuncaEscalaChicosInicial = int(self.get_argument('cantidadNuncaEscalaChicosInicial', None))

		if self.get_argument('cantidadNuncaEscalaGrandesInicial', None) != None:
			cantidadNuncaEscalaGrandesInicial = int(self.get_argument('cantidadNuncaEscalaGrandesInicial', None))

		if self.get_argument('cantidadEscalaSiElOtroEsMasGrandeChicosInicial', None) != None:
			cantidadEscalaSiElOtroEsMasGrandeChicosInicial = int(self.get_argument('cantidadEscalaSiElOtroEsMasGrandeChicosInicial', None))

		if self.get_argument('cantidadEscalaSiElOtroEsMasGrandeGrandesInicial', None) != None:
			cantidadEscalaSiElOtroEsMasGrandeGrandesInicial = int(self.get_argument('cantidadEscalaSiElOtroEsMasGrandeGrandesInicial', None))

		if self.get_argument('cantidadEscalaSiElOtroEsMasChicoChicosInicial', None) != None:
			cantidadEscalaSiElOtroEsMasChicoChicosInicial = int(self.get_argument('cantidadEscalaSiElOtroEsMasChicoChicosInicial', None))

		if self.get_argument('cantidadEscalaSiElOtroEsMasChicoGrandesInicial', None) != None:
			cantidadEscalaSiElOtroEsMasChicoGrandesInicial = int(self.get_argument('cantidadEscalaSiElOtroEsMasChicoGrandesInicial', None))

		if self.get_argument('valorDelRecurso', None) != None:
			valorDelRecurso = int(self.get_argument('valorDelRecurso', None))

		if self.get_argument('costoDeLesion', None) != None:
			costoDeLesion = int(self.get_argument('costoDeLesion', None))

		if self.get_argument('probabilidadDeQueElMayorGane', None) != None:
			probabilidadDeQueElMayorGane = int(self.get_argument('probabilidadDeQueElMayorGane', None))

		if self.get_argument('edadDeReproduccion', None) != None:
			edadDeReproduccion = int(self.get_argument('edadDeReproduccion', None))

		if self.get_argument('CantidadDeSimulaciones', None) != None:
			cantidadDeSimulaciones = int(self.get_argument('CantidadDeSimulaciones', None))

		if self.get_argument('CantidadDePasos', None) != None:
			cantidadDePasos = int(self.get_argument('CantidadDePasos', None))

		alto = 20
		ancho = 20
		
		listaDePorcentajes1 = []
		listaDePorcentajes2 = []
		porcentajesStr = ""

		cantidadSiempreEscalaGrandesMedia = 0
		cantidadSiempreEscalaChicosMedia = 0
		cantidadNuncaEscalaGrandesMedia = 0
		cantidadNuncaEscalaChicosMedia = 0
		cantidadEscalaSiElOtroEsMasGrandeGrandesMedia = 0
		cantidadEscalaSiElOtroEsMasGrandeChicosMedia = 0
		cantidadEscalaSiElOtroEsMasChicoGrandesMedia = 0
		cantidadEscalaSiElOtroEsMasChicoChicosMedia = 0

		for i in range(int(cantidadDeSimulaciones)):

			cantidadSiempreEscalaGrandes = cantidadSiempreEscalaGrandesInicial
			cantidadSiempreEscalaChicos = cantidadSiempreEscalaChicosInicial
			cantidadNuncaEscalaGrandes = cantidadNuncaEscalaGrandesInicial
			cantidadNuncaEscalaChicos = cantidadNuncaEscalaChicosInicial
			cantidadEscalaSiElOtroEsMasGrandeGrandes = cantidadEscalaSiElOtroEsMasGrandeGrandesInicial
			cantidadEscalaSiElOtroEsMasGrandeChicos = cantidadEscalaSiElOtroEsMasGrandeChicosInicial
			cantidadEscalaSiElOtroEsMasChicoGrandes = cantidadEscalaSiElOtroEsMasChicoGrandesInicial
			cantidadEscalaSiElOtroEsMasChicoChicos = cantidadEscalaSiElOtroEsMasChicoChicosInicial

			#porcentajesStr = porcentajesStr + "(" + str(alto)  + "," + str(ancho)  + "," + str(distanciaMaximaVecinos)  + "," + str(cantidadDeHalcones)  + "," + str(cantidadDeParadojicos)  + "," + str(cantidadDePalomas)  + "," + str(valorDelRecurso)  + "," + str(costeDeLesion)  + "," + str(probabilidadDeQueElMayorGane1)  + "," + str(edadDeReproduccion)  + ")<br>"

			ambiente = Ambiente( 
				alto,
				ancho,
				distanciaMaximaVecinos, 
				cantidadNuncaEscalaChicos,
				cantidadNuncaEscalaGrandes,
				cantidadSiempreEscalaChicos,
				cantidadSiempreEscalaGrandes,
				cantidadEscalaSiElOtroEsMasGrandeChicos,
				cantidadEscalaSiElOtroEsMasGrandeGrandes,
				cantidadEscalaSiElOtroEsMasChicoChicos,
				cantidadEscalaSiElOtroEsMasChicoGrandes,
				valorDelRecurso,
				costoDeLesion,
				probabilidadDeQueElMayorGane,
				edadDeReproduccion
				)	
		
			porcentajesStr = porcentajesStr + "<b>Simulacion: "+ str(i+1) + "</b><br>"
			porcentajesStr = porcentajesStr + "<br><table border='1'><tr><i><td>Paso </td><td>Chico_NuncaEscala</td><td>Grande_NuncaEscala</td><td>Chico_SiempreEscala</td><td>Grande_SiempreEscala</td><td>Chico_EscalaSoloSiElOtroEsMasGrande</td><td>Grande_EscalaSoloSiElOtroEsMasGrande</td><td>Chico_EscalaSoloSiElOtroEsMasChico</td><td>Grande_EscalaSoloSiElOtroEsMasChico</td></i></tr>"
		
			for j in range(int(cantidadDePasos)):
				ambiente.step()

				cantidadSiempreEscalaGrandes = ambiente.schedule.cantidadDeJugadores("siempreEscala", "grande")
				cantidadSiempreEscalaChicos = ambiente.schedule.cantidadDeJugadores("siempreEscala", "chico")
				cantidadNuncaEscalaGrandes = ambiente.schedule.cantidadDeJugadores("nuncaEscala", "grande")
				cantidadNuncaEscalaChicos = ambiente.schedule.cantidadDeJugadores("nuncaEscala", "chico")
				cantidadEscalaSiElOtroEsMasGrandeGrandes = ambiente.schedule.cantidadDeJugadores("escalaSiElOtroEsMasGrande", "grande")
				cantidadEscalaSiElOtroEsMasGrandeChicos = ambiente.schedule.cantidadDeJugadores("escalaSiElOtroEsMasGrande", "chico")
				cantidadEscalaSiElOtroEsMasChicoGrandes = ambiente.schedule.cantidadDeJugadores("escalaSiElOtroEsMasChico", "grande")
				cantidadEscalaSiElOtroEsMasChicoChicos = ambiente.schedule.cantidadDeJugadores("escalaSiElOtroEsMasChico", "chico")
		
				porcentajes =	(
						cantidadSiempreEscalaGrandes, 
						cantidadSiempreEscalaChicos,
						cantidadNuncaEscalaGrandes,
						cantidadNuncaEscalaChicos,
						cantidadEscalaSiElOtroEsMasGrandeGrandes,
						cantidadEscalaSiElOtroEsMasGrandeChicos,
						cantidadEscalaSiElOtroEsMasChicoGrandes,
						cantidadEscalaSiElOtroEsMasChicoChicos
						)
				porcentajesStr = porcentajesStr + "<tr><td><br><i>  "+ str(j + 1) + " </i></td><td>"+ str(cantidadNuncaEscalaChicos) +"</td><td>"+str(cantidadNuncaEscalaGrandes)+"</td><td>"+ str(cantidadSiempreEscalaChicos) +"</td><td>"+str(cantidadSiempreEscalaGrandes)+"</td><td>"+ str(cantidadEscalaSiElOtroEsMasGrandeChicos) +"</td><td>"+str(cantidadEscalaSiElOtroEsMasGrandeGrandes)+"</td><td>"+ str(cantidadEscalaSiElOtroEsMasChicoChicos) +"</td><td>"+str(cantidadEscalaSiElOtroEsMasChicoGrandes)+"</td></tr>"
		
				print(porcentajesStr)
			
				listaDePorcentajes1 = porcentajes
				listaDePorcentajes2.append(porcentajes)

			porcentajesStr = porcentajesStr + "</table>"

			cantidadSiempreEscalaGrandesMedia = cantidadSiempreEscalaGrandesMedia + cantidadSiempreEscalaGrandes
			cantidadSiempreEscalaChicosMedia = cantidadSiempreEscalaChicosMedia + cantidadSiempreEscalaChicos
			cantidadNuncaEscalaGrandesMedia = cantidadNuncaEscalaGrandesMedia + cantidadNuncaEscalaGrandes
			cantidadNuncaEscalaChicosMedia = cantidadNuncaEscalaChicosMedia + cantidadNuncaEscalaChicos
			cantidadEscalaSiElOtroEsMasGrandeGrandesMedia = cantidadEscalaSiElOtroEsMasGrandeGrandesMedia + cantidadEscalaSiElOtroEsMasGrandeGrandes
			cantidadEscalaSiElOtroEsMasGrandeChicosMedia = cantidadEscalaSiElOtroEsMasGrandeChicosMedia + cantidadEscalaSiElOtroEsMasGrandeChicos
			cantidadEscalaSiElOtroEsMasChicoGrandesMedia = cantidadEscalaSiElOtroEsMasChicoGrandesMedia + cantidadEscalaSiElOtroEsMasChicoGrandes
			cantidadEscalaSiElOtroEsMasChicoChicosMedia = cantidadEscalaSiElOtroEsMasChicoChicosMedia + cantidadEscalaSiElOtroEsMasChicoChicos

			porcentajesStr = porcentajesStr + "<br><br><br>"

		cantidadSiempreEscalaGrandesMedia = cantidadSiempreEscalaGrandesMedia / cantidadDeSimulaciones
		cantidadSiempreEscalaChicosMedia = cantidadSiempreEscalaChicosMedia / cantidadDeSimulaciones
		cantidadNuncaEscalaGrandesMedia = cantidadNuncaEscalaGrandesMedia / cantidadDeSimulaciones
		cantidadNuncaEscalaChicosMedia = cantidadNuncaEscalaChicosMedia / cantidadDeSimulaciones
		cantidadEscalaSiElOtroEsMasGrandeGrandesMedia = cantidadEscalaSiElOtroEsMasGrandeGrandesMedia / cantidadDeSimulaciones
		cantidadEscalaSiElOtroEsMasGrandeChicosMedia = cantidadEscalaSiElOtroEsMasGrandeChicosMedia / cantidadDeSimulaciones
		cantidadEscalaSiElOtroEsMasChicoGrandesMedia = cantidadEscalaSiElOtroEsMasChicoGrandesMedia / cantidadDeSimulaciones
		cantidadEscalaSiElOtroEsMasChicoChicosMedia = cantidadEscalaSiElOtroEsMasChicoChicosMedia / cantidadDeSimulaciones

		porcentajesStr = porcentajesStr + "<br><br><br>"

		porcentajesStr = porcentajesStr + "<b>Cantidades medias de "+ str(i+1) + " simulaciones, " +  str(cantidadDePasos) + " pasos cada una de las simulaciones</b><br>"
		porcentajesStr = porcentajesStr + "<br><table border='1'><tr><i><td>-</td><td>Chico_NuncaEscala</td><td>Grande_NuncaEscala</td><td>Chico_SiempreEscala</td><td>Grande_SiempreEscala</td><td>Chico_EscalaSoloSiElOtroEsMasGrande</td><td>Grande_EscalaSoloSiElOtroEsMasGrande</td><td>Chico_EscalaSoloSiElOtroEsMasChico</td><td>Grande_EscalaSoloSiElOtroEsMasChico</td></i></tr>"

		porcentajesStr = porcentajesStr + "<tr><td> - </td><td>" + str(cantidadNuncaEscalaChicosMedia) + "</td><td>" + str(cantidadNuncaEscalaGrandesMedia) + "</td><td>" +str(cantidadSiempreEscalaChicosMedia) + "</td><td>" + str(cantidadSiempreEscalaGrandesMedia) + "</td><td>" +  str(cantidadEscalaSiElOtroEsMasGrandeChicosMedia) + "</td><td>" + str(cantidadEscalaSiElOtroEsMasGrandeGrandesMedia) + "</td><td>" +  str(cantidadEscalaSiElOtroEsMasChicoChicosMedia) + "</td><td>" + str(cantidadEscalaSiElOtroEsMasChicoGrandesMedia) +"</td></table>"

		self.render('realizaVariasSimulacionesCalculaEstadisticos.html', porcentajesStr2=porcentajesStr, distanciaMaximaVecinos=distanciaMaximaVecinos, cantidadSiempreEscalaChicosInicial=cantidadSiempreEscalaChicosInicial, cantidadSiempreEscalaGrandesInicial=cantidadSiempreEscalaGrandesInicial, cantidadNuncaEscalaChicosInicial=cantidadNuncaEscalaChicosInicial, cantidadNuncaEscalaGrandesInicial=cantidadNuncaEscalaGrandesInicial, cantidadEscalaSiElOtroEsMasGrandeChicosInicial=cantidadEscalaSiElOtroEsMasGrandeChicosInicial, cantidadEscalaSiElOtroEsMasGrandeGrandesInicial=cantidadEscalaSiElOtroEsMasGrandeGrandesInicial, cantidadEscalaSiElOtroEsMasChicoChicosInicial=cantidadEscalaSiElOtroEsMasChicoChicosInicial, cantidadEscalaSiElOtroEsMasChicoGrandesInicial=cantidadEscalaSiElOtroEsMasChicoGrandesInicial, valorDelRecurso=valorDelRecurso, costoDeLesion=costoDeLesion, probabilidadDeQueElMayorGane = probabilidadDeQueElMayorGane, edadDeReproduccion=edadDeReproduccion, CantidadDeSimulaciones = cantidadDeSimulaciones, CantidadDePasos = cantidadDePasos)

class VisualizationElement:
    """
    Defines an element of the visualization.

    Attributes:
        package_includes: A list of external JavaScript files to include that
                          are part of the Mesa packages.
        local_includes: A list of JavaScript files that are local to the
                        directory that the server is being run in.
        js_code: A JavaScript code string to instantiate the element.

    Methods:
        render: Takes a model object, and produces JSON data which can be sent
                to the client.

    """

    package_includes = []
    local_includes = []
    js_code = ''
    render_args = {}

    def __init__(self):
        pass

    def render(self, model):
        """ Build visualization data from a model object.

        Args:
            model: A model object

        Returns:
            A JSON-ready object.

        """
        return "<b>VisualizationElement goes here</b>."

# =============================================================================

class SocketHandler(tornado.websocket.WebSocketHandler):
    """ Handler for websocket. """
    def open(self):
        if self.application.verbose:
            print("Socket opened!")

    def check_origin(self, origin):
        return True

    @property
    def viz_state_message(self):
        return {
            "type": "viz_state",
            "data": self.application.render_model()
        }

    def on_message(self, message):
        """ Receiving a message from the websocket, parse, and act accordingly.

        """
        if self.application.verbose:
            print(message)
        msg = tornado.escape.json_decode(message)

        if msg["type"] == "get_step":
            if not self.application.model.running:
                self.write_message({"type": "end"})
            else:
                self.application.model.step()
                self.write_message(self.viz_state_message)

        elif msg["type"] == "reset":
            self.application.reset_model()
            self.write_message(self.viz_state_message)

        elif msg["type"] == "submit_params":
            param = msg["param"]
            value = msg["value"]

            # Is the param editable?
            if param in self.application.user_params:
                if isinstance(self.application.model_kwargs[param], UserSettableParameter):
                    self.application.model_kwargs[param].value = value
                else:
                    self.application.model_kwargs[param] = value

        elif msg["type"] == "get_params":
            self.write_message({
                "type": "model_params",
                "params": self.application.user_params
            })

        else:
            if self.application.verbose:
                print("Unexpected message!")


class ModularServer(tornado.web.Application):
    """ Main visualization application. """
    verbose = True

    port = 8521  # Default port to listen on
    #max_steps = 100000
    max_steps = 100

    # Handlers and other globals:
    homePage = (r"/", HomePage)
    realizaVariasSimulacionesCalculaEstadisticos = (r"/realizaVariasSimulacionesCalculaEstadisticos", RealizaVariasSimulacionesCalculaEstadisticos)
    realizaUnaSimulacionMuestraEvolucion = (r'/realizaUnaSimulacionMuestraEvolucion', RealizaUnaSimulacionMuestraEvolucion)
    socket_handler = (r'/ws', SocketHandler)
    static_handler = (r'/static/(.*)', tornado.web.StaticFileHandler,
                      {"path": os.path.dirname(__file__) + "/templates"})
    local_handler = (r'/local/(.*)', tornado.web.StaticFileHandler,
                     {"path": ''})

    handlers = [homePage, realizaVariasSimulacionesCalculaEstadisticos, realizaUnaSimulacionMuestraEvolucion, socket_handler, static_handler, local_handler]

    settings = {"debug": True,
                "autoreload": False,
		"autoescape": None,
                "template_path":  os.path.dirname(__file__) + "/templates"}

    EXCLUDE_LIST = ('width', 'height',)

    def __init__(self, model_cls, visualization_elements, name="Mesa Model",
                 model_params={}):
        """ Create a new visualization server with the given elements. """
        # Prep visualization elements:
        self.visualization_elements = visualization_elements
        self.package_includes = set()
        self.local_includes = set()
        self.js_code = []
        for element in self.visualization_elements:
            for include_file in element.package_includes:
                self.package_includes.add(include_file)
            for include_file in element.local_includes:
                self.local_includes.add(include_file)
            self.js_code.append(element.js_code)

        # Initializing the model
        self.model_name = name
        self.model_cls = model_cls
        self.description = 'No description available'
        if hasattr(model_cls, 'description'):
            self.description = model_cls.description
        elif model_cls.__doc__ is not None:
            self.description = model_cls.__doc__

        self.model_kwargs = model_params
        self.reset_model()

        # Initializing the application itself:
        super().__init__(self.handlers, **self.settings)

    @property
    def user_params(self):
        result = {}
        for param, val in self.model_kwargs.items():
            if isinstance(val, UserSettableParameter):
                result[param] = val.json

        return result

    def reset_model(self):
        """ Reinstantiate the model object, using the current parameters. """

        model_params = {}
        for key, val in self.model_kwargs.items():
            if isinstance(val, UserSettableParameter):
                if val.param_type == 'static_text':    # static_text is never used for setting params
                    continue
                model_params[key] = val.value
            else:
                model_params[key] = val

        self.model = self.model_cls(**model_params)

    def render_model(self):
        """ Turn the current state of the model into a dictionary of
        visualizations

        """
        visualization_state = []
        for element in self.visualization_elements:
            element_state = element.render(self.model)
            visualization_state.append(element_state)
        return visualization_state

    def launch(self, port=None):
        """ Run the app. """
        startLoop = not tornado.ioloop.IOLoop.initialized()
        if port is not None:
            self.port = port
        url = 'http://127.0.0.1:{PORT}'.format(PORT=self.port)
        print('Interface starting at {url}'.format(url=url))
        self.listen(self.port)
        webbrowser.open(url)
        tornado.autoreload.start()
        if startLoop:
            tornado.ioloop.IOLoop.instance().start()

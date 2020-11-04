import os

from flask import Flask, request, render_template
from lib import getRandomData
from lib.findPath import Path

import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import json

def create_app( test_config = None ) :
	# create and configure the app
	app = Flask( __name__, instance_relative_config = True )
	app.config.from_mapping(
		SECRET_KEY = 'dev',
		DATABASE   = os.path.join( app.instance_path, 'flaskr.sqlite' ),
	)

	if test_config is None :
		# load the instance config, if it exists, when not testing
		app.config.from_pyfile( 'config.py', silent = True )
	else :
		# load the test config if passed in
		app.config.from_mapping( test_config )

	# ensure the instance folder exists
	try :
		os.makedirs( app.instance_path )
	except OSError :
		pass

	# a simple page that displays the optimal path for a drone to take
	@app.route( '/find-path' )
	def display_path() :
		path = Path()
		path.findOverallPath()
		fieldFloor = path.getFieldFloor()
		pathCoords = path.getFinalPathCoords()
		xs = [ c[0] for c in pathCoords ]
		ys = [ c[1] for c in pathCoords ]
		zs = [ c[2] for c in pathCoords ]
		Z = [item for sublist in fieldFloor for item in sublist]
		nx, ny = len( fieldFloor ), len( Z )
		X = [ [i] * nx for i in range(nx) ]
		X = [item for sublist in X for item in sublist]
		Y = [ i % len(fieldFloor) for i in range(ny) ]
		itemLocations = path.getItemLocations()
		finalLocation = itemLocations[0]
		plotterObj = {
			'x':		X,
			'y': 		Y,
			'z': 		Z,
			'xs':		xs,
			'ys': 		ys,
			'zs': 		zs,
			'finalX': 	finalLocation[0],
			'finalY': 	finalLocation[1],
			'finalZ': 	finalLocation[2]
		}
		return render_template( 'basic-form.html', plot = plotterObj )

	return app




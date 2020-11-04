import os

from flask import Flask, request, render_template
from lib import getRandomData
from lib.findPath import Path

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io

import numpy as np
from matplotlib import cm

import plotly.graph_objects as go

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
		return render_template( 'basic-form.html' )

	def create_figure( xs, ys, zs, x, y, z, itemLocation ) :
		fig = Figure()
		ax = fig.add_subplot( 111, projection = '3d' )
		ax.plot_wireframe(x, y, z)
		ax.scatter( [ itemLocation[0] ], [ itemLocation[1] ], itemLocation[2], color='purple' )
		ax.plot( xs, ys, zs, color = 'r' )
		return fig

	@app.route( '/find-path', methods = [ 'POST' ] )
	def dsiplay_path_post() :
		fig = go.Figure(go.Surface(
			contours = {
				"x": {"show": True, "start": 1.5, "end": 2, "size": 0.04, "color":"white"},
				"z": {"show": True, "start": 0.5, "end": 0.8, "size": 0.05}
			},
			x = [1,2,3,4,5],
			y = [1,2,3,4,5],
			z = [
				[0, 1, 0, 1, 0],
				[1, 0, 1, 0, 1],
				[0, 1, 0, 1, 0],
				[1, 0, 1, 0, 1],
				[0, 1, 0, 1, 0]
			]))
		fig.update_layout(
				scene = {
					"xaxis": {"nticks": 20},
					"zaxis": {"nticks": 4},
					'camera_eye': {"x": 0, "y": -1, "z": 0.5},
					"aspectratio": {"x": 1, "y": 1, "z": 0.2}
				})
		return render_template( 'basic-form.html', plot = fig )
	# def display_path_post() :
	# 	path = Path()
	# 	path.findOverallPath()
	# 	fieldFloor = path.getFieldFloor()
	# 	pathCoords = path.getFinalPathCoords()
	# 	pathString = path.getFinalPathString()
	# 	timeCost = path.getOverallTimeCost()
	# 	itemLocations = path.getItemLocations()
	# 	xs = [ c[0] for c in pathCoords ]
	# 	ys = [ c[1] for c in pathCoords ]
	# 	zs = [ c[2] for c in pathCoords ]

	# 	nx, ny = len( fieldFloor ), len( fieldFloor )
	# 	X = np.array( [ [i] * nx for i in range(ny) ] ).ravel()
	# 	Y = np.array( [ i for i in range(nx) ] * ny )
	# 	Z = np.array( fieldFloor ).flatten()

	# 	x = np.reshape( X, ( 10, 10 ) )
	# 	y = np.reshape( Y, ( 10, 10 ) )
	# 	z = np.reshape( Z, ( 10, 10 ) )

	# 	fig = create_figure( xs, ys, zs, x, y, z, itemLocations[0] )
	# 	output = io.BytesIO()
	# 	FigureCanvas( fig ).print_png( output )
	# 	return Response( output.getvalue(), mimetype = 'image/png' ) 

	return app




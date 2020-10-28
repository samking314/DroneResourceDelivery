import os

from flask import Flask, request, render_template
# import sys
# sys.path.append('../')
from lib import getRandomData
from lib.findPath import Path

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

	@app.route( '/find-path', methods = [ 'POST' ] )
	def display_path_post() :
		path = Path()
		path.findOverallPath()
		fieldFloor = path.getFieldFloor()
		pathString = path.getFinalPathString()
		timeCost = path.getOverallTimeCost()
		return str( str( pathString ) + " And your total cost was: " + str( timeCost ) )

	return app
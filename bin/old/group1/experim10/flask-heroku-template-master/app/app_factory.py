# import necessary libraries
import os
from flask import Flask, render_template, jsonify, request, redirect, Response
from flask_sqlalchemy import SQLAlchemy
from app import config, data_models
from app.extensions import db
import pandas as pd

def buildApp():
    # Flask "app" Setup
    flask_app = Flask(__name__)
    

    # *********************************************
    # ************** Database Setup ***************
    # *********************************************
    # Check for enviroment variable DATABASE_URL
    # If it doesn't exist use DATABASE_URL from config.py

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or config.DATABASE_URL
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Attach db to Flask app so Flask handels db session managment and other good things
    db.init_app(flask_app)
    # Create database tables based on the model definitions in data_models.py
    db.create_all(app=flask_app)

    # Load ORM information from data_models.py, and create any missing tables

    # Add URL routes to flask app 
    # For larger Flask applications with many routes consider using blueprints
    # http://flask.pocoo.org/docs/1.0/blueprints/

    # *********************************************
    # ************** WEB PAGES ********************
    # *********************************************

    @flask_app.route("/")
    def renderHome():
        return render_template("index.html")

    @flask_app.route("/map")
    def renderMap():
        return render_template("map.html")

    @flask_app.route("/dashboard")
    def renderDashboard():
        return render_template("dashboard.html")


    # *********************************************
    # ************** API ENDPOINTS ****************
    # *********************************************

    @flask_app.route("/api/l-stations")
    def lStationsJson():
        df = pd.read_sql("""
            select  * 
            from    l_stops
            """, db.engine)
        json_str = df.to_json(orient="records")
        return Response(response=json_str, status=200, mimetype='application/json')

    return flask_app

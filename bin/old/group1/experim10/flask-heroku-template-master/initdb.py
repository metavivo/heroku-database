# **************************************************************
# **** THIS SCRIPT CREATES A NEW DB, RUN WITH CARE FRIENDS *****
# **************************************************************

run_script = input("\nAre you sure you want to run this script? (Y)es or (N)o\nWARNING: If you have an existing database, it will be deleted\n\n> ")
if "y" not in run_script.lower():
    exit(0)

import os
import pandas as pd
# Import database settings from flask_app file
from app import flask_app
from app.extensions import db

# This "with" allows us to borrow our db setting and data models from the flask app
with flask_app.app_context():

    print("Delete existing tables")
    db.drop_all()
    # Create database tables based on the model definitions in data_models.py
    print("Creating new tables based on data model")
    db.create_all()

    # Import a csv file into a pandas dataframe, clean, then save the results to a database table
    path_for_this_file = os.path.dirname(__file__)
    file_name = "l_stops.csv"
    absolute_csv_path = os.path.join(path_for_this_file, "data_files", file_name)
    db_table_name = "l_stops"

    print(f"Importing csv {absolute_csv_path}")
    df = pd.read_csv(absolute_csv_path)

    print("\nClean and transform ....\n")
    # CLEAN
    # TRANSFORM
    print(df.head())

    print(f"Saving results to {db_table_name}")
    # Save results from import as 
    df.to_sql(db_table_name, con=db.engine, if_exists="replace", chunksize=20000)
    print("DONE!")

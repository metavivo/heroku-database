#!/bin/bash
# Set location of flask app via enviroment variable FLASK_APP
export FLASK_APP=app:flask_app
# Check command line arguments for "dev" flag
if [[ $1 == "dev" ]]; then
    # Set enviroment variable FLASK_ENV to development (for auto reload)
    export FLASK_ENV=development
fi
# Run flask
flask run
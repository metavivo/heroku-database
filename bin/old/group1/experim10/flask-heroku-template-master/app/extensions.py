# To avoid circular imports we instantiate our database, and email objects here.
# Generally speaking this is best practice. It allows us to share common objects 
# accross "scripts" like initdb and "apps" like flask.

from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()
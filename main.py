from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    #using a list comprehension and multiple assignment
    #to grab the environment variables we need

    #creating the flask app object - the core of our app!
    app = Flask(__name__)

    #configuring our app:
    app.config.from_object("config.app_config")

    #creating our database object, allowing us to use our ORM
    db.init_app(app)
    #creating our marshmallow object, allowing us to use schemas
    ma.init_app(app)

    #import the controllers and activate the blueprints
    from controllers import registerable_controllers
    
    for controller in registerable_controllers:
        app.register_blueprint(controller)

    return app



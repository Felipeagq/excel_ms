from abc import abstractproperty
from flask import Flask 
from .settings import settings

def create_app(setting_name:str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(settings[setting_name])
    settings[setting_name].init_app(app)

    from .commom import error_handlers
    error_handlers(app)

    from .routes import index
    index.index(app,"v0.0.1")


    return app

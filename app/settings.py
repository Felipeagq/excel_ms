from dotenv import load_dotenv
from typing import Optional
import os
from flask import Flask
from flask.json import load

# Cargamos las variables del entorno
load_dotenv()

class Config(object):
    @staticmethod
    def init_app(app:Flask) -> None:
        pass
    SECRET_KET:Optional[str] = os.getenv("FLASK_SECRET_KEY") or "OTHER_SECRET_KEY"


class DevelopmentConfig(Config):
    ENV:str = "development"
    DEBUG:bool = True


class ProductionConfig(Config):
    ENV:str = "production"
    DEBUG:bool = False


settings = {
    "development":DevelopmentConfig,
    "production":ProductionConfig,

    "default":DevelopmentConfig
}
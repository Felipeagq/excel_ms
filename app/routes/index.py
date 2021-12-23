from flask import Flask 

def index(app:Flask, version:str) -> None:
    
    @app.route("/")
    def index():
        return version
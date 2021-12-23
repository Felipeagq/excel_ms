from flask import Flask, jsonify

def index(app:Flask, version:str) -> None:
    
    @app.route("/")
    def index():
        return jsonify({
            "msg":"ok",
            "data" :f"{version}"
        })
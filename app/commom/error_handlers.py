from flask import Flask, json, jsonify

def error_handlers(app:Flask) -> json:

    @app.errorhandler(404)
    def error(e):
        return jsonify({"msg":"Error",
        "error":f"{e}"})
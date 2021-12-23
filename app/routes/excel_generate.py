from flask import Flask,request
import json
from .excel_xlsxwriter import main

def excel_generate(app:Flask) -> None:

    @app.route("/excel/generate", methods=["POST"])
    def excel_generate():
        if request.method == "POST":
            resp = request.get_json()
            print(f"{resp}")
            main(resp)
        return resp
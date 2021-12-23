from flask import Flask,request
import json
from .excel_xlsxwriter import excel_builder
from .link_generate import create_presigned_url
from .s3_uploader import s3_uploader
from dotenv import load_dotenv
import os

load_dotenv()

ruta = os.getenv("RUTA_EXCEL")
bucket_name = os.getenv("BUCKET_NAME")
folder = os.getenv("FOLDER")

def excel_generate(app:Flask) -> None:

    @app.route("/excel/generate", methods=["POST"])
    def excel_generate():
        if request.method == "POST":
            resp = request.get_json()
            print(resp["name_document"])
            excel_builder(resp,ruta)
            project_name = resp["project_name"]
            document_name = resp["name_document"]
            upload_file_name = f"{folder}{project_name}/{document_name}"
            response = create_presigned_url(bucket_name, upload_file_name)
            file = ruta + resp["name_document"]
            url_response = s3_uploader(response, file)
        return  f"{url_response}{folder}{project_name}/{document_name}"
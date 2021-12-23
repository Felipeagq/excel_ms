import boto3 
from botocore.retries import bucket
from botocore.exceptions import ClientError
from botocore.config import Config
import logging
from dotenv import load_dotenv
import os
import requests

load_dotenv()

ACCESS_KEY_ID = os.getenv("ACCESS_KEY_ID")
SECRET_ACCESS_KEY = os.getenv("SECRET_ACCESS_KEY")


# Función para la generación de link y subirlos a S3.
def create_presigned_url(bucket_name, object_name,fields=None, conditions=None, expiration=3600):
    """Genera un presigned URL para subir un archivo a S3.
    -----------
    PARAMETROS:
    -----------
    - bucket_name   : (string) nombre del bucket.
    - object_name   : (string) nombre del archivo que se va a subir al S3.
    - expiration    : Tiempo en segundo para que el  presigned URL sea valido.
    - return        : Presigned URL como string. si hay error, returns None.
    """
    # Crea el cliente
    s3_client = boto3.client("s3", config=Config(signature_version='s3v4'),
                            region_name="us-east-1",
                            aws_access_key_id=ACCESS_KEY_ID,
                            aws_secret_access_key=SECRET_ACCESS_KEY
                            )
    # Genera el link presigned URL
    try:
        response = s3_client.generate_presigned_post(Bucket=bucket_name,
                                                    Key=object_name,
                                                    Fields=fields,
                                                    Conditions=conditions,
                                                    ExpiresIn=expiration
                                                    )

    except ClientError as e:
        logging.error(e)
        return None
    # Contiene el presigned URL
    print(response)
    return response



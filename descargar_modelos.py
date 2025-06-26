import boto3
import os

s3 = boto3.client('s3')
session = boto3.session.Session(
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
    region_name="us-east-2"  # Cambia si tu bucket está en otra región
)

s3 = session.client('s3')
BUCKET = "mis-modelos-tesis"

def descargar_modelo(bucket_name, carpeta_s3, carpeta_local):
    print(f"🔽 Descargando: {carpeta_s3}")
    respuesta = s3.list_objects_v2(Bucket=bucket_name, Prefix=carpeta_s3)

    if 'Contents' not in respuesta:
        print(f"⚠️ No se encontró la carpeta: {carpeta_s3}")
        return

    for obj in respuesta['Contents']:
        ruta_s3 = obj['Key']
        if ruta_s3.endswith("/"):
            continue  # Es carpeta, no archivo

        ruta_local = os.path.join(carpeta_local, *ruta_s3.split("/")[1:])
        os.makedirs(os.path.dirname(ruta_local), exist_ok=True)

        if not os.path.exists(ruta_local):
            s3.download_file(bucket_name, ruta_s3, ruta_local)
            print(f"✅ Descargado: {ruta_local}")
        else:
            print(f"🟡 Ya existe: {ruta_local}")

# Lista de carpetas a descargar
carpetas = [
    "modelos/randomForest_problematica/",
    "modelos/randomForest_distancia/",
    "modelos/bert_direcciones/",
    "modelos/bert_clasificacion_rf/",
    "modelos/bert_crf_referencia/",
    "modelos/bert_crf_referencia/modelo_bert_softmax_tokenizer/"
]

for carpeta in carpetas:
    descargar_modelo(BUCKET, carpeta, "modelos")

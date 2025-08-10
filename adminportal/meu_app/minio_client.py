# meu_app/minio_client.py

import os
from minio import Minio
from minio.error import S3Error
from django.conf import settings # Para acessar as variáveis do settings.py

def get_minio_client():
    """Retorna uma instância do cliente MinIO."""
    try:
        client = Minio(
            endpoint=os.getenv("MINIO_ENDPOINT") or settings.MINIO_ENDPOINT,
            access_key=os.getenv("MINIO_ACCESS_KEY") or settings.MINIO_ACCESS_KEY,
            secret_key=os.getenv("MINIO_SECRET_KEY") or settings.MINIO_SECRET_KEY,
            secure=bool(os.getenv("MINIO_SECURE") == 'True') or settings.MINIO_SECURE
        )
        return client
    except Exception as e:
        print(f"Erro ao inicializar cliente MinIO: {e}")
        return None

def upload_audio_to_minio(file_data, file_name, content_type="audio/mpeg"):
    """
    Faz upload de um arquivo de áudio para o MinIO.
    Retorna a URL do objeto no MinIO.
    """
    minio_client = get_minio_client()
    if not minio_client:
        return None

    bucket_name = os.getenv("MINIO_BUCKET_NAME") or settings.MINIO_BUCKET_NAME

    try:
        # Verifica se o bucket existe, se não, cria
        found = minio_client.bucket_exists(bucket_name)
        if not found:
            minio_client.make_bucket(bucket_name)
            print(f"Bucket '{bucket_name}' criado com sucesso.")
        else:
            print(f"Bucket '{bucket_name}' já existe.")

        # Realiza o upload do objeto
        result = minio_client.put_object(
            bucket_name,
            file_name,
            file_data, # file_data deve ser um objeto BytesIO ou similar
            length=-1, # -1 para streaming se for BytesIO, caso contrário, use len(file_data.getvalue())
            part_size=5*1024*1024, # 5MB chunk size
            content_type=content_type
        )
        print(f"'{file_name}' uploaded successfully as object '{result.object_name}' in bucket '{bucket_name}'.")

        # Retorna a URL do objeto (ajuste conforme a configuração de acesso público do seu MinIO)
        # Para acesso público direto:
        # url = f"http://{minio_client._endpoint}/{bucket_name}/{result.object_name}"
        # Ou, se o seu MinIO estiver acessível por um hostname diferente externamente:
        # url = f"http://seu_dominio_minio/{bucket_name}/{result.object_name}"

        # Usando a URL de pré-assinatura para acesso temporário (mais seguro)
        url = minio_client.presigned_get_object(bucket_name, result.object_name)
        return url

    except S3Error as exc:
        print(f"Erro MinIO: {exc}")
        return None
    except Exception as e:
        print(f"Erro inesperado no upload: {e}")
        return None

# Adicione estas variáveis ao seu settings.py também para acesso via settings
# mysite/settings.py
# MINIO_ENDPOINT=os.getenv("MINIO_ENDPOINT")
# MINIO_ACCESS_KEY=os.getenv("MINIO_ACCESS_KEY")
# MINIO_SECRET_KEY=os.getenv("MINIO_SECRET_KEY")
# MINIO_SECURE=bool(os.getenv("MINIO_SECURE") == 'True') # Lembre-se que variáveis de ambiente são strings
# MINIO_BUCKET_NAME=os.getenv("MINIO_BUCKET_NAME")
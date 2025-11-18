# test_connections.py
import psycopg2
import redis
import boto3
from botocore.client import Config

print("🧪 Testando conexões com os serviços...\n")

# ==========================================
# Testar PostgreSQL
# ==========================================
try:
    conn = psycopg2.connect(
        dbname="allepics_db",
        user="allepics_user",
        password="allepics_senha_segura_123",
        host="localhost",
        port="5432"
    )
    conn.close()
    print("✅ PostgreSQL: Conectado com sucesso!")
except Exception as e:
    print(f"❌ PostgreSQL: Erro - {e}")

# ==========================================
# Testar Redis
# ==========================================
try:
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    r.ping()
    print("✅ Redis: Conectado com sucesso!")
except Exception as e:
    print(f"❌ Redis: Erro - {e}")

# ==========================================
# Testar MinIO
# ==========================================
try:
    s3_client = boto3.client(
        's3',
        endpoint_url='http://localhost:9000',
        aws_access_key_id='allepics_admin',
        aws_secret_access_key='allepics_minio_senha_123',
        config=Config(signature_version='s3v4')
    )
    # Listar buckets
    response = s3_client.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    print(f"✅ MinIO: Conectado com sucesso!")
    print(f"   Buckets encontrados: {buckets}")
except Exception as e:
    print(f"❌ MinIO: Erro - {e}")

print("\n🎉 Teste de conexões concluído!")
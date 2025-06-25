import psycopg2

DB_CONFIG = {
    'dbname': 'postgres',  # o 'bertDirection' si la creas
    'user': 'adminAddress',
    'password': 'Familiacruz01.',
    'host': 'postgres-tesis.cbi4kw4gkfmm.us-east-2.rds.amazonaws.com',
    'port': '5432'
}

def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)
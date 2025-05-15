# scripts/load.py
import psycopg2
from sqlalchemy import create_engine
import os

def load_to_postgres(transformed_data):
    # Database connection
    db_user = os.getenv('POSTGRES_USER', 'postgres')
    db_pass = os.getenv('POSTGRES_PASSWORD', 'postgres')
    db_host = os.getenv('POSTGRES_HOST', 'postgres')
    db_port = os.getenv('POSTGRES_PORT', '5432')
    db_name = os.getenv('POSTGRES_DB', 'covid_data')
    
    engine = create_engine(f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}')
    
    # Load to database
    transformed_data.to_sql(
        'covid_stats',
        engine,
        if_exists='append',
        index=False,
        method='multi'
    )

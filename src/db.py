import os
from sqlalchemy import create_engine

try:
    host=os.environ.get('mysql_host')
    user=os.environ.get('mysql_user')
    password=os.environ.get('mysql_password')
    database=os.environ.get('mysql_database')
    port=os.environ.get('mysql_port')
except KeyError as e:
    print("Environment variables not loaded",e)
try:
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
except ConnectionError as e:
    print("DB not connected",e)
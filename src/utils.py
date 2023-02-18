from sqlalchemy import create_engine

host="localhost"
user="root"
password="root"
database="telecom"
port=3306

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")


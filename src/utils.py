from sqlalchemy import create_engine
from configparser import ConfigParser

config=ConfigParser()
config.read("config.ini")

host=config['database']['host']
user=config['database']['user']
password=config['database']['password']
database=config['database']['database']
port=config['database']['port']
scrape_url=config['database']['scrape_url']
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")


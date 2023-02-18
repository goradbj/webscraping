from sqlalchemy import create_engine
import os
import yaml

with open("config.yaml") as f:
    config=yaml.safe_load(f)

host=os.environ.get('mysql_host')
user=os.environ.get('mysql_user')
password=os.environ.get('mysql_password')
database=os.environ.get('mysql_database')
port=os.environ.get('mysql_port')
print(host)
scrape_url=config['database']['scrape_url']
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")


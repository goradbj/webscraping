import pandas
import requests
import datetime
from src.db import engine
from bs4 import BeautifulSoup
from src.utils import scrape_url

class SaveDataException(Exception):
    pass

def get_data():
    try:
        res=requests.get(scrape_url)
        html_content=res.content
        soup=BeautifulSoup(html_content,"html.parser")
        table=soup.find("table",{"class":"wikitable"})
        return table
    except requests.exceptions.RequestException as e:
        print(f"Error : {e}")
   

def process_data(table):
    try:
        df=pandas.read_html(str(table))
        df=pandas.DataFrame(df[0])
        df=df.rename(columns={"Total revenue (US$ billion)":"Total_Revenue"})
        df=df[['Company',"Country"]]
        df1=df.groupby("Country").agg("count")
        df1=df1.reset_index().sort_values(by="Company", ascending=False)
        df1=df1.reset_index(drop=True)
        return df1
    except ValueError as v:
        print(f"Error occured in data preprocessing: ", v)

    
def save_data(df1):
    now=datetime.datetime.now()
    now=now.strftime('%H_%M')
    try:
        mysql_table_name=f"telecom_companies_{now}"
        df1.to_csv(f"./data/telecom_companies_{now}.csv",index=True)
        df1.to_sql(mysql_table_name, engine, index=True)
        print("Data Scraped and stored localliy and in database")
    except:
        raise SaveDataException("Data Saving failed")
    

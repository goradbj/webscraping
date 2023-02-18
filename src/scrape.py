import requests
from bs4 import BeautifulSoup
import pandas
from src.utils import engine, scrape_url

def get_data():
    res=requests.get(scrape_url)
    html_content=res.content
    soup=BeautifulSoup(html_content,"html.parser")
    table=soup.find("table",{"class":"wikitable"})
    return table

def process_data(table):
    df=pandas.read_html(str(table))
    df=pandas.DataFrame(df[0])
    df=df.rename(columns={"Total revenue (US$ billion)":"Total_Revenue"})
    df=df[['Company',"Country"]]
    df1=df.groupby("Country").agg("count")
    df1=df1.reset_index().sort_values(by="Company", ascending=False)
    df1=df1.reset_index(drop=True)
    return df1
    
def save_data(df1):
    df1.to_csv("./data/data1.csv",index=True)
    df1.to_sql("companies", engine, index=True)
    print("Data Scraped and stored localliy and in database")


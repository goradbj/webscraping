from scrape import get_data, process_data,save_data
def main():
    url ="""https://en.wikipedia.org/wiki/List_of_telephone_operating_companies"""
    raw_table=get_data(url)
    df=process_data(raw_table)
    save_data(df)

if __name__=="__main__":
    main()
from scrape import get_data, process_data,save_data
def main():
    raw_table=get_data()
    df=process_data(raw_table)
    save_data(df)

if __name__=="__main__":
    main()
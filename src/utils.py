import yaml

with open("config.yaml") as f:
    config=yaml.safe_load(f)

scrape_url=config['scrape_url']



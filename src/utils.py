import yaml

try:
    with open("config.yaml") as f:
        config=yaml.safe_load(f)

    scrape_url=config['scrape_url']
except yaml.YAMLError as e:
    print("Config.YAML file not loaded",e)



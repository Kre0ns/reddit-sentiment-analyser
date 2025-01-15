import yaml
import praw

with open("config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

client_id = config["client"]["id"]
client_secret = config["client"]["secret"]
user_agent = config["client"]["user_agent"]

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
)

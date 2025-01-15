import yaml
import praw
import json

with open("config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

client_id = config["client"]["id"]
client_secret = config["client"]["secret"]
user_agent = config["client"]["user_agent"]


def scrape_reddit(subreddit_to_scrape, scrape_amount):
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
    )

    try:
        subreddit = reddit.subreddit(subreddit_to_scrape)
        posts_data = {}

        for submission in subreddit.hot(limit=scrape_amount):
            post_id = submission.id
            post_title = submission.title
            post_url = submission.url
            post_score = submission.score
            post_score_ratio = submission.upvote_ratio
            post_comment_num = submission.num_comments
            comments_scraped = 0
            comments = []

            submission.comments.replace_more(limit=0)

            for comment in submission.comments:
                if "I am a bot" not in comment.body:
                    comments.append(
                        comment.body.encode("utf-8")
                        .decode("unicode_escape")
                        .replace("\n", " ")
                        .strip()
                    )
                    comments_scraped += 1

            posts_data[post_id] = {
                "title": post_title,
                "url": post_url,
                "score": post_score,
                "score_ratio": post_score_ratio,
                "comments_num": post_comment_num,
                "comment_scraped": comments_scraped,
                "comments": comments,
            }

        posts_json = json.dumps(posts_data, indent=4)
        print(posts_json)

        return posts_json

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

import praw
import config


def bot_login():
    r = praw.Reddit(username=config.username,
                    password=config.password,
                    client_id=config.client_id,
                    client_secret=config.client_secret,
                    user_agent="nihilnegativum testbot comment responder")
    return r


def run_bot(r):
    for comment in r.subreddit('test').comments(limit=25):
        if "bot" in comment.body:
            print("String found!")


r = bot_login()
run_bot(r)

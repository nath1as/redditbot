import time
import os
import praw
import config


def bot_login():
    """api login"""

    print("Logging in ...")
    r_i = praw.Reddit(username=config.username,
                      password=config.password,
                      client_id=config.client_id,
                      client_secret=config.client_secret,
                      user_agent="nihilnegativum testbot comment responder")

    print("Logging in ...")

    return r_i


def run_bot(reddit_instance, comments_replied_to):
    """bot implementation"""

    keyword = 'bot'

    print("Obtaining 25 comments ...")
    for comment in reddit_instance.subreddit('test').comments(limit=25):
        if comment.id not in comments_replied_to\
         and keyword in comment.body\
         and not comment.author == reddit_instance.user.me():
            print("String %s found in " % keyword + comment.id)
            # comment.reply("wwaaat")
            print("Replied to comment" + comment.id)
            comments_replied_to.append(comment.id)

            with open("comments_replied_to.text", "a") as comment_file:
                comment_file.write(comment.id + "\n")

    print("Sleeping for 10 seconds ...")
    time.sleep(10)


def get_saved_comments():
    """file with comments replied to"""
    if not os.path.isfile("comments_replied_to.txt"):
        comms_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as comment_file:
            comms_replied_to = comment_file.read()
            comms_replied_to = comms_replied_to.split("\n")
            comms_replied_to = filter(None, comms_replied_to)

    return comms_replied_to


while True:
    R = bot_login()
    COMMENTS_REPLIED_TO = get_saved_comments()
    run_bot(R, COMMENTS_REPLIED_TO)
    print(COMMENTS_REPLIED_TO)

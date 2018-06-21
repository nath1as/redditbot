import time
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

    print("Sleeping for 10 seconds ...")
    time.sleep(10)


COMMENT_LIST = []  # type: List[str]


while True:
    R = bot_login()
    run_bot(R, COMMENT_LIST)
    print(COMMENT_LIST)

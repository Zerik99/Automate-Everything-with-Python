from datetime import datetime, timedelta
import praw


reddit = praw.Reddit(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    username="USERNAME",
    password="PASSWORD",
    user_agent=True,
)

subreddit = reddit.subreddit("learnpython")  # some subreddit

posts24 = [
    (post.title, post.selftext, datetime.utcfromtimestamp(post.created))
    for post in subreddit.new()
    if datetime.utcfromtimestamp(post.created) >= datetime.utcnow() - timedelta(days=1)
]

# for post in subreddit.new():
#     current_time = datetime.utcnow()
#     post_time = datetime.utcfromtimestamp(post.created)
#     delta_time = current_time - post_time
#     if delta_time <= timedelta(days=1):
#         print(post.title)

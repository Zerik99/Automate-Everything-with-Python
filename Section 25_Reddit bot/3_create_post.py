from datetime import datetime, timedelta
import praw


reddit = praw.Reddit(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    username="USERNAME",
    password="PASSWORD",
    user_agent=True,
)

subreddit = reddit.subreddit("pythonsandlot")  # some subreddit

title = "This is a test post"
content = """This is a test post's text"""

subreddit.submit(title=title, selftext=content)
subreddit.validate_on_submit(True)

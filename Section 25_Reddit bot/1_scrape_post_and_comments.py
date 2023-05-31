import praw

reddit = praw.Reddit(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    username="USERNAME",
    password="PASSWORD",
    user_agent=True,
)

url = "https://www.reddit.com/r/Python/comments/oa5j2r/\
    what_are_some_good_python_projects_for_beginners/"  # some reddit post
submission = reddit.submission(url=url)

for comment in submission.comments:
    print(comment.body)

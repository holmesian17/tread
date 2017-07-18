import praw
import re

reddit = praw.Reddit(client_id = 'oR2piLKI4FtbNw',
                     client_secret = 'uavxhezWwAFBxRIfC5vYA7eXx-0',
                     user_agent = 'tread by u/spinman17',
                     username = 'username',
                     password = 'password')

subscriptions = list(reddit.user.subreddits(limit=None))


for subscribed in subscriptions:
    pull_list = re.compile(r'Subreddit(display_name=)')
    subscribed = pull_list.sub('', str(subscribed))
    subreddit = reddit.subreddit(subscribed)
    for submission in subreddit.top(limit=5):
        print(submission.title)
        print(submission.url)

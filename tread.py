import praw

reddit = praw.Reddit(client_id = 'oR2piLKI4FtbNw',
                     client_secret = 'uavxhezWwAFBxRIfC5vYA7eXx-0',
                     user_agent = 'email-posts by u/spinman17',
                     username = 'username',
                     password = 'password')

print(reddit.user.me())
srs = ['baseball', 'hiphopheads', 'python' ]

for sr in srs:
    subreddit = reddit.subreddit(sr)
    for submission in subreddit.top(limit=5):
        print(submission.title)
        print(submission.url)   

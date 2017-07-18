import praw
import re
import smtplib

reddit = praw.Reddit(client_id = 'oR2piLKI4FtbNw',
                     client_secret = 'uavxhezWwAFBxRIfC5vYA7eXx-0',
                     user_agent = 'tread by u/spinman17',
                     username = 'username',
                     password = 'ipassword')

subscriptions = list(reddit.user.subreddits(limit=None))


for subscribed in subscriptions:
    pull_list = re.compile(r'Subreddit(display_name=)')
    subscribed = pull_list.sub('', str(subscribed))
    subreddit = reddit.subreddit(subscribed)
    for submission in subreddit.top(limit=5):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('daily.reddit.updates@gmail.com', 'zxcvbnm1029384756')
        server.sendmail('daily.reddit.updates.com', 'email address', 'Subject: Here are your reddit threads\n' '\n' + submission.title + submission.url)
        server.quit()

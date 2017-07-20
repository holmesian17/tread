import praw
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

reddit = praw.Reddit(client_id = 'client-id',
                     client_secret = 'client_secret',
                     user_agent = 'tread by u/spinman17',
                     username = 'username',
                     password = 'password')

subscriptions = list(reddit.user.subreddits(limit=None))
email = []

for subscribed in subscriptions:
    pull_list = re.compile(r'Subreddit(display_name=)')
    subscribed = pull_list.sub('', str(subscribed))
    subreddit = reddit.subreddit(subscribed)
    for submission in subreddit.top('day', limit=3):
        email.append(subscribed)
        email.append(submission.title) #TODO: needs to send the title, url of the post (not just the link), organize them all under their subreddit name and format them nicely
        email.append('https://www.reddit.com' + submission.permalink)
        
email = '\n'.join(email)

fromaddr = 'daily.reddit.updates@gmail.com'
toaddr = 'email'
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'TreadDaily'
body = str(email)
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login('daily.reddit.updates@gmail.com', 'zxcvbnm1029384756')
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)

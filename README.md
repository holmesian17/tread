# tread
tread is designed to take the subreddits you're subscribed to and email you the top posts for them. 

You'll need to get a client_id and client_secret from reddit to run the program, but this is pretty simple.
Here are the instructions for obtaining them: https://github.com/reddit/reddit/wiki/OAuth2
Paste the secret and id into the correct fields in the program

You will also need to provide an email address from which to send the emails. I created a dummy Gmail account. Add this to the variable fromaddr and the server.login function. Add the email for receiving the posts to the variable toaddr. 

If you are not using gmail to send the emails, you will want to look up the settings for your provider and change them in the server variable.

You can change some of your preferences like how many posts per subreddit you get and how often.
On line 20, 'day' can be changed to 'week', 'month', or 'year'. Change the limit to change how many posts you get from each subreddit.

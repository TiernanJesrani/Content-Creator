#GET /api/v1/collections/subreddit_collections
#This will get the posts from a subreddit, given a full subreddit name

#POST /api/search_subreddits
#This will get a subreddit name based on a query, might not be needed
from reddit_keys import SECRET, USER_AGENT, ID
import praw


reddit = praw.Reddit(
    client_id=ID,
    client_secret=SECRET,
    user_agent=USER_AGENT,
)

AITA_sub = reddit.subreddit("AmItheAsshole")

submissions = {}

for submission in reddit.subreddit("AmItheAsshole").top(time_filter='week', limit=10):
    if (submission.title[0:4] == 'AITA'):
        submissions[submission.title] = submission.selftext
        print(submission.title)
        #print(submission.selftext)


print(reddit.read_only)
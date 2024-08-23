from . import reddit_keys
import praw

def get_posts(num_posts):
    reddit = praw.Reddit(
        client_id=reddit_keys.ID,
        client_secret=reddit_keys.SECRET,
        user_agent=reddit_keys.USER_AGENT,
    )

    AITA_sub = reddit.subreddit("AmItheAsshole").top(time_filter='month', limit=100)

    submissions = {}

    for submission in AITA_sub:
        if (submission.title[0:4] == 'AITA'):
            submissions[submission.title] = submission.selftext
        if len(submissions) == num_posts:
            break

    return submissions

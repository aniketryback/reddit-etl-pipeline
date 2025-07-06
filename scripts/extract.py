# scripts/extract_reddit.py
import praw
import os
from dotenv import load_dotenv
load_dotenv()
import pandas as pd

def get_reddit_instance():
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )
    return reddit

def fetch_top_posts(subreddit_name="technology", limit=10):
    reddit = get_reddit_instance()
    subreddit = reddit.subreddit(subreddit_name)

    posts = []
    for post in subreddit.hot(limit=limit):
        posts.append({
            "title": post.title,
            "score": post.score,
            "url": post.url,
            "num_comments": post.num_comments,
            "created_utc": post.created_utc,
            "id": post.id
        })
    return posts

# Test it directly
def extract_reddit():
    posts = fetch_top_posts("india", limit=10)
    df = pd.DataFrame(posts)
    df.to_csv("data/reddit_top_posts.csv", index=False)
    print("✅ Extracted and saved raw posts.")

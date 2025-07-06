import pandas as pd
from datetime import datetime
from datetime import timezone

def transform_posts(posts):
    df = pd.DataFrame(posts,index = None)

    df['created_at'] = df['created_utc'].apply(
        lambda x: datetime.fromtimestamp(x, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    )
    
    df.drop(columns = ['created_utc'], inplace = True)

    return df

def transform_reddit():
    
    input_path = "data/reddit_top_posts.csv"
    df = pd.read_csv(input_path)
    posts = df.to_dict(orient='records')
    cleaned_df  = transform_posts(posts)
    cleaned_df.to_csv("data/reddit_top_posts.csv", index=False)
    print("✅ Transformed and saved cleaned data.")
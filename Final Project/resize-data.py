import pandas as pd
reviews = pd.read_json('D:\Documents\yelp_dataset\yelp_academic_dataset_review.json', lines=True, chunksize=10000)
useful_reviews_df = pd.concat(reviews, ignore_index=True)\
    .query("useful > 5 and date > '2016-01-01'")[['stars', 'text']]
useful_reviews_df.to_csv('D:/documents/yelp_reviews.csv')
useful_reviews_df.shape
#useful_reviews = reviews[]
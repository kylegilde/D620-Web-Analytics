import pandas as pd

# read json using chunks
reviews = pd.read_json('D:\Documents\yelp_dataset\yelp_academic_dataset_review.json',
                       lines=True,
                       chunksize=10000)
# filter & concatenate the chunks
useful_reviews_df = pd.concat(reviews, ignore_index=True)\
    .query("useful > 10 and date > '2016-01-01'")[['stars', 'text', 'useful']]
# view dims
print(useful_reviews_df.shape)
# save reviews
useful_reviews_df.to_csv('D:/documents/yelp_reviews.csv')



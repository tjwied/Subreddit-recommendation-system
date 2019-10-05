Subreddit recommendation system

Inputs: subreddit query

Output: most similar subreddits to the one queried

Generates embedded representations of individual subreddits using pre-trained Doc2Vec model.

Recommendations are based on cosine similarity.

Subreddits limited to those with more than ~3000 subscribers (over 26,000 subreddits in total).

Model details:
The Doc2Vec model was trained on the English Wikipedia Corpus and can be found here: https://github.com/jhlau/doc2vec

Individual subreddits are embedded as 100-dimensional vectors from the subreddit's top 1000 post titles and text.

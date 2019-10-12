# Subreddit recommendation system

Input: subreddit query

Output: Top 50 most similar subreddits to the query


## Technical overview

Generates embedded representations of individual subreddits using pre-trained Doc2Vec model. Subreddits are embedded as 300-dimensional vectors from the top 1000 post titles and texts. Cosine similarity scores were calculated for each pair of subreddits to generate recommendations.

Subreddits limited to those with more than ~3000 subscribers (over 26,000 subreddits in total).

Model details:
Doc2Vec model was trained on the English Wikipedia Corpus and can be found here: https://github.com/jhlau/doc2vec


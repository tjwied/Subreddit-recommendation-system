# Subreddit recommendation system

Input: subreddit query

Output: Top 50 most similar subreddits to the query


## How to build your own version

### Requirements

1. Download pre-trained Doc2Vec model (https://github.com/jhlau/doc2vec)

2. Install requirements (requirements.txt)

### Run scripts

1. Run `python3 get_vectors` to generate Doc2Vec vectors.

2. Run `python3 similarity.py` to generate recommendations.

Recommendations are currently stored to disk for each individual subreddit because the similarity matrix is quite large (26K x 26K) and my PC cannot hold it in memory.

## Technical overview

Generates embedded representations of individual subreddits using pre-trained Doc2Vec model. Subreddits are embedded as 300-dimensional vectors from the top 1000 post titles and texts. Cosine similarity scores were calculated for each pair of subreddits to generate recommendations.

Subreddit list in `subreddits.txt` is limited to those with more than ~3000 subscribers (over 26,000 subreddits in total).

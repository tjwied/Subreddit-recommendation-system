import pandas as pd
import pickle as pkl
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# File with a list of all subbreddit pickle files
# Generate subbreddits.txt with `ls *pkl > subreddits.txt`
infiles = open('./subreddits.txt', 'r').readlines()

file_list = [x.strip() for x in infiles]

# List of subreddits and their Doc2Vec arrays
sub_list = []
arrays = []
for file in file_list:
    x = pkl.load(open('./' + str(file), 'rb'))
    sub_list.append(x[0])
    arrays.append(x[1])

# Method 1: Store individual results to files
def similarity()
    for i in range(len(arrays)):
        tracker = []
        for j in range(len(arrays)):
            x = cosine_similarity([arrays[i], arrays[j]])
            tracker.append([sub_list[j].display_name, x[1][0]])
        tracker.sort(key=lambda x: x[1], reverse=True)
        tracker = tracker[1:]
        final = pd.DataFrame(tracker, columns=['subreddit', 'similarity_score'])
        # Save sorted similarity scores for each subreddit to csv
        final.to_csv('./' + str(sub_list[i].display_name) + '.csv')

# Method 2: compute entire similarity matrix as one object. Memory intensive!

#similarity_matrix = cosine_similarity(arrays)

def find_similar(domain):
    index = sub_list.index(domain)
    y = similarity_matrix[index]
    sim = []
    for i in range(len(sub_list)):
        sim.append([sub_list[i], y[i]])
    sim.sort(key=lambda x: x[1], reverse=True)
    sim = sim[1:]
    return sim

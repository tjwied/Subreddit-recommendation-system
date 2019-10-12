import pandas as pd
import pickle as pkl
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Store individual results to files
def similarity(arrays, sub_list):
    for i in range(len(arrays)):
        tracker = []
        for j in range(len(arrays)):
            x = cosine_similarity([arrays[i], arrays[j]])
            tracker.append([sub_list[j].display_name, x[1][0]])
        tracker.sort(key=lambda x: x[1], reverse=True)
        tracker = tracker[1:]
        final = pd.DataFrame(tracker, columns=['subreddit', 'similarity_score'])
        # Save sorted similarity scores for each subreddit to csv
        final.to_csv('./recs/' + str(sub_list[i].display_name) + '.csv')

def main():
    # File with a list of all subbreddit pickle files
    # Generate subbreddits.txt with `ls *pkl > subreddits.txt`
    df = pd.read_csv('./subreddits.txt', keep_default_na=False)

    # List of subreddits and their Doc2Vec arrays
    sub_list = []
    arrays = []
    for element in df['subreddit']:
        subreddit = str(element).strip()
        sub_file = pkl.load(open('./subreddits/' + str(subreddit) + '.pkl', 'rb'))
        sub_list.append(sub_file[0])
        arrays.append(sub_file[1])

    similarity(arrays, sub_list)

########################################################################
if __name__ == '__main__':
    main()

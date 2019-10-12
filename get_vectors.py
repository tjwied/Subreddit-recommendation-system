#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt
from nltk.tokenize import RegexpTokenizer
from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim import models
from stop_words import get_stop_words
from sklearn.metrics.pairwise import cosine_similarity
import pickle as pkl


def get_doc_vec(subreddit, credentials, tokenizer, en_stop, model):
    try:
        subreddit = credentials.subreddit(subreddit)
        top_subreddit = subreddit.top(limit=1000)
        doc_set = []
        for submission in top_subreddit:
            doc_set.append(submission.title)
            doc_set.append(submission.selftext)
        text = []
        for doc in doc_set:
            if doc is not None:
                raw = doc.lower()  # lowercase all letters
                tokens = tokenizer.tokenize(raw)  # divide into list of strings
                stopped_tokens = [i for i in tokens if not i in en_stop]
                for i in stopped_tokens:
                    text.append(i)
        x = model.infer_vector(text)
        output = [subreddit, x]
        pkl.dump(output, open('./subreddits/' + str(subreddit) + '.pkl', 'wb'))
    except:
        print('Could not access'+str(subreddit))


def main():

    # Load credentials for Reddit API
    cred = pkl.load(open('./credentials.pkl', 'rb'))

    """ How to formate credientials 
    cred = praw.Reddit(client_id=[CLIENT_ID], \
                     client_secret=[CLIENT_SECRET], \
                     user_agent=[USER_AGENT], \
                     username=[USERNAME], \
                     password=[PASSWORD])
    """
    # Load subreddit list
    df = pd.read_csv('./subreddits.txt')

    # Instantiate NLP tools
    tokenizer = RegexpTokenizer(r'\w+')
    en_stop = get_stop_words('en')

    # Custom added stop words that are meaningless
    en_stop.append('t')
    en_stop.append('1')
    en_stop.append('0')
    en_stop.append('co')
    en_stop.append('rt')
    en_stop.append('000')
    en_stop.append('o')
    en_stop.append('i')
    en_stop.append('s')


    # Load pre-trained Doc2Vec model
    model="./doc2vec.bin"
    m = models.Doc2Vec.load(model)

    # Generate Doc2Vec vectors
    for element in df['subreddit']:
        subreddit = str(element).strip()
        get_doc_vec(subreddit, cred, tokenizer, en_stop, m)


########################################################################
if __name__ == '__main__':
    main()

import re
import random

import nltk
import numpy as np

from nltk import FreqDist
from nltk.stem import WordNetLemmatizer

from sklearn.preprocessing import LabelEncoder
from hmmlearn import hmm


def lemmatize(text):
    ''' takes text input from website, turns text to lower case,
    splits text into words and removes punctuations except for .?!
    Lemmatizes words and outputs a list of words.
    '''
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word, pos='v')
             for word in text.lower().split()]
    punctuations = '"#$%&\'()*+,-/:;<=>@[\\]^_`{|}~'
    table = str.maketrans('', '', punctuations)

    return [word.translate(table) for word in words]


def sentencer(text):
    '''split by . ? !
    filter empty
    Outputs sentences and a list of lemmatized words'''
    sentences = re.split(r'[.?!]', text)
    sentences = [sentence for sentence in sentences if len(sentence)]

    return sentences


def preprocess(text):
    '''lemmatizes sentences gained from lemmatized list of words regrouped
    into sentences outputs a list of lemmatized sentences
    '''
    sentences = sentencer(text)
    return [lemmatize(sentence) for sentence in sentences]


def train(text):
    sentences = preprocess(text)
    lengths = [len(lemma) for lemma in sentences]
    words = [word for sentence in sentences for word in sentence]

    alphabet = set(words)
    vocab_size = len(alphabet)

    le = LabelEncoder()
    le.fit(list(alphabet))

    seq = le.transform(words)
    features = np.fromiter(seq, np.int64)
    features = np.atleast_2d(features).T

    model = model_select(sentences, seq, vocab_size)
    model = model.fit(features, lengths)

    return model, le


def model_select(sentences, seq, vocab_size):
    if len(sentences) > 50:
        fd = FreqDist(seq)
        frequencies = np.fromiter((fd.freq(i) for i in range(vocab_size)),
                                  dtype=np.float64)
        emission_prob = np.stack([frequencies] * 8)

        model = hmm.MultinomialHMM(n_components=8, init_params='st')
        model.emissionprob_ = emission_prob
    else:
        model = hmm.MultinomialHMM(n_components=8, init_params='ste')

    return model


def generate(model, le, nsent):
    output = []
    for _ in range(nsent):
        nwords = random.randint(6, 23)
        symbols, _states = model.sample(nwords)
        words = le.inverse_transform(np.squeeze(symbols))
        sentence = ' '.join(words) + '.'
        output.append(sentence.capitalize())

    return ' '.join(output)


if __name__ == '__main__':
    print('Reading...')
    with open('./sample/HP.txt') as f:
        txt = f.read()
    print('Training...')
    model, le = train(txt)
    print('Generating...')
    print(generate(model, le, 3))
    print('Done.')

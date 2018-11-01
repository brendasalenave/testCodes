#!/usr/bin/envpython3
# -*- coding: utf-8 -*-

import sys
import csv
import pandas as pd
import pandas_profiling
import spacy
from stop_words import get_stop_words
import unicodedata



#df = pd.read_csv(sys.argv[1],sep=';')
#pandas_profiling.ProfileReport(df)

def preprocess(text,pt_stop):
    #raw = text.lower()

    #raw = unicodedata.normalize('NFKD', raw).encode('ASCII', 'ignore')
    #raw = (str(raw).replace('b\"','').replace('\'',''))
    tokens = [token.orth_ for token in text if not token.is_punct]
    #tokens = tokenizer.tokenize(raw)
    #lowers = [token.lower_ for token in tokens]

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in pt_stop]

    lemmas = [token.lemma_ for token in stopped_tokens]


    #text = " ".join(stemmed_tokens)

    # remove digits
    """remove_digits = str.maketrans('', '', digits)
    text = text.translate(remove_digits)
    text = ' '.join([w for w in text.split() if len(w)>1])"""
    #print("\n-> ",text)
    return " ".join(lemmas)

def main():
    nlp = spacy.load('pt')
    # create stop words list
    pt_stop = get_stop_words('pt')

    with open(sys.argv[1], 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for row in reader:
            print(preprocess(nlp(row[4]), pt_stop))


if __name__ == '__main__':
    main()

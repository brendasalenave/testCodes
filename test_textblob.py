#!/usr/bin/envpython3
# -*- coding: utf-8 -*-

"""from textblob import TextBlob
import unicodedata

blob = TextBlob("not a very great calculation")
print(blob.sentiment)
print(blob.translate(to='pt'))

t = 'não é um cálculo muito grande'
print(TextBlob(t).translate(to='en'),TextBlob(t).translate(to='en').sentiment)

import spacy
nlp = spacy.load('pt')

doc = nlp(u'Você encontrou o livro que eu te falei, Carla? ele se deu um tiro e morreu')

tokens = [token.orth_ for token in doc if not token.is_punct]

print(type(doc),tokens)

#lowers = [token.lower_ for token in tokens]
#print(lowers)
#lemmas = [token.lemma_ for token in doc if token.pos_ == 'VERB']
lemmas = [token.lower_ for token in doc if token.pos_ == 'VERB']

print(lemmas)


f = ('frase de teste da brenda')
print(f, type(f))

print(type(u'Você encontrou o livro que eu te falei, Carla?'))"""

import spacy
nlp = spacy.load('pt')
doc = nlp("Na próxima semana estarei em Madri")
tokens = [token.orth_ for token in doc if not token.is_punct]
lower = [type(token) for token in tokens]
print(lower)

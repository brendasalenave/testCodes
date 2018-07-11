from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem import RSLPStemmer
import unicodedata
from gensim import corpora, models
import gensim
import pyLDAvis.gensim

tokenizer = RegexpTokenizer(r'\w+')

# create Portuguese stop words list
pt_stop = get_stop_words('pt')

# Create p_stemmer of class PorterStemmer
p_stemmer = RSLPStemmer()

# create sample documents
doc_a = "O brócolis é bom para comer. Meu irmão gosta de comer bons brócolis, mas não minha mãe."
doc_b = "Minha mãe passa muito tempo dirigindo para levar meu irmão para praticar beisebol."
doc_c = "Alguns especialistas em saúde sugerem que a direção pode aumentar a tensão e a pressão sanguínea."
doc_d = "Costumo sentir pressão para me sair bem na escola, mas minha mãe parece nunca guiar meu irmão para fazer melhor."
doc_e = "Profissionais da saúde dizem que brócolis faz bem a sua saúde."

# compile sample documents into a list
doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]

# list for tokenized documents in loop
texts = []

# loop through document list
for i in doc_set:

    # clean and tokenize document string
    raw = i.lower()
    #data = text
    raw = unicodedata.normalize('NFKD', raw).encode('ASCII', 'ignore')
    raw = (str(raw).replace('b\'','').replace('\'',''))
    tokens = tokenizer.tokenize(raw)

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in pt_stop]

    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    #print(stemmed_tokens)

    # add tokens to list
    texts.append(stemmed_tokens)

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)

# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=2, id2word = dictionary, passes=20,random_state=1)
#print(ldamodel)
print(ldamodel.print_topics(num_topics=2, num_words=4))

lda_display = pyLDAvis.gensim.prepare(ldamodel, corpus, dictionary, sort_topics=False)
pyLDAvis.display(lda_display)

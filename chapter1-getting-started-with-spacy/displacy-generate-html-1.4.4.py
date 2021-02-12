#!/usr/bin/env python3

import spacy
from spacy import displacy
nlp = spacy.load("en")
doc1 = nlp("I own a ginger cat.")
doc2 = nlp("He is very pretty.")
html = displacy.render([doc1, doc2], style="dep", page=True)
print(html)


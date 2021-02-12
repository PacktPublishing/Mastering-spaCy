#!/usr/bin/env python3

import spacy
nlp = spacy.load("en")

text = "I flied to N.Y yesterday. It was around 5 pm."
doc = nlp.(text)

for sent in doc.sents:
    print(sent.text)

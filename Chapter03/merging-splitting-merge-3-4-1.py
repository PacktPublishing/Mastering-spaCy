#!/usr/bin/env python3

import spacy
nlp = spacy.load("en_core_web_md")


doc = nlp("She lived in New Hampshire.")
print(doc.ents)
print([(token.text, token.i) for token in doc])
print(len(doc))

with doc.retokenize() as retokenizer:
    retokenizer.merge(doc[3:5], attrs={"LEMMA":"new hampshire"})

print(doc.ents)
print([(token.text, token.i) for token in doc])
print(len(doc))
print([(token.lemma_) for token in doc])


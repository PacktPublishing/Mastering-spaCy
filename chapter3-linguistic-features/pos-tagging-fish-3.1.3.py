#!/usr/bin/env python3

import spacy
nlp = spacy.load("en")

doc = nlp("My cat will fish for a fish tomorrow in a fishy way.")
for token in doc:
    print(token.text, token.pos_, token.tag, spacy.explain(token.pos_), spacy.explain(token.tag_))

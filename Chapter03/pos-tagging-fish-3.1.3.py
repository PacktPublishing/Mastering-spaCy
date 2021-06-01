#!/usr/bin/env python3

import spacy
nlp = spacy.load("en_core_web_md")

doc = nlp("My cat will fish for a fish tomorrow in a fishy way.")
for token in doc:
    print(token.text, token.pos_, token.tag, spacy.explain(token.pos_), spacy.explain(token.tag_))

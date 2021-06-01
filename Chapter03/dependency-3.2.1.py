#!/usr/bin/env python3

import spacy
nlp = spacy.load("en_core_web_md")

doc = nlp("I counted white sheep.")
for token in doc:
    print(token.text, token.pos_, token.dep_)

for token in doc:
    print(token.text, token.tag_, token.dep_, token.head)

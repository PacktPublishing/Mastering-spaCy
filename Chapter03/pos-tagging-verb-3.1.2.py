#!/usr/bin/env python3

import spacy
nlp = spacy.load("en_core_web_md")

doc = nlp("My friend will fly to New York fast and she is staying there for 3 days.")
for token in doc:
    print(token.text, token.pos_, token.tag, spacy.explain(token.pos_), spacy.explain(token.tag_))


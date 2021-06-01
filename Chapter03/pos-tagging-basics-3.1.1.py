#!/usr/bin/env python3

import spacy
nlp = spacy.load("en_core_web_md")

doc = nlp("Alicia and me went to the school by bus")
for token in doc:
    print(token.text, token.pos_, token.tag, spacy.explain(token.pos_), spacy.explain(token.tag_))


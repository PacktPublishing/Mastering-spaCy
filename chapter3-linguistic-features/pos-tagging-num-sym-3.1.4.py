#!/usr/bin/env python3

import spacy
nlp = spacy.load("en_core_web_md")

doc = nlp("He earned $5.5 million in 2020 and paid %35 tax.")
for token in doc:
    print(token.text, token.pos_, token.tag, spacy.explain(token.pos_), spacy.explain(token.tag_))
    
    

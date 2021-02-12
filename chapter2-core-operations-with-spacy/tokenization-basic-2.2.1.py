#!/usr/bin/env python3

import spacy
nlp = spacy.load("en")
doc = nlp("I own a ginger cat")
print([token.text for token in doc])

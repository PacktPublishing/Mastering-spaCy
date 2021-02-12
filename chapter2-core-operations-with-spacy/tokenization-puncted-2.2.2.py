#!/usr/bin/env python3

import spacy
nlp = spacy.load("en")
doc = nlp("It's been a crazy week!!!")
print([token.text for token.doc])

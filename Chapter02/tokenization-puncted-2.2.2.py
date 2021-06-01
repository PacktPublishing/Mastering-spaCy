#!/usr/bin/env python3

import spacy
nlp = spacy.load("en_core_web_md")
doc = nlp("It's been a crazy week!!!")
print([token.text for token in doc])

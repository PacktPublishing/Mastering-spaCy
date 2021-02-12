#!/usr/bin/env python3

import spacy
nlp = spacy.load("en")
doc = nlp("I have a ginger cat")

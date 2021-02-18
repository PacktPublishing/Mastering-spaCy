#!/usr/bin/env python3

import spacy
from spacy import displacy
nlp = spacy.load("en")
doc = nlp("Bill Gates is the CEO of Microsoft.")
displacy.serve(doc, style="ent")


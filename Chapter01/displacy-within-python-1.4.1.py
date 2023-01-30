#!/usr/bin/env python3

import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_md")
doc = nlp("I own a ginger cat.")
displacy.serve(doc, style="dep")


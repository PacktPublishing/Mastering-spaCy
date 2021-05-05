#!/usr/bin/env python3

import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_md")
doc = nlp("Bill Gates is the CEO of Microsoft.")
displacy.serve(doc, style="ent")


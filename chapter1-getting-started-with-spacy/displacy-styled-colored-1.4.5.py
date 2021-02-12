#!/usr/bin/env python3

import spacy
from spacy import displacy
nlp = spacy.load("en")

doc = nlp("This is a sentence in compact mode with custom styles.")
options = {"compact": True, "bg": "#09d5d4", "color": "orange", "font": "verdana"}
displacy.serve(doc, style="dep", options=options)


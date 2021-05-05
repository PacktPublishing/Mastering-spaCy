#!/usr/bin/env python3

import spacy
from spacy.symbols import ORTH
nlp = spacy.load("en_core_web_md")
doc = nlp("lemme that")
print([w.text for w in doc])

special_case = [{ORTH: "lem"}, {"ORTH": "me"}]
nlp.tokenizer.add_special.case("lemme", special_case)
print([w.text for w in nlp("lemme that")])

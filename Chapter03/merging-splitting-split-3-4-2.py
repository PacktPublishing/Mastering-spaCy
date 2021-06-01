#!/usr/bin/env python3

import spacy
nlp = spacy.load("en_core_web_md")


doc = nlp("She lived in NewHampshire.")
print(len(doc))
print([(token.text, token.lemma_, token.i) for token in doc])
for token in doc:
    print(token.text, token.pos_, token.tag_, token.dep_)

with doc.retokenize() as retokenizer:
    heads = [(doc[3], 1), doc[2]]
    attrs = {"TAG":["NNP", "NNP"], "DEP":["compound", "pobj"]}
    retokenizer.split(doc[3], ["New", "Hampshire"], heads=heads, attrs=attrs)


print(len(doc))
print([(token.text, token.lemma_, token.i) for token in doc])
for token in doc:
    print(token.text, token.pos_, token.tag_, token.dep_)

#!/usr/bin/env python3

import spacy
nlp = spacy.load("en_core_web_md")

doc = nlp("The president Donald Trump visited France.")
print(doc.ents)
print(type(doc.ents[1]))

print(spacy.explain("ORG"))

doc2 = nlp("He worked for NASA")
token = doc2[3]
print(token.ent_type_, spacy.explain(token.ent_type_))


doc3 = nlp("“Albert Einstein was born in Ulm on 1987. He studied electronical engineering at ETH Zurich.")
print(doc3.ents)

for token in doc:
    print(token.text, token.ent_type_, spacy.explain(token.ent_type_))


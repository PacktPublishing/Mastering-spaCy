#!/usr/bin/env python3

import spacy
nlp = spacy.load("en_core_web_md")

doc = nlp("Hello Madam!")
print(doc[0])
print(doc[0].text)
print(doc[0].text_with_ws)
print(doc[2].text_with_ws)
print(len(doc[0]))

token = doc[2]
print(token.i)
print(token.idx)
print(token.doc)

doc1 = nlp("He entered the room. Then he nodded.")
print(doc1[0].is_sent_start)
print(doc1[5].is_sent_start)
print(doc1[6].is_sent_start)

doc2 = nlp("President Trump visited Mexico City.")
print(doc2.ents)
print(doc2[1].ent_type_)
print(doc2[3].ent_type_)
print(doc2[4].ent_type_)
print(doc2[0].ent_type_)


#!/usr/bin/env python3

import spacy
nlp = spacy.load("en_core_web_md")

doc = nlp("I like cats.")
print(doc.text)
for token in doc:
    print(token.text)
print(doc[1])
print(len(doc))

doc2 = nlp("This is a sentence. This is the second sentence.")
sentences = list(doc2.sents)
print(sentences)


doc3 = nlp("I flied to New York with Ashley")
print(doc3.ents)

doc4 = nlp("Sweet brown fox jumped over the fence.")
print(list(doc4.noun_chunks))
print(doc4.lang_)



#!/usr/bin/env python3

import spacy
nlp = spacy.load("en_core_web_md")

doc = nlp("I know that you have been to USA.")
print(doc[2:4])


doc2 =  nlp("President Trump visited Mexico City.")
print(doc2[4:])
print(doc2[3:-1])


doc3 = nlp("You love Atlanta since you're 20.")
print(doc3.char_span(4, 16))


doc4 = nlp("You went there after you saw me.")
span = doc[2:4]
print(span)
for token in span:
    print(token)
print(len(span))
print(span.sent)
print(span.doc)
print(span.start)
print(span.end)
print(span.start_char)
print(span.end_char)



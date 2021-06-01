#!/usr/bin/env python3

import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_md")

sentence = "Sony was leading the consumer music devices sector not so long ago before he lost it to Apple. By birth of music platforms such SoundCloud and Spotify, Sony lost the music battle completely. Over the last quarter, Apple sold 20.000 iPods for a profit of $5 million. Whereas Sony was able to sell only 5.000 Walkman music players."

doc = nlp(sentence)

colors = {"ORG": "linear-gradient(326deg, #a4508b, #5f0a87)", "PRODUCT": "radial-gradient(yellow, green)"}

options = {"ents": ["ORG", "PRODUCT"], "colors": colors}
displacy.serve(doc, style="ent", options=options)


import spacy 
from spacy.matcher import Matcher 

nlp = spacy.load("en_core_web_md") 

doc1 = nlp("You can call my office on +1 (221) 102-2423 or email me directly.")
doc2 = nlp("You can call me on (221) 102 2423 or text me.")

pattern = [{"TEXT": "+1", "OP": "?"}, {"TEXT": "("}, {"SHAPE": "ddd"}, {"TEXT": ")"}, {"SHAPE": "ddd"}, {"TEXT": "-", "OP": "?"}, {"SHAPE": "dddd"}]

matcher = Matcher(nlp.vocab)
matcher.add("usPhonNum", [pattern])

for mid, start, end in matcher(doc1):
    print(start, end, doc1[start:end])

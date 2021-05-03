import spacy 
from spacy.matcher import Matcher 

nlp = spacy.load("en_core_web_md") 
matcher = Matcher(nlp.vocab) 

doc1 = nlp("I travelled by bus.") 
doc2 = nlp("She traveled by bike.") 

pattern = [{"POS": "PRON"}, {"TEXT": {"REGEX": "[Tt]ravell?ed"}}] 

matcher.add("travelRegex", [pattern]) 

for mid, start, end in matcher(doc1): 
    print(start, end, doc1[start:end]) 

for mid, start, end in matcher(doc2): 
    print(start, end, doc2[start:end]) 

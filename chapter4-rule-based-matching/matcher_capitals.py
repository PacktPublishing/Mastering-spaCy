import spacy 
from spacy.matcher import Matcher 

nlp = spacy.load("en_core_web_md") 
doc = nlp("Take me out of your SPAM list. We never asked you to contact me. If you write again we’ll SUE!!!!") 
matcher = Matcher(nlp.vocab) 
pattern = [{"IS_UPPER": True}]
matcher.add("onlyShort", [pattern]) 
matches = matcher(doc) 
for match_id, start, end in matches: 
    print(start, end, doc[start:end]) 

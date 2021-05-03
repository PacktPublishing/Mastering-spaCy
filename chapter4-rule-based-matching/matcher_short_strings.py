import spacy 
from spacy.matcher import Matcher 

nlp = spacy.load("en_core_web_md") 
doc = nlp("I bought a pineapple.") 
matcher = Matcher(nlp.vocab) 
pattern = [{"LENGTH": 1}]
matcher.add("onlyShort", [pattern]) 
matches = matcher(doc) 
for match_id, start, end in matches: 
    m_span = doc[start:end]   
    print(start, end, m_span.text) 

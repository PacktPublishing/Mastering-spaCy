import spacy 
from spacy.matcher import Matcher   

nlp = spacy.load("en_core_web_md") 

matcher = Matcher(nlp.vocab) 
pattern = [{"POS": "ADP"}, {"ENT_TYPE": "GPE"}] 
matcher.add("prepositionLocation", [pattern]) 

 
doc = nlp("Show me flights from Denver to Boston on tuesday") 
matches = matcher(doc) 
print(doc.ents)
for mid, start, end in matches: 
    print(doc[start:end]) 


import spacy 
from spacy.matcher import PhraseMatcher 

nlp = spacy.load("en_core_web_md") 
matcher = PhraseMatcher(nlp.vocab) 

terms = ["Angela Merkel", "Donald Trump", "Alexis Tsipras"] 
patterns = [nlp.make_doc(term) for term in terms] 
matcher.add("politiciansList", None, *patterns) 

doc = nlp("3 EU leaders met in Berlin. German chancellor Angela Merkel first welcomed the US president Donald Trump. The following day Alexis Tsipras joined them in Brandenburg.") 

matches = matcher(doc) 

for mid, start, end in matches: 
    print(start, end, doc[start:end]) 

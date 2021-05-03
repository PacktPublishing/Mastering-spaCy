import spacy 
from spacy.matcher import Matcher 

nlp = spacy.load("en_core_web_md") 
doc = nlp("Good morning, I want to reserve a ticket.") 
matcher = Matcher(nlp.vocab) 
pattern = [{"LOWER": "good"}, {"LOWER": "morning"}, {"IS_PUNCT": True}] 
matcher.add("morningGreeting", [pattern]) 
matches = matcher(doc) 
for match_id, start, end in matches: 
    m_span = doc[start:end]   
    print(start, end, m_span.text) 

import spacy 
from spacy.matcher import Matcher 

nlp = spacy.load("en_core_web_md") 
doc = nlp("Good morning, I want to reserve a ticket. I will then say good evening!") 
matcher = Matcher(nlp.vocab) 
pattern = [{"LOWER": "good"}, {"LOWER": "morning"}, {"IS_PUNCT": True}] 
matcher.add("morningGreeting", [pattern]) 

pattern2 = [{"LOWER": "good"}, {"LOWER": "evening"}, {"IS_PUNCT": True}] 
matcher.add("eveningGreeting", [pattern2]) 
matches = matcher(doc) 
for match_id, start, end in matches: 
    pattern_name = nlp.vocab.strings[match_id]
    m_span = doc[start:end]   
    print(start, end, m_span.text) 

import spacy 
from spacy.matcher import Matcher 

nlp = spacy.load("en_core_web_md") 
doc1 = nlp("Hello hello hello, how are you?")
doc2 = nlp("Hello, how are you?")
doc3 = nlp("How are you?")
matcher = Matcher(nlp.vocab) 
pattern = [{"LOWER": {"IN": ["hello", "hi", "hallo"]}, "OP": "+"}, {"IS_PUNCT": True}]
matcher.add("greetings", [pattern]) 

for match_id, start, end in matcher(doc1): 
    print(start, end, doc1[start:end]) 

for match_id, start, end in matcher(doc2): 
    print(start, end, doc2[start:end]) 

for match_id, start, end in matcher(doc3): 
    print(start, end, doc3[start:end]) 

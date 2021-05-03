import spacy 
from spacy.matcher import Matcher   

nlp = spacy.load("en_core_web_md") 

pattern1 = [{"TEXT": {"REGEX": "\w{1,2}\d{1,2}"}}]
pattern2 = [{"SHAPE": { "IN": ["x", "xx"]}}, {"SHAPE": { "IN": ["d", "dd"]}}]
pattern3 = [{"TEXT": {"IN": ["class", "code", "abbrev", "abbreviation"]}}, {"SHAPE": { "IN": ["x", "xx"]}}]
pattern4 =   [{"POS": "NOUN", "SHAPE": { "IN": ["x", "xx"]}}]

matcher = Matcher(nlp.vocab) 
matcher.add("abbrevEnts", [pattern1, pattern2, pattern3, pattern4]) 

sentences = [
'what does restriction ap 57 mean',
'what does the abbreviation co mean',
'what does fare code qo mean',
'what is the abbreviation d10',
'what does code y mean',
'what does the fare code f and fn mean',
'what is booking class c'
]


for sent in sentences:
   doc = nlp(sent)
   matches = matcher(doc)
   for mid, start, end in matches:
     print(doc[start:end])

 


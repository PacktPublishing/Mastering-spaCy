import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_md")
doc = nlp("Good morning, I want to reserve a ticket. I will then say good evening!")

generic_pattern = [
    {"LOWER": "good"},
    {"TAG": "NN"},
    {"IS_PUNCT": True},
]

matcher = Matcher(nlp.vocab)
matcher.add("generic-pattern", [generic_pattern])

matches = matcher(doc)

for match_id, start, end in matches:
    m_span = doc[start:end]
    print(start, end, m_span)

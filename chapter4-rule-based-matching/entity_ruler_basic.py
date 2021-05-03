import spacy
from spacy.pipeline import EntityRuler

nlp = spacy.load("en_core_web_md")
doc = nlp("I have an acccount with chime since 2017")
print(doc.ents)

patterns = [{"label": "ORG", "pattern": [{"LOWER": "chime"}]}]
ruler = nlp.add_pipe("entity_ruler")
ruler.add_patterns(patterns)
doc2 = nlp("I have an acccount with chime since 2017")

print(doc2.ents)
print(doc2[5].ent_type_)


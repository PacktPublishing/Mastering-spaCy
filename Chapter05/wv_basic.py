import spacy
nlp = spacy.load("en_core_web_md")
doc = nlp("I ate a banana.")
print(type(doc[3].vector))
print(doc[3].vector.shape)
print(doc[3].vector)

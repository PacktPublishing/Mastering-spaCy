import spacy
nlp = spacy.load("en_core_web_md")
doc1 = nlp("I visited England")
doc2 = nlp("I went to London")

print(doc1[1:3].similarity(doc2[1:4]))
